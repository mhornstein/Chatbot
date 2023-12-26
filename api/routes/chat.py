from flask import Blueprint, render_template, request, jsonify
import state_machine_module.state_machine as state_machine

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates')

@chat_bp.route('/')
def home():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    user_state = request.json['userState']  # Retrieve the user state from the JSON request

    # Logic to determine the server's reply based on user input and state
    new_state, server_reply = state_machine.reply(user_input, user_state)

    # Include the updated state in the response
    response_data = {
        'serverReply': server_reply,
        'userState': new_state,
    }

    # Render the JSON response
    return jsonify(response_data)
