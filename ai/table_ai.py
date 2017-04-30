import random

class ai:
    def __init__(self, actions, perform, get_state, get_score, gamma):
        self.actions = actions
        self.perform = perform,
        self.get_state = get_state,
        self.get_score = get_score
        self.gamma = gamma
        self.q_table = {}
    
    def perform_step(self, train = True):
        """Main function used to perform an action and learn from it"""
        current_state = self.__check_and_get_state()
        if train:
            next_action = self.__explore()
        else:
            next_action = self.__exploit(current_state)
        self.perform[0](next_action)
        future_state = self.__check_and_get_state()
        self.__learn(current_state, next_action, future_state)
    
    def __learn(self, current_state, next_action, future_state):
        """Update the q_table thanks the previous state, the action, and the future state"""
        current_reward = self.get_score()
        self.q_table[current_state][next_action] = (current_reward + self.gamma * (self.__get_max_reward(future_state)))
    
    def __explore(self):
        """Take a random action"""
        return random.choice(self.actions)
    
    def __exploit(self, current_state):
        """Thanks to the q_table, take the most rewarding action"""
        actions = list(self.q_table[current_state])
        best_actions = actions
        best_reward = 0
        for action in actions:
            r = self.q_table[current_state][action]
            if r > best_reward:
                best_reward = r
                best_actions = [action]
            elif r == best_reward:
                best_actions.append(action)
        return random.choice(best_actions)

    def __get_max_reward(self, state):
        """Get the max_reward giving a state by using the q_table"""
        if state in list(self.q_table):
            max_reward = 0
            for action in self.actions:
                r = self.q_table[state][action]
                if r > max_reward:
                    max_reward = r
            return max_reward
        else:
            raise ValueError('error: state ' + state + ' is not present in q_table')

    def __check_and_get_state(self):
        """Get the state and insert it on the q_table if not existing"""
        current_state = self.get_state[0]()[0]
        # init state in q_table
        if current_state not in list(self.q_table):
            self.q_table[current_state] = {}
            for action in self.actions:
                self.q_table[current_state][action] = 0
        return current_state
    
    def get_display_q_table():
        """Just a conveniant way of displaying the q_table. Used for debugging purpose"""
        q_table_str = ''
        q_table_keys = list(self.q_table)
        for q_table_key in q_table_keys:
            q_table_str += '   ' + q_table_key + '\n'
            actions_key = list(self.q_table[q_table_key])
            for action_key in actions_key:
                q_table_str += action_key + ' : ' + \
                    str(self.q_table[q_table_key][action_key]) + '\n'
        q_table_str += '\n'
        return q_table_str
        