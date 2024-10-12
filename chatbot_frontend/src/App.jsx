import React, { useEffect } from "react";
import ChatbotPage from './components/pages/ChatbotPage';
import '/src/styles/global.css';

function App() {

  useEffect(() => {
    const setUserId = () => {
      let username = localStorage.getItem("username");

      if (!username) {
        localStorage.setItem("username", "janedoe");
      }
      console.log("Username:", "janedoe");
    };

    setUserId();
  }, []);

  return (
    <div>
      <ChatbotPage />
    </div>
  )
}

export default App
