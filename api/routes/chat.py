from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates')

@chat_bp.route('/')
def home():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    user_state = request.json['userState']  # Retrieve the user state from the JSON request

    # Logic to determine the server's reply based on user input and state
    if user_input.lower() == 'dummy' and user_state == 'initialState':
        server_reply = 'Hi'
        new_state = 'greeted'  # Update the state as needed
    else:
        server_reply = 'Bye'
        new_state = 'default'

    # Include the updated state in the response
    response_data = {
        'serverReply': server_reply,
        'userState': new_state,
    }

    # Render the JSON response
    return jsonify(response_data)
