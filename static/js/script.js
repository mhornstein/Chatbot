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

document.getElementById('chatForm').onsubmit = async function(event) {
    event.preventDefault();

    const userInput = document.getElementById('messageInput').value;

    const payload = {
        user_input: userInput
    };

    // Make the POST request to the server
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    });

    if (response.ok) {
        const responseData = await response.json();

        const agentStrOutput = responseData.agent_str_output;
        const agentImageOutput = responseData.agent_image_output; // This might be a URL or base64 string

        updateChat(userInput, agentStrOutput, agentImageOutput);
        saveChat(userInput, agentStrOutput, agentImageOutput);

        document.getElementById('messageInput').value = ''; // Clear the input field for the next message
    } else {
        // Handle errors
        const error = await response.text();
        alert(`Error: ${error}`);
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