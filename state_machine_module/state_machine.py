import state_machine_module.user_states as states
import state_machine_module.messages as messages

def reply(user_input, user_state):
    # Initial state
    if states.INITIAL_STATE == user_state:
        return states.INITIAL_STATE_PENDING_YES, messages.HELLO_MSG

    elif states.INITIAL_STATE_PENDING_YES == user_state:
        if user_input != messages.YES:
            return states.INITIAL_STATE_PENDING_YES, messages.INVALID_RESPONSE + messages.HELLO_MSG
        else:
            return states.SENTENCE_COMPLETEION_NOTEBOOK_PENDING_I_AM_BACK, messages.SENTENCE_COMPLETTION_NOTEBOOK_EXPLAINATION

    # Sentence completion - notebook
    elif states.SENTENCE_COMPLETEION_NOTEBOOK_PENDING_I_AM_BACK == user_state:
        if user_input != messages.I_AM_BACK:
            return states.SENTENCE_COMPLETEION_NOTEBOOK_PENDING_I_AM_BACK, messages.INVALID_RESPONSE
        else:
            return states.SENTENCE_COMPLETEION_DATA_PENDING_I_AM_BACK, messages.SENTENCE_COMPLETTION_DATA_EXPLAINATION

    elif states.SENTENCE_COMPLETEION_DATA_PENDING_I_AM_BACK == user_state:
        if user_input != messages.I_AM_BACK:
            return states.SENTENCE_COMPLETEION_DATA_PENDING_I_AM_BACK, messages.INVALID_RESPONSE
        else:
            return "dummy", "dummy"