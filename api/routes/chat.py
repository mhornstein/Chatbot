from flask import Blueprint, render_template, request, jsonify
import base64
import os
from state_machine.stateMachine import do_move

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates')

@chat_bp.route('/')
def home():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_name = data.get('user_name')
    agent_state = data.get('agent_state')
    user_state = data.get('user_state')
    user_input = data.get('user_input')

    # Process data here and generate responses
    '''
    updated_agent_state = 1  # some processing
    updated_user_state = 2  # some processing
    agent_str_output = "c"  # some processing
    user_name = 'some name'
    
    # Dummy example for image creation (the image may be None if no exists)
    image_path = os.path.join('static', 'images', 'logo_good_snowflake.png')
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    agent_image_output = encoded_string  # this is now a base64 string of the image
    '''
    
    user_name, updated_agent_state, updated_user_state, agent_str_output, agent_image_output = do_move(user_name, agent_state, user_state, user_input)

    response = {
        'updated_agent_state': updated_agent_state,
        'updated_user_state': updated_user_state,
        'agent_str_output': agent_str_output,
        'agent_image_output': agent_image_output,
        'user_name': user_name
    }

    return jsonify(response)