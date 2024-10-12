import React, { useRef, useEffect, useState, useCallback } from 'react';
import ReactMarkdown from 'react-markdown';

const ChatBubble = ({ message, user_message, isNew, scrollToBottom }) => {
    const [displayedMessage, setDisplayedMessage] = useState('');
    const [completedTyping, setCompletedTyping] = useState(false);

    const TYPEWRITER_SPEED_MS = 10;

    useEffect(() => {
        if (!user_message && isNew) { //only apply typewriter effect for new AI messages
            setCompletedTyping(false);
            let i = 0;
            const intervalId = setInterval(() => {
                setDisplayedMessage(message.slice(0, i + 1));
                i++;
                scrollToBottom();
                if (i >= message.length) {
                    clearInterval(intervalId);
                    setCompletedTyping(true);
                }
            }, TYPEWRITER_SPEED_MS);

            return () => clearInterval(intervalId);
        } else {
            //immediately display the full message for loaded messages or user messages
            setDisplayedMessage(message);
        }
    }, [message, user_message, isNew]);

    return (
        <div className={`chat-bubble ${user_message ? 'sent' : 'received'}`}>
            {!user_message ? (
                <ReactMarkdown>{displayedMessage}</ReactMarkdown>
            ) : (
                displayedMessage
            )}
        </div>
    );
};

export const ChatBox = ({ messages = [], onSendMessage }) => {
    const chatHistoryRef = useRef(null);
    const [message, setMessage] = useState('');

    //scroll to the bottom of the chat history
    const scrollToBottom = useCallback(() => {
        if (chatHistoryRef.current) {
            chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
        }
    }, []);

    useEffect(() => {
        scrollToBottom();
    }, [messages, scrollToBottom]);

    const handleSendMessage = () => {
        if (message.trim()) {
            onSendMessage(message, true); //pass true indicating it's a new message
            setMessage('');
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSendMessage();
        }
    };

    return (
        <div className="chatbox-container">
            <div className="chat-history-container" ref={chatHistoryRef}>
                {messages.map((chat, index) => (
                    <ChatBubble key={index} message={chat.message} user_message={chat.user_message} isNew={chat.isNew} scrollToBottom={scrollToBottom} />
                ))}
            </div>
            <div className="new-message-container">
                <input
                    type="text"
                    placeholder="Type a message"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    onKeyPress={handleKeyPress}
                    className="input"
                />
                <button onClick={handleSendMessage} className="submit-button">
                    <span className="arrow">&#10148;</span>
                </button>
            </div>
        </div>
    );
};

export default ChatBox;
