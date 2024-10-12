import redis
import pickle
from config import RedisConfig

class RedisConnector:

    # Usage methods

    def __enter__(self):
        self.create_redis_connection()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy_redis_connection()

    # Connection methods

    def create_redis_connection(self) -> None:
        """Creates a connection to a specified Redis instance."""
        try:
            self.conn = redis.Redis(**RedisConfig)
            print("Connected to Redis.")
        except redis.ConnectionError as e:
            print(f"Connection error while connecting to Redis: {e}")
        except redis.RedisError as e:
            print(f"Redis error: {e}")

    def destroy_redis_connection(self) -> None:
        """Destroys a connection to a specified Redis instance."""
        self.conn = None
        print("Redis connection closed.")

    # Conversation methods

    def start_conversation_history(self, system_context: str, conversation_id: int) -> None:
        """Starts a clean conversation history with system context."""
        conversation = [{"role": "system", "content": system_context}]
        self.conn.set(str(conversation_id), pickle.dumps(conversation))

    def retrieve_conversation_history(self, conversation_id) -> list:
        conversation_history = self.conn.get(str(conversation_id))
        return pickle.loads(conversation_history)
    
    def update_conversation_history(self, user_prompt: str, ai_response: str, conversation_id: int) -> None:
        new_messages = [
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": ai_response}
        ]
        conversation_history = self.retrieve_conversation_history(conversation_id)
        conversation_history.extend(new_messages)
        self.conn.set(str(conversation_id), pickle.dumps(conversation_history))



