import mysql.connector
from datetime import datetime, date
from mysql.connector import Error
from config import MySQLConfig

class MySQLConnector:

    # Usage methods

    def __enter__(self):
        self.create_database_connection()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy_database_connection()

    # Connection methods

    def create_database_connection(self):
        try:
            self.conn = mysql.connector.connect(**MySQLConfig)
            if self.conn.is_connected():
                print("Connected to MySQL.")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def destroy_database_connection(self):
        if self.conn.is_connected():
            self.conn.close()

    # Conversation methods

    def get_user_reference_id(self, username):
        cursor = self.conn.cursor(dictionary=True)
        query = ("SELECT id from chatbot_users WHERE username = %(username)s")

        values = {
            "username": username,
        }

        cursor.execute(query, values)
        reference_id = cursor.fetchone()

        cursor.close()
        return reference_id['id']
    
    def insert_new_conversation_turn(self, reference_id, conversation_id, username, message_body, ai_response, data_points, summarized_data_points, keywords):
        query = "INSERT INTO chatbot_messages (reference_id, conversation_id,username, message_body, ai_response, data_points, summarized_data_points, keywords) VALUES (%(reference_id)s,%(conversation_id)s,%(username)s,%(message_body)s,%(ai_response)s,%(data_points)s,%(summarized_data_points)s,%(keywords)s)"

        values = {
            "reference_id": reference_id,
            "username": username,
            "message_body": message_body,
            "ai_response": ai_response,
            "data_points": str(data_points),
            "conversation_id": conversation_id,
            "summarized_data_points": summarized_data_points,
            "keywords": keywords,
        }

        cursor = self.conn.cursor()
        cursor.execute(query,values)
        self.conn.commit()
        cursor.close()

    def retrieve_conversation_pointers(self, reference_id):
        query = "SELECT ID, TIMESTAMP FROM chatbot_conversations WHERE reference_id = %(reference_id)s"

        #id IN (SELECT DISTINCT id from chatbot_messages WHERE id IS NOT NULL) and

        values = {
            "reference_id": reference_id
        }

        cursor = self.conn.cursor()
        cursor.execute(query, values)

        return_pointers = []
        for (CONVERSATION_ID, TIMESTAMP) in cursor:
            if isinstance(TIMESTAMP, (datetime, date)):
                TIMESTAMP = TIMESTAMP.isoformat()
            return_pointers.append({
                "CONVERSATION_ID": CONVERSATION_ID,
                "TIMESTAMP": TIMESTAMP
            })

        cursor.close()
        return return_pointers

    def create_new_conversation(self, reference_id):
        query = "INSERT INTO chatbot_conversations (reference_id) VALUES (%(reference_id)s)"

        values = {
            'reference_id': reference_id
        }

        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()

        query = "SELECT MAX(id) FROM chatbot_conversations WHERE reference_id = %(reference_id)s"

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, values)
        new_conversation_id = cursor.fetchone()
        print(new_conversation_id)
        
        cursor.close()
        return new_conversation_id['MAX(id)']

    def retrieve_conversation_history(self, conversation_id, reference_id):
        query = "SELECT ID, MESSAGE_BODY, AI_RESPONSE FROM chatbot_messages WHERE conversation_id = %(conversation_id)s AND reference_id = %(reference_id)s"
        fields = {
            'conversation_id': conversation_id,
            'reference_id': reference_id,
        }

        cursor = self.conn.cursor()
        cursor.execute(query, fields)

        return_data = []
        for (ID, MESSAGE_BODY, AI_RESPONSE) in cursor:
            return_data.append({
                'MESSAGE_ID': ID,
                'MESSAGE_BODY': MESSAGE_BODY,
                'AI_RESPONSE': AI_RESPONSE,
            })

        cursor.close()
        return return_data
    
    def retrieve_customer_history(self, customer_id):
        query = 'SELECT first_name, last_name, customer_since, last_purchase FROM sample.customer_data WHERE id = %(customer_id)s'
        fields = {
            'customer_id': customer_id
        }

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, fields)

        raw_data = cursor.fetchone()
        cursor.close()

        return raw_data

    def retrieve_customer_contact_info(self, customer_id):
        query = 'SELECT first_name, last_name, email, phone_number FROM sample.customer_data WHERE id = %(customer_id)s'
        fields = {
            'customer_id': customer_id
        }

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, fields)

        raw_data = cursor.fetchone()
        cursor.close()

        return raw_data

    def retrieve_customer_mailing_address(self, customer_id):
        query = 'SELECT first_name, last_name, address, city, state, zip_code FROM sample.customer_data WHERE id = %(customer_id)s'
        fields = {
            'customer_id': customer_id
        }

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, fields)

        raw_data = cursor.fetchone()
        cursor.close()

        return raw_data

