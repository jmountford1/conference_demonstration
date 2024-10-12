export const fetchChatHistories = async () => {
    try {
        const response = await fetch('http://localhost:8000/api/initial-handshake', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                USERNAME: localStorage.getItem("username")
            }),
        });
        const data = await response.json();
        return data.map(conversation => ({
            id: conversation.CONVERSATION_ID,
            timestamp: conversation.TIMESTAMP
        }));
    } catch (error) {
        console.error('Error fetching chat histories:', error);
        throw error;
    }
};

export const fetchChatMessages = async (chatId) => {
    try {
        const response = await fetch('http://localhost:8000/api/view-conversation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                USERNAME: localStorage.getItem("username"),
                CONVERSATION_ID: chatId
            }),
        });
        const data = await response.json();
        const formattedMessages = [
            { message: "Welcome! How can I assist you today?", user_message: false }
        ];

        data.forEach((msg) => {
            if (msg.MESSAGE_BODY) {
                formattedMessages.push({
                    message: msg.MESSAGE_BODY,
                    user_message: true,
                });
            }
            if (msg.AI_RESPONSE) {
                formattedMessages.push({
                    message: msg.AI_RESPONSE,
                    user_message: false,
                });
            }
        });

        return formattedMessages;
    } catch (error) {
        console.error('Error fetching chat messages:', error);
        throw error;
    }
};

export const getChatResponse = async (message, selectedChatId, customerId) => {
    try {
        const response = await fetch('http://localhost:8000/api/send-chat-message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                USERNAME: localStorage.getItem("username"),
                USER_MESSAGE: message,
                CONVERSATION_ID: selectedChatId,
                TARGET_CUSTOMER_ID: customerId,
            })
        });
        const data = await response.json();
        return data['AI_RESPONSE_MESSAGE'];
    } catch (error) {
        console.error('Error getting chat response:', error);
        throw error;
    }
};

export const createNewConversationId = async () => {
    try {
        const response = await fetch('http://localhost:8000/api/create-new-chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                USERNAME: localStorage.getItem("username")
            })
        });
        const data = await response.json();
        return data['NEW_CONVERSATION_ID'];
    } catch (error) {
        console.error('Error generating new conversation:', error);
        throw error;
    }
};
