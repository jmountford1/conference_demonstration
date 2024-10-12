import React, { useEffect, useState } from 'react';
import ChatBox from '../widgets/Chatbox';
import ChatHistory from '../widgets/ChatHistory';
import Modal from '../widgets/Modal';
import { fetchChatHistories, fetchChatMessages, getChatResponse, createNewConversationId } from '../functions/conversations';

const ChatbotPage = () => {
    const [showHistory, setShowHistory] = useState(false);
    const [chatMessages, setChatMessages] = useState([
        { message: "Welcome! How can I assist you today?", user_message: false, isNew: false }
    ]);
    const [chatHistories, setChatHistories] = useState([]);
    const [selectedChatId, setSelectedChatId] = useState(null);
    const [customerId, setCustomerId] = useState(null);
    const [isNewChat, setIsNewChat] = useState(false);

    const handleSaveCustomerId = (id) => {
        setCustomerId(id);
        setIsNewChat(false);
    };

    const loadChatHistories = async () => {
        try {
            const histories = await fetchChatHistories();
            setChatHistories(histories);
        } catch (error) {
            console.error('Error loading chat histories:', error);
        }
    };

    const loadChatMessages = async (chatId) => {
        try {
            const messages = await fetchChatMessages(chatId);
            // Mark all loaded messages as not new
            const loadedMessages = messages.map(msg => ({ ...msg, isNew: false }));
            setChatMessages(loadedMessages);
        } catch (error) {
            console.error('Error loading chat messages:', error);
        }
    };

    const handleSendMessage = async (userMessage) => {
        const newUserMessage = { message: userMessage, user_message: true, isNew: false };
        setChatMessages((prevMessages) => [...prevMessages, newUserMessage]);

        try {
            const chat_response = await getChatResponse(userMessage, selectedChatId, customerId);
            // Mark the AI response as a new message
            const aiResponseMessage = { message: chat_response, user_message: false, isNew: true };
            setChatMessages((prevMessages) => [...prevMessages, aiResponseMessage]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    const createNewChat = async () => {
        try {
            const newChatId = await createNewConversationId();
            setSelectedChatId(newChatId);
            setChatMessages([{ message: "Welcome! How can I assist you today?", user_message: false, isNew: false }]);
            setIsNewChat(true);
        } catch (error) {
            console.error('Error creating new chat:', error);
        }
    };

    useEffect(() => {
        createNewChat();
        loadChatHistories();
    }, []);

    const toggleChatHistory = () => {
        setShowHistory(!showHistory);
    };

    return (
        <div className="chatbox-page-container">
            <Modal isNewChat={isNewChat} onSaveCustomerId={handleSaveCustomerId} />
            <button onClick={createNewChat} className="clear-history-button">
                &#10000;
            </button>
            <ChatBox messages={chatMessages} onSendMessage={handleSendMessage} />
            <button className="hamburger-menu" onClick={toggleChatHistory}>
                ☰
            </button>
            <div className={`previous-conversations-container ${showHistory ? 'visible' : ''}`}>
                <ChatHistory 
                    chatHistories={chatHistories} 
                    onSelectChat={loadChatMessages} 
                />
            </div>
        </div>
    );
};

export default ChatbotPage;
