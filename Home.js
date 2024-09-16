import React from 'react';
import { useNavigate } from 'react-router-dom';
import './home.css';

const HomePage = () => {
  const navigate = useNavigate();

  const handleChatClick = () => {
    navigate('/chat');
  };

  const handleFaqClick = () => {
    navigate('/faq');
  };

  const handleTranslatorClick = () => {
    navigate('/translator');
  };

  return (
    <div className="home-container">
      <div className="grid-container">
        <div className="box" onClick={handleChatClick}>
          <h3>Chat</h3>
        </div>
        <div className="box"></div>
        <div className="box"></div>
        <div className="box" onClick={handleTranslatorClick}>
          <img src="path/to/google-translator-icon.png" alt="Translator" />
        </div>
        <div className="box" onClick={handleFaqClick}>
          <h3>FAQs</h3>
        </div>
        <div className="box"></div>
      </div>
    </div>
  );
};

export default HomePage;