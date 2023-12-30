const AGENT_STATE_COOKIE_NAME = 'agent_state';
const EVIL_AGENT_STATES = ['30', '31', '32'];
const ERROR_MESSAGE = 'זוהי שגיאה שאינה חלק מהתרגיל. פנו למדריך/ה לעזרה. פרטי השגיאה: ';

function updateChat(user, server, image) {
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML += `<p><strong>User:</strong> ${user}</p>`;

    if (image) {
        // Assuming image is a base64 encoded string
        chatHistoryDiv.innerHTML += `<p><strong>Server:</strong></p> <img src="data:image/jpeg;base64,${image}" alt="Agent Image"/>`;
    }
    
    let formattedServerText = server.replace(/\n/g, '<br>'); // replace new line with break
    chatHistoryDiv.innerHTML += `<p><strong>Server:</strong> ${formattedServerText}</p>`;
    chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight; // Scroll to the bottom of the chat history
}

function loadChatHistory() {
    const history = JSON.parse(localStorage.getItem('chatHistory')) || [];
    history.forEach(chat => {
        updateChat(chat.user, chat.server, chat.image);
    });
}

function saveChat(userInput, serverReply, image) {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];

    const chat = {
        user: userInput,
        server: serverReply,
        image: image // This is the base64 encoded image string
    };

    chatHistory.push(chat);

    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}

function getCookie(name) {
    let cookieArray = document.cookie.split(';');
    for(let i = 0; i < cookieArray.length; i++) {
        let cookiePair = cookieArray[i].split('=');
        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

function updatePageStyle() {
    let agent_state = getCookie(AGENT_STATE_COOKIE_NAME);

    if (EVIL_AGENT_STATES.includes(agent_state)) { 
        document.getElementById('logo').src = '/static/images/logo_bad_snowflake.png';
        document.body.style.backgroundColor = '#f85e5b';
    } else {
        document.getElementById('logo').src = '/static/images/logo_good_snowflake.png';
        document.body.style.backgroundColor = '#f9f9f9';
    }
}

document.getElementById('chatForm').onsubmit = async function(event) {
    event.preventDefault();

    const userInput = document.getElementById('messageInput').value;
    let agentStrOutput = '', agentImageOutput = null; // default value for image is null

    const payload = {
        user_input: userInput
    };

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (response.ok) {
            const responseData = await response.json();

            agentStrOutput = responseData.agent_str_output;
            agentImageOutput = responseData.agent_image_output; // This might be a URL or base64 string
        } else {
            const error = await response.text();
            agentStrOutput = ERROR_MESSAGE + error;
        }
    } catch (error) {
        agentStrOutput = ERROR_MESSAGE + error.message;
    } finally {
        updateChat(userInput, agentStrOutput, agentImageOutput);
        updatePageStyle();

         saveChat(userInput, agentStrOutput, agentImageOutput);

        document.getElementById('messageInput').value = ''; // Clear the input field for the next message
    }
}

document.getElementById('initBtn').onclick = function() {
    initChat();
};

function clearAllCookies() {
    document.cookie.split(";").forEach(function(c) {
        document.cookie = c.trim().split("=")[0] + "=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
    });
}

function initChat() {
    // Clear the display
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML = '';

    // Clear the history
    localStorage.removeItem('chatHistory');

    // Clear agent and user states, and any other session-related information
    clearAllCookies();
}

// Load chat history when the page loads
window.onload = loadChatHistory;