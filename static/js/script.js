function updateChat(user, server) {
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML += `<p><strong>את/ה:</strong> ${user}</p>`;
    chatHistoryDiv.innerHTML += `<p>${server} <strong>:Snowflake</strong></p>`;
}

// Load chat history from localStorage
function loadChatHistory() {
    const history = JSON.parse(localStorage.getItem('chatHistory')) || [];
    history.forEach(chat => {
        updateChat(chat.user, chat.server);
    });
}

// Save chat to localStorage
function saveChat(user, server) {
    const history = JSON.parse(localStorage.getItem('chatHistory')) || [];
    history.push({user, server});
    localStorage.setItem('chatHistory', JSON.stringify(history));
}

// Handle form submission
document.getElementById('chatForm').onsubmit = async function(event) {
    event.preventDefault();
    const userInput = document.getElementById('messageInput').value;
    const userState = document.getElementById('userState').value;

    // Send the user input and userState to the Flask server
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: userInput,
            userState: userState,
        }),
    });

    if (response.ok) {
        const responseData = await response.json();
        const serverReply = responseData.serverReply;
        const newUserState = responseData.userState;

        updateChat(userInput, serverReply);
        saveChat(userInput, serverReply);

        // Update the hidden input with the new userState
        document.getElementById('userState').value = newUserState;

        document.getElementById('messageInput').value = ''; // Clear input field
    } else {
        alert(error.message);
    }
}

function clearChatHistory() {
    // Clear the display
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML = '';

    // Clear the localStorage
    localStorage.removeItem('chatHistory');
}

// Event listener for the Clear button
document.getElementById('clearBtn').onclick = function() {
    clearChatHistory();
};

// Load chat history when the page loads
window.onload = loadChatHistory;