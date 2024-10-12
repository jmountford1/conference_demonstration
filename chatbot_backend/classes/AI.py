from openai import OpenAI
from config import OPENAI_KEY
client = OpenAI(api_key=OPENAI_KEY)

class AI:

    # Usage functions
    def __init__(self, 
                 temperature=0, 
                 context="You are an extremely helpful, polite, and intuitive virtual assistant helping to answer information about customer records. You are only to give correct, accurate, and precise information and suggestions based on the data that is provided to you about a customer. Do not provide any information outside of what is asked by the user. Be concise with your answers. If you do not have the information that the user is looking for, please state so. ", 
                 chat_model="gpt-4"
                ):
        
        self.chat_model = chat_model
        self.temperature = temperature
        self.context = context

    # Conversation functions

    def attach_prompt(self, prompt):
        self.prompt = prompt

    def attach_supplementary_data(self, data):
        self.prompt += (' | ' + data)

    def query_llm(self, conversation_history):
        chat_completion = client.chat.completions.create(
            model=self.chat_model,
            messages = conversation_history + [{"role": "user", "content": self.prompt}]
        )
        return chat_completion.choices[0].message.content
    
    def check_keywords(self, keywords = "CONTACT_INFO, MAILING_ADDRESS, CUSTOMER_HISTORY"):
        context = "Based on the following question, select the most relevant keywords from the comma-separated list provided. The keywords need to be closely related to, or likely corresponding with the user intent behind the question. Only respond with the selected keywords by themselves, capitalized, in a comma-separated string. Please respond with a minimum of 1 returned keyword, but you may reply with multiple keywords. If unsure, respond with all of the relevant keywords."

        chat_message = f"QUESTION: {self.prompt} | KEYWORDS: {keywords}"

        chat_completion = client.chat.completions.create(
            model= self.chat_model,
            messages = [
                {"role": "system", "content": context},
                {"role": "user", "content": chat_message}
            ]
        )

        return chat_completion.choices[0].message.content
    
    def analyze_customer_data(self, customer_data):
        combined_prompt = "You are a polite, eager, and intuitive virtual assistant. Please re-write the following raw data as best as you are able to, in regular sentences, with a polite and formal tone. Be certain the rewrite is as accurate as possible. Ensure that all data is included in the re-write." + customer_data

        chat_completion = client.chat.completions.create(
            model=self.chat_model,
            messages = [
                {"role": "system", "content": self.context},
                {"role": "user", "content": combined_prompt}
                ]
            )
        
        return chat_completion.choices[0].message.content
