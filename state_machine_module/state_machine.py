import pandas as pd
import state_machine_module.user_states as states
import state_machine_module.messages as messages

def reply(user_input, user_state):
    if states.INITIAL_STATE == user_state:
        return states.INITIAL_STATE_PENDING_YES, messages.HELLO_MSG
    elif states.INITIAL_STATE_PENDING_YES and user_input != messages.YES:
        return states.INITIAL_STATE_PENDING_YES, messages.INVALID_RESPONSE + messages.HELLO_MSG
    else:
        return "dummy", "dummy"
