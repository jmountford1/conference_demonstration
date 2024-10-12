import React from 'react';

export const ChatHistory = ({ chatHistories, onSelectChat }) => {

    const handleClick = (id) => {
        onSelectChat(id); //fetch messages for the selected conversation ID
    };

    return (
        <div className="chat-history-list">
            {chatHistories.map((history) => (
                <div 
                    key={history.id} 
                    className="chat-history-item"
                    onClick={() => handleClick(history.id)}
                >
                    <span>Conversation #{history.id}</span>
                </div>
            ))}
        </div>
    );
};

export default ChatHistory;
