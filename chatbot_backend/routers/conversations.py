from fastapi import APIRouter, HTTPException, Request
from classes.Processor import Processor

router = APIRouter()

@router.get("/hello")
def return_hello():
    return "Hello"

@router.post("/api/initial-handshake")
async def initial_handshake(request: Request):
    request_data = await request.json()
    print(request_data)

    RequestHandler = Processor()
    conversation_pointers = RequestHandler.initial_connection_handshake(request_data)
    
    return conversation_pointers

@router.post("/api/view-conversation")
async def view_conversation(request: Request):
    request_data = await request.json()
    print(request_data)

    RequestHandler = Processor()
    conversation_data = RequestHandler.view_conversation_handler(request_data)

    print('Conversation data: ' + str(conversation_data))
    return conversation_data

@router.post("/api/send-chat-message")
async def continue_conversation(request: Request):
    request_data = await request.json()
    print(request_data)

    RequestHandler = Processor()
    response = RequestHandler.continue_conversation_handler(request_data)
    
    return response

@router.post("/api/create-new-chat")
async def new_conversation(request: Request):
    request_data = await request.json()
    print(request_data)

    RequestHandler = Processor()
    response = RequestHandler.new_conversation_handler(request_data)

    return response