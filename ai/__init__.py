import ai.table_ai

def create(actions, perform, get_state, get_score, gamma = 0.9):
    return ai.table_ai.ai(actions, perform, get_state, get_score, gamma)
    