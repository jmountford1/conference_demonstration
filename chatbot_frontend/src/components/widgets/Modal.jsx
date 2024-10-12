import React, { useState, useEffect } from 'react';

const Modal = ({ onSaveCustomerId, isNewChat }) => {
    const [selectedCustomerId, setSelectedCustomerId] = useState('');
    const [isModalVisible, setIsModalVisible] = useState(true);

    const handleCustomerIdChange = (e) => {
        setSelectedCustomerId(e.target.value);
    };

    const handleEnterClick = () => {
        if (selectedCustomerId) {
            onSaveCustomerId(selectedCustomerId);  //save customer ID to parent state
            setIsModalVisible(false);  //close the modal
        }
    };

    useEffect(() => {
        //show modal when a new chat is created
        if (isNewChat) {
            setIsModalVisible(true);
        }
    }, [isNewChat]);  //modal visibility controlled by isNewChat

    if (!isModalVisible) return null;

    const username = localStorage.getItem("username");

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <h2>Welcome, {username}!</h2>
                <p>Please select a customer ID from the list below to get started.<br/><br/>Once you've selected an ID, feel free to ask questions about your selected customer.</p>
                <select value={selectedCustomerId} onChange={handleCustomerIdChange}>
                    <option value="" selected disabled hidden>Select ID</option>
                    <option value="1">John Doe</option>
                    <option value="2">Emily Smith</option>
                    <option value="3">Michael Brown</option>
                    <option value="4">Sarah Johnson</option>
                    <option value="5">David Wilson</option>
                </select>
                <button onClick={handleEnterClick}>Enter</button>
            </div>
        </div>
    );
};

export default Modal;
