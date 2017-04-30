Q LEARNING SAMPLE
=================
This repository provide a simple implementation of the q learning algorithm in Python.
It also provide a simple game that the AI will try to solve.

Requirement
-----------
Python 3.6+ 

Running the sample
------------------
Just run `python main.py` in order to run the sample.
The AI will learn from 100 games before starting exploiting what it learned.
There is a small timer in the exploit phase in order to be able see the AI (too fast for human otherwise).

Usage
-----

### Create a world
Import the module universe and use it:
```
import universe
env = universe.create()
```
Get all possible action:
```
action_list = env.get_actions()
```
Perform an action:
```
env.perform("right")
```
Get the state of the world: 
```
env.get_state()
```
Get the current score:
```
env.get_score
```
Render the world:
```
env.render()
```

### Create an ai
Just pass some parameter to the AI in order to create it. It needs the list of actions, the way of performing actions, the way of getting the state of the world, and the way of getting the score
```
firstai = ai.create(env.get_actions(), env.perform, env.get_state, env.get_score)
```
Now, each step can be performed in a While loop using the `perform_step` function:
```
for i in range(100):
    while not env.win:
        firstai.perform_step(train = True)
        env.render()
    env.reset_world()
```
The `perform_step` can be used in training mode or note. The difference is that in training mode (or explore mode), it will choose random actions but in exploit mode, it will choose what it consider to be the best possible action.
