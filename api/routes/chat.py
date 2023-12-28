from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates')

@chat_bp.route('/')
def home():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_name = data.get('user_name')
    user_input = data.get('user_input')
    agent_state = data.get('agent_state')
    user_state = data.get('user_state')

    # Process data here and generate responses
    updated_agent_state = 1  # some processing
    updated_user_state = 2  # some processing
    agent_str_output = "c"  # some processing
    agent_image_output = None  # some processing, convert to suitable format if necessary
    user_name = 'some name'

    # Construct response
    response = {
        'updated_agent_state': updated_agent_state,
        'updated_user_state': updated_user_state,
        'agent_str_output': agent_str_output,
        'agent_image_output': agent_image_output,
        'user_name': user_name
    }

    return jsonify(response)