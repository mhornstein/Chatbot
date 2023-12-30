from state_machine.constants import *
from state_machine.agentMessages import messages as agentMessages

def do_move(agent_state, user_state, session_cache, user_input):
    """
    Executes a move in the bot's state machine, i.e. for the snowflake agent.

    Parameters:
    - agent_state (int): The current state of the agent.
    - user_state (int): The current state of the user.
    - session_cache (dict): A small key-value cache storing information by the state machine for its future use. information stored as strings.
    - user_input (str): The input string from the user.

    Returns:
    Tuple containing:
    - updated_agent_state (int): The new state of the agent after the move.
    - updated_user_state (int): The new state of the user after the move.
    - agent_str_output (str): The textual output from the agent.
    - agent_image_output (Optional[str]): The encoded image output from the agent. This is optional and will be None if no image is required.

    This function processes the given inputs to transition both the agent and the user to their next respective states and produces the agent's textual and, optionally, image output.
    It also updates the session_cache in-place as needed by adding or removing keys.
    The image output is encoded and should be decoded for display or further processing.
    """
    if agent_state == 0:
        return 1, 0, agentMessages[1], None
    
    elif agent_state == 1:
        session_cache[NAME] = user_input
        return 2, 0, agentMessages[2], None
    
    elif agent_state == 2:
        if user_input != I_AM_BACK:
            return 2, 0, INVALID_INPUT, None
        else:
            return 3, 0, agentMessages[3], None
        
    elif agent_state == 3:
        if user_input != I_AM_BACK:
            return 3, 0, INVALID_INPUT, None
        else:
            return 4, 1, agentMessages[4], None
        
    elif agent_state == 4:
        return 5, 1, agentMessages[5], None

    elif agent_state == 5:
        if user_input == '1':
            return 6, user_state, agentMessages[6], None
        elif user_input == '2':
            if user_state in [0, 1, 2, 4]: # User didn't complete required preliminaries stages
                return 5, user_state, agentMessages[11] + DELIM + agentMessages[5], None
            elif user_state >= 6: # User had already completed this stage
                return 14, user_state, agentMessages[14], None
            else:
                return 12, user_state, agentMessages[12], None
        elif user_input == '3':
            if user_state < 6:  # User didn't complete required preliminaries stages
                return 5, user_state, agentMessages[16] + DELIM + agentMessages[5], None
            elif user_state == 6:
                return 17, user_state, agentMessages[17], None 
            else: # the user has already mentioned 2 suspects successfully
                return 19, user_state, agentMessages[19], None 
        else:
            return 5, user_state, INVALID_INPUT, None
        
    elif agent_state == 6:
        if user_input == '1':
            return 7, user_state, agentMessages[7], None
        elif user_input == '2':
            return 9, user_state, agentMessages[9], None
        elif user_input == '3':
            return 5, user_state, agentMessages[5], None
        else:
            return 6, user_state, INVALID_INPUT, None
        
    elif agent_state == 7:
        if user_input != I_AM_BACK:
            return 7, user_state, INVALID_INPUT, None
        else:
            return 8, user_state, agentMessages[8], None

    elif agent_state == 8:
        if user_input != I_AM_BACK:
            return 8, user_state, INVALID_INPUT, None
        else:
            if user_state == 1:
                user_state = 2
            elif user_state == 4:
                user_state = 5
            else:
                pass # In any other case - leave user state as it is
            
            return 6, user_state, agentMessages[6], None

    elif agent_state == 9:
        if user_input != I_AM_BACK:
            return 9, user_state, INVALID_INPUT, None
        else:
            return 10, user_state, agentMessages[10], None
    
    elif agent_state == 10:
        if user_input != I_AM_BACK:
            return 10, user_state, INVALID_INPUT, None
        else:
            if user_state == 1:
                user_state = 4
            elif user_state == 2:
                user_state = 3
            else:
                pass # In any other case - leave user state as it is
            
            return 6, user_state, agentMessages[6], None

    elif agent_state == 12:
        if user_input == 'success': # TODO change with required check
            return 14, user_state, agentMessages[14], None
        else:
            return 5, user_state, agentMessages[13] + DELIM + agentMessages[5], None
    
    elif agent_state == 14:
        if user_input != I_AM_BACK:
            return 14, user_state, INVALID_INPUT, None
        else:
            return 15, user_state, agentMessages[15], None
    
    elif agent_state == 15:
        if user_input != I_AM_BACK:
            return 15, user_state, INVALID_INPUT, None
        else:
            if user_state < 6: # If this is the first time the user finishes this part
                user_state = 6
            return 5, user_state, agentMessages[5], None

    elif agent_state == 17:
        if user_input == 'success': # TODO change with required check
            return 19, user_state, agentMessages[19], None
        else:
            return 5, user_state, agentMessages[18] + DELIM + agentMessages[5], None
    
    elif agent_state == 19:
        if user_input != I_AM_BACK:
            return 19, user_state, INVALID_INPUT, None
        else:
            return 20, 7, agentMessages[20], None

    elif agent_state == 20:
        if user_input == '1':
            return 20, user_state, agentMessages[21] + DELIM + agentMessages[20], None
        elif user_input == '2':
            return 22, user_state, agentMessages[22], None
        elif user_input == '3':
            return 28, user_state, agentMessages[28], None
        elif user_input == '4':
            return 5, user_state, agentMessages[5], None
        else:
            return 20, user_state, INVALID_INPUT, None
    
    elif agent_state == 22:
        if user_input == '1' or user_input == '2' or user_input == '3': # TODO change with required check
            requested_camera = user_input
            if was_camera_unlocked(requested_camera, session_cache):
                return 20, user_state, agentMessages[27] + DELIM + agentMessages[20], None
            else:
                session_cache[REQUESTED_CAMERA] = requested_camera
                return 24, user_state, agentMessages[24], None
        else:
            return 23, user_state, agentMessages[23], None
        
    elif agent_state == 23:
        if user_input == YES:
            return 22, user_state, agentMessages[22], None
        elif user_input == NO:
            return 20, user_state, agentMessages[20], None
        else:
            return 23, user_state, INVALID_INPUT, None

    elif agent_state == 24 or agent_state == 25:
        if user_input == 'success': # TODO change with required check
            unlocked_camera = session_cache[REQUESTED_CAMERA]
            update_cache_with_unlocked_camera(session_cache, unlocked_camera)
            del session_cache[REQUESTED_CAMERA] # remove camera id as it is no longer required
            return 20, user_state, agentMessages[27] + DELIM + agentMessages[20], None
        else:
            return 26, user_state, agentMessages[26], None
        
    elif agent_state == 26:
        if user_input == '1':
            return 25, user_state, agentMessages[25], None
        elif user_input == '2':
            del session_cache[REQUESTED_CAMERA] # remove camera id as it is no longer required
            return 20, user_state, agentMessages[20], None
        else:
            return 26, user_state, INVALID_INPUT, None

    elif agent_state == 28:
        if user_input == 'success': # TODO change with required check
            session_cache.pop(UNLOCKED_CAMERAS, None) # remove cameras info as this is no longer required for next states
            return 30, 8, agentMessages[30], None 
        else:
            return 20, user_state, agentMessages[29] + DELIM + agentMessages[20], None
    
    elif agent_state == 30:
        if user_input != I_AM_BACK:
            return 30, user_state, INVALID_INPUT, None
        else:
            return 31, user_state, agentMessages[31], None
        
    elif agent_state == 31 or agent_state == 32:
        if user_input == 'success': # TODO change with required check
            return 34, 9, agentMessages[33] + DELIM + agentMessages[34], None
        else:
            return 32, user_state, agentMessages[32], None

    elif agent_state == 34:
        if user_input == '1':
            return 35, user_state, agentMessages[35], None
        elif user_input == '2':
            return 38, user_state, agentMessages[38], None
        elif user_input == '3':
            return 41, user_state, agentMessages[41], None
        elif user_input == '4':
            return 45, user_state, agentMessages[45], None
        else:
            return 34, user_state, INVALID_INPUT, None

    elif agent_state == 35:
        if user_input != I_AM_BACK:
            return 35, user_state, INVALID_INPUT, None
        else:
            return 36, user_state, agentMessages[36], None

    elif agent_state == 36:
        return 34, user_state, agentMessages[37] + DELIM + agentMessages[34], None
    
    elif agent_state == 38:
        if user_input != I_AM_BACK:
            return 38, user_state, INVALID_INPUT, None
        else:
            return 39, user_state, agentMessages[39], None

    elif agent_state == 39:
        return 34, user_state, agentMessages[40] + DELIM + agentMessages[34], None
    
    elif agent_state == 41 or agent_state == 44:
        return 42, user_state, agentMessages[42], None # TODO create image according to prompt
    
    elif agent_state == 42:
        if user_input == YES:
            return 44, user_state, agentMessages[44], None
        elif user_input == NO:
            return 34, user_state, agentMessages[43] + DELIM + agentMessages[34], None
        else:
            return 42, user_state, INVALID_INPUT, None

    elif agent_state == 45:
        if user_input == YES:
            return 0, 0, agentMessages[46], None
        elif user_input == NO:
            return 34, user_state, agentMessages[34], None
        else:
            return 45, user_state, INVALID_INPUT, None 

    else:
        return 0, 0, INVALID_STATE, None
    
def was_camera_unlocked(camera, session_cache):
    if UNLOCKED_CAMERAS not in session_cache:
        return False
    else:
        cameras_list = session_cache[UNLOCKED_CAMERAS].split(COMMA_DELIM)
        return camera in cameras_list

def update_cache_with_unlocked_camera(session_cache, unlocked_camera):
    if UNLOCKED_CAMERAS not in session_cache:
        session_cache[UNLOCKED_CAMERAS] = unlocked_camera
    else:
        session_cache[UNLOCKED_CAMERAS] += COMMA_DELIM + unlocked_camera