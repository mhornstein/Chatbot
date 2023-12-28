from state_machine.constants import *
from state_machine.agentMessages import messages as agentMessages

def do_move(user_name, agent_state, user_state, user_input):
    """
    Executes a move in the bot's state machine, i.e. for the snowflake agent.

    Parameters:
    - user_name (str): The name of the user interacting with the agent.
    - agent_state (int): The current state of the agent.
    - user_state (int): The current state of the user.
    - user_input (str): The input string from the user.

    Returns:
    Tuple containing:
    - user_name (str): The name of the user.
    - updated_agent_state (int): The new state of the agent after the move.
    - updated_user_state (int): The new state of the user after the move.
    - agent_str_output (str): The textual output from the agent.
    - agent_image_output (Optional[str]): The encoded image output from the agent. This is optional and will be None if no image is required.

    The function processes the given inputs to transition the agent and the user to their next respective states and produces the agent's textual and optional image output.
    The image output is encoded and should be decoded for display or further processing.
    """
    if agent_state == 0:
        return UNKNOWN_USENAME, 1, 0, agentMessages[1], None
    
    elif agent_state == 1:
        return user_input, 2, 0, agentMessages[2], None
    
    elif agent_state == 2:
        if user_input != I_AM_BACK:
            return user_name, 2, 0, INVALID_INPUT, None
        else:
            return user_name, 3, 0, agentMessages[3], None
        
    elif agent_state == 3:
        if user_input != I_AM_BACK:
            return user_name, 3, 0, INVALID_INPUT, None
        else:
            return user_name, 4, 1, agentMessages[4], None
        
    elif agent_state == 4:
        return user_name, 5, 1, agentMessages[5], None

    else:
        return user_name, 100, 100, 'Invalid state', None