import json
import os.path

class world:
    def __init__(self):
        self.size, self.agent_init, self.objective_init = self.__read_file('world.json')
        if self.__check_inclusion(self.objective_init, self.size) or self.__check_inclusion(self.agent_init, self.size):
            raise ValueError('world.json file is not correctly initilized: objective or agent cannot be on the world')
        self.action_map = {
            "up": self.__move_up,
            "down": self.__move_down,
            "right": self.__move_right,
            "left": self.__move_left
        }
        self.reset_world()
    
    # init
    def __read_file(self, file_name):
        """Read config file in json format and extract world information"""
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, file_name))
        with open(filepath) as json_file:
            data = json.load(json_file)
            size = {'x': data['size'][0], 'y': data['size'][1]}
            agent = {'x': data['agent'][0], 'y': data['agent'][1]}
            objective = {'x': data['objective'][0], 'y': data['objective'][1]}
            return (size, agent, objective)
                        
    def __check_inclusion(self, world_object, size):
        """Check if the objective and agent are in the world"""
        return world_object['x'] >= size['x'] or world_object['y'] >= size['y'] or world_object['x'] < 0 or world_object['y'] < 0
    
    # world 
    def __generate_world(self):
        """Update the world object, score and win condition"""
        world = [['.'] * self.size['x'] for y in range(self.size['y'])]
        world[self.agent['y']][self.agent['x']] = '@'
        world[self.objective['y']][self.objective['x']] = 'x'
        if self.__check_collision(self.agent, self.objective):
            self.win = True
            self.score += 100
        return world
    
    def reset_world(self):
        """Reset the world"""
        self.agent = self.agent_init.copy()
        self.objective = self.objective_init.copy()
        self.score = 0
        self.win = False
        self.world = self.__generate_world()

    # actions
    def get_actions(self):
        """Return all possibles actions"""
        return list(self.action_map)
    
    def perform(self, action):
        """Perform an action by action name"""
        if action in self.get_actions():
            self.action_map[action]()
            self.world = self.__generate_world()
        else:
            raise ValueError('action: ', action, ' is not part of possible actions')

    def __move_up(self):
        """Move the agent up"""
        if self.agent['y'] > 0:
            self.agent['y'] -= 1

    def __move_down(self):
        """Move the agent down"""
        if self.agent['y'] < (self.size['y'] - 1):
            self.agent['y'] += 1

    def __move_right(self):
        """Move the agent right"""
        if self.agent['x'] < (self.size['x'] - 1):
            self.agent['x'] += 1

    def __move_left(self):
        """Move the agent left"""
        if self.agent['x'] > 0:
            self.agent['x'] -= 1

    # state
    def __check_collision(self, object_a, object_b):
        """Check two object are in the same case"""
        return object_a['x'] == object_b['x'] and object_a['y'] == object_b['y']

    def get_state(self):
        """Return a tuple with the state (in string format) and a boolean in order to know if the game is over"""
        return ('@ ' + str(self.agent['x']) + ':' + str(self.agent['y']) + ' x ' + str(self.objective['x']) + ':' + str(self.objective['y']), self.win)
    
    def get_score(self):
        """Return the score"""
        return self.score

    # rendering
    def render(self):
        """Render the world"""
        # clear the terminal before rendering
        print(chr(27) + "[2J")
        for i in range(self.size['y']):
            line = self.world[i]
            print(self.__custom_join(line))
        print('STATE: ' + self.get_state()[0])

    def __custom_join(self, line):
        """Helper used in the rendering function"""
        line_str = ''
        for e in line:
            line_str += ' ' + e + ' '
        return line_str
    