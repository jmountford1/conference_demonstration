from classes.Database import MySQLConnector
from classes.AI import AI
from classes.Redis import RedisConnector

class Processor:
    @staticmethod
    def initial_connection_handshake(request_data):
        with MySQLConnector() as MySQL:
            username = request_data['USERNAME']
            reference_id = MySQL.get_user_reference_id(username)
            print("Reference ID (User's ID): " + str(reference_id))
            conversation_data = MySQL.retrieve_conversation_pointers(reference_id)
            print("Conversations: " + str(conversation_data))
        return conversation_data
    
    @staticmethod
    def new_conversation_handler(request_data):
        new_conversation_id = None
        with MySQLConnector() as MySQL:
            username = request_data['USERNAME']
            reference_id = MySQL.get_user_reference_id(username)
            new_conversation_id = MySQL.create_new_conversation(reference_id)
            print('New conversation ID: ' + str(new_conversation_id))
        with RedisConnector() as Redis:
            Agent = AI()
            Redis.start_conversation_history(Agent.context, new_conversation_id)

        return_data = {
            'NEW_CONVERSATION_ID': new_conversation_id
        }
        return return_data

    @staticmethod
    def continue_conversation_handler(request_data):
        message_body = request_data['USER_MESSAGE']
        conversation_id = request_data['CONVERSATION_ID']
        customer_lookup_id = request_data['TARGET_CUSTOMER_ID']

        Agent = AI()
        Agent.attach_prompt(message_body)
        str_selected_keywords = Agent.check_keywords()
        print('Selected keywords: ' + str_selected_keywords)
        raw_data = []
        with MySQLConnector() as MySQL:
            if "CONTACT_INFO" in str_selected_keywords:
                raw_data.append(MySQL.retrieve_customer_contact_info(customer_lookup_id))
            if "MAILING_ADDRESS" in str_selected_keywords:
                raw_data.append(MySQL.retrieve_customer_mailing_address(customer_lookup_id))
            if "CUSTOMER_HISTORY" in str_selected_keywords:
                raw_data.append(MySQL.retrieve_customer_history(customer_lookup_id))
        print("Raw data: " + str(raw_data))

        data_points = raw_data
        summarized_data_points = Agent.analyze_customer_data(str(raw_data))
        print("Summarized data: " + summarized_data_points)
        Agent.attach_supplementary_data(summarized_data_points)
        # After analyzing supplementary data; running it to be summarized; and then finally appending the final summary data to our prompt
        Redis = RedisConnector()
        with RedisConnector() as Redis:
            conversation_history = Redis.retrieve_conversation_history(conversation_id)
            ai_response = Agent.query_llm(conversation_history)
            print('AI Response: ' + ai_response)
            Redis.update_conversation_history(message_body, ai_response, conversation_id)

        with MySQLConnector() as MySQL:
            username = request_data['USERNAME']
            reference_id = MySQL.get_user_reference_id(username)
            MySQL.insert_new_conversation_turn(reference_id, conversation_id, username, message_body, ai_response, data_points, summarized_data_points, str_selected_keywords)
            
        return_data = {
            'AI_RESPONSE_MESSAGE': ai_response,
        }

        return return_data

    @staticmethod
    def view_conversation_handler(request_data):
        with MySQLConnector() as MySQL:
            conversation_id = request_data['CONVERSATION_ID']
            username = request_data['USERNAME']
            reference_id = MySQL.get_user_reference_id(username)
            
            conversation_data = MySQL.retrieve_conversation_history(conversation_id, reference_id)

        return conversation_data