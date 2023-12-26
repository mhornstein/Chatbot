import state_machine_module.user_states as states
import state_machine_module.messages as messages

def reply(user_input, user_state):
    if states.INITIAL_STATE == user_state:
        return states.INITIAL_STATE_PENDING_YES, messages.HELLO_MSG
    elif states.INITIAL_STATE_PENDING_YES == user_state:
        if user_input != messages.YES:
            return states.INITIAL_STATE_PENDING_YES, messages.INVALID_RESPONSE + messages.HELLO_MSG
        else:
            return states.SENTENCE_COMPLETEION_PENDING_I_AM_BACK, messages.SENTENCE_COMPLETTION_NOTEBOOK_EXPLAINATION
    if states.SENTENCE_COMPLETEION_PENDING_I_AM_BACK == user_state:
        if user_input != messages.I_AM_BACK:
            return states.SENTENCE_COMPLETEION_PENDING_I_AM_BACK, messages.INVALID_RESPONSE
        else:
            return "dummy", "dummy"