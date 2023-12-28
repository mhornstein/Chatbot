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

    elif agent_state == 5:
        if user_input == '1':
            return user_name, 6, user_state, agentMessages[6], None
        elif user_input == '2':
            if user_state in [0, 1, 2, 4]:
                return user_name, 5, user_state, agentMessages[11] + DELIM + agentMessages[5], None
            else:
                return user_name, 12, user_state, agentMessages[12], None
        else: # TODO support also option 3 + invalid option
            return user_name, 5, user_state, INVALID_INPUT, None
        
    elif agent_state == 6:
        if user_input == '1':
            return user_name, 7, user_state, agentMessages[7], None
        elif user_input == '2':
            return user_name, 9, user_state, agentMessages[9], None
        elif user_input == '3':
            return user_name, 5, user_state, agentMessages[5], None
        else:
            return user_name, 6, user_state, INVALID_INPUT, None
        
    elif agent_state == 7:
        if user_input != I_AM_BACK:
            return user_name, 7, user_state, INVALID_INPUT, None
        else:
            return user_name, 8, user_state, agentMessages[8], None

    elif agent_state == 8:
        if user_input != I_AM_BACK:
            return user_name, 8, user_state, INVALID_INPUT, None
        else:
            if user_state == 1:
                user_state = 2
            elif user_state == 4:
                user_state = 5
            else:
                pass # In any other case - leave user state as it is
            
            return user_name, 6, user_state, agentMessages[6], None

    elif agent_state == 9:
        if user_input != I_AM_BACK:
            return user_name, 9, user_state, INVALID_INPUT, None
        else:
            return user_name, 10, user_state, INVALID_INPUT, None
    
    elif agent_state == 10:
        if user_input != I_AM_BACK:
            return user_name, 10, user_state, INVALID_INPUT, None
        else:
            if user_state == 1:
                user_state = 4
            elif user_state == 2:
                user_state = 3
            else:
                pass # In any other case - leave user state as it is
            
            return user_name, 6, user_state, agentMessages[6], None

    elif agent_state == 12:
        if user_input == 'success': # TODO change with required check
            return user_name, 14, user_state, agentMessages[14], None
        else:
            return user_name, 5, user_state, agentMessages[13] + DELIM + agentMessages[5], None
    
    elif agent_state == 14:
        if user_input != I_AM_BACK:
            return user_name, 14, user_state, INVALID_INPUT, None
        else:
            return user_name, 15, user_state, agentMessages[15], None
    
    elif agent_state == 15:
        if user_input != I_AM_BACK:
            return user_name, 15, user_state, INVALID_INPUT, None
        else:
            return user_name, 5, 6, agentMessages[5], None

    else:
        return user_name, 100, 100, 'Invalid state', None