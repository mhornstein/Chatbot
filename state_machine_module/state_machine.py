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
            return states.SENTENCE_COMPLETEION_RESULTS_PENDING_ANSWER, messages.SENTENCE_COMPLETEION_RESULTS_INQUIRY

    elif states.SENTENCE_COMPLETEION_RESULTS_PENDING_ANSWER == user_state:
        return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.INTERESTING + messages.MAIN_MENU

    # main menu - only option 1 enabled
    elif states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE == user_state:
        if user_input == '1':
            return states.OPTION_1_PENDING_CHOISE, messages.OPTION_1_ENABLED
        elif user_input == '2':
            return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.OPTION_2_DISABLED + '\n' + messages.MAIN_MENU
        elif user_input == '3':
            return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.OPTION_3_DISABLED + '\n' + messages.MAIN_MENU
        else: # Invalid choise
            return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.INVALID_RESPONSE + messages.MAIN_MENU

    # main menu - option 1 - workers review
    elif states.OPTION_1_PENDING_CHOISE == user_state:
        if user_input == '1':
            return states.SENTIMENT_ANALYSIS_NOTEBOOK_PENDING_I_AM_BACK, messages.SENTIMENT_ANALYSIS_NOTEBOOK_EXPLAINATION
        elif user_input == '2':
            return "dummy", "dummy"
        else: # Invalid choise
            return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.INVALID_RESPONSE + messages.MAIN_MENU

    # sentiment analysis
    elif states.SENTIMENT_ANALYSIS_NOTEBOOK_PENDING_I_AM_BACK == user_state:
        if user_input != messages.I_AM_BACK:
            return states.SENTIMENT_ANALYSIS_NOTEBOOK_PENDING_I_AM_BACK, messages.INVALID_RESPONSE
        else:
            return states.SENTIMENT_ANALYSIS_NOTEBOOK_PENDING_I_AM_BACK, messages.SENTIMENT_ANALYSIS_NOTEBOOK_EXPLAINATION

    elif states.SENTIMENT_ANALYSIS_DATA_PENDING_I_AM_BACK == user_state:
        if user_input != messages.I_AM_BACK:
            return states.SENTIMENT_ANALYSIS_NOTEBOOK_PENDING_I_AM_BACK, messages.INVALID_RESPONSE
        else:
            return states.MAIN_MENU_OPTION_1_ENABLED_PENDING_CHOISE, messages.INTERESTING + messages.MAIN_MENU