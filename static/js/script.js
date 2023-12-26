// Function to update chat on the screen
function updateChat(user, server) {
    const chatHistoryDiv = document.getElementById('chat-history');
    chatHistoryDiv.innerHTML += `<p><strong>You:</strong> ${user}</p>`;
    chatHistoryDiv.innerHTML += `<p><strong>Server:</strong> ${server}</p>`;
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
document.getElementById('chatForm').onsubmit = function(event) {
    event.preventDefault();
    const userInput = document.getElementById('messageInput').value;
    const serverReply = userInput.toLowerCase() === 'boris' ? 'Hi' : 'Bye';

    updateChat(userInput, serverReply);
    saveChat(userInput, serverReply);

    document.getElementById('messageInput').value = ''; // Clear input field
}

// Load chat history when the page loads
window.onload = loadChatHistory;