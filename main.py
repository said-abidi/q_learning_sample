import universe
import time
import ai

env = universe.create()
firstai = ai.create(env.get_actions(), env.perform, env.get_state, env.get_score)

# learning phase
for i in range(100):
    while not env.win:
        firstai.perform_step(train = True)
        env.render()
    env.reset_world()

for i in range(5):
    while not env.win:
        firstai.perform_step(train = False)
        env.render()
        time.sleep(0.2)
    env.reset_world()

print('Success')
