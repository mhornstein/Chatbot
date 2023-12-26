import pandas as pd
from state_machine_module.user_states import *

texts = pd.read_csv('./texts/texts.csv').set_index('id')

def reply(user_input, user_state):
    if INITIAL_STATE == user_state:
        return "1", texts.loc[1][0]
    else:
        return "2", texts
