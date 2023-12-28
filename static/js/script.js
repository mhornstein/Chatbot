function initializeStates() {
    if (localStorage.getItem('userState') === null) {
        localStorage.setItem('userState', '0');
    }

    if (localStorage.getItem('agentState') === null) {
        localStorage.setItem('agentState', '0');
    }

    if (localStorage.getItem('userName') === null) {
        localStorage.setItem('userName', 'None');
    }
}

function updateChat(user, server, image) {
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML += `<p><strong>User:</strong> ${user}</p>`;
    let formattedServerText = server.replace(/\n/g, '<br>'); // replace new line with break
    chatHistoryDiv.innerHTML += `<p><strong>Server:</strong> ${formattedServerText}</p>`;
    if (image) {
        // Assuming image is a base64 encoded string
        chatHistoryDiv.innerHTML += `<img src="data:image/jpeg;base64,${image}" alt="Agent Image" style="max-width:100%;"/>`;
    }
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

    let userState = parseInt(localStorage.getItem('userState') || '0');
    let agentState = parseInt(localStorage.getItem('agentState') || '0');
    let userName = localStorage.getItem('userName') || 'None';

    // Construct the request payload with all required fields
    const payload = {
        user_name: userName,
        user_input: userInput,
        user_state: userState,
        agent_state: agentState
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

        const updatedAgentState = parseInt(responseData.updated_agent_state);
        const updatedUserState = parseInt(responseData.updated_user_state);
        const agentStrOutput = responseData.agent_str_output;
        const agentImageOutput = responseData.agent_image_output; // This might be a URL or base64 string
        const userName = responseData.user_name;

        updateChat(userInput, agentStrOutput, agentImageOutput);
        saveChat(userInput, agentStrOutput, agentImageOutput);

        localStorage.setItem('userState', updatedUserState);
        localStorage.setItem('agentState', updatedAgentState);
        localStorage.setItem('userName', userName);

        document.getElementById('messageInput').value = ''; // Clear the input field for the next message
    } else {
        // Handle errors
        const error = await response.text();
        alert(`Error: ${error}`);
    }
}

function initChat() {
    // Clear the display
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML = '';

    // Clear the localStorage
    localStorage.removeItem('chatHistory');

    localStorage.removeItem('userState');
    localStorage.removeItem('agentState');
    localStorage.removeItem('userName');
}

// Event listener for the Clear button
document.getElementById('initBtn').onclick = function() {
    initChat();
};

// Load chat history when the page loads
initializeStates();
window.onload = loadChatHistory;