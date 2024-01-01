from flask import Blueprint, render_template, request, jsonify, make_response
from state_machine.stateMachine import do_move

AGENT_STATE = 'agent_state'
USER_STATE = 'user_state'

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates')

@chat_bp.route('/')
def home():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('user_input')

    agent_state = int(request.cookies.get(AGENT_STATE, 0)) # If no state avaiable - this is initial state: state 0
    user_state = int(request.cookies.get(USER_STATE, 0))

    cookies_dict = dict(request.cookies)
    cookies_dict.pop(AGENT_STATE, None)  # Removes AGENT_STATE and USER_STATE if it exists, does nothing otherwise
    cookies_dict.pop(USER_STATE, None)
    
    updated_agent_state, updated_user_state, agent_str_output, agent_image_output = do_move(agent_state, user_state, cookies_dict, user_input)

    response = make_response(jsonify({
        'agent_str_output': agent_str_output,
        'agent_image_output': agent_image_output,
    }))

    # Clear existing cookies by setting them to expire immediately
    for key in request.cookies:
        response.set_cookie(key, '', expires=0)

    # Set updated states in cookies
    response.set_cookie(AGENT_STATE, str(updated_agent_state))
    response.set_cookie(USER_STATE, str(updated_user_state))

    for key, value in cookies_dict.items():
        response.set_cookie(key, value)

    return response