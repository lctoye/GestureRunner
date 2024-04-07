![title](https://github.com/lctoye/GestureRunner/assets/111930021/47400c5b-c43b-4a68-af5f-a33f4411644b)

Gesture Runner is an endless runner game in Python which uses hand gestures to control the character.

## Requirements
- Python 3.11
- A webcam

## Instructions
- Clone or download the repo and cd into it, i.e. `cd GestureRunner`
- Run `python -m venv .venv` to create the virtual environment
    - On macOS/Linux use `python3 -m venv .venv`
- Run `.venv\Scripts\activate` to activate the virtual environment
    - On macOS/Linux use `source .venv/bin/activate`
- Run `pip install -r requirements.txt` to install requirements
- Run `python GestureRunner.py` to launch the game
    - The first window that will open is the hand gesture tracking; the second is the game itself
    - There is a hardcoded 10 second delay to let the webcam initialize; the actual time this takes is hardware-dependent
    - You may have to rearrange the windows to minimize overlapping
 
## How to Play
Gameplay is very straightforward. Your character endlessly runs towards the right while trying to avoid both flying and grounded enemies. The longer you can survive without colliding with an enemy, the higher your score. At the risk of stating the obvious, you must run underneath the flying enemies and jump over the grounded ones.

## Controls
### ✊ RUN
### 🖐️ JUMP
In Gesture Runner, your character is controlled with hand gestures. Currently, only **right hand** tracking is supported. Sorry lefties :(
- To stay running on the ground, keep your right hand in a closed fist position:
  ![image](https://github.com/lctoye/GestureRunner/assets/111930021/fe53704f-94a9-4288-9766-bd37a937c216)
- To jump, open your hand and splay out your fingers.
  ![image](https://github.com/lctoye/GestureRunner/assets/111930021/312465be-99e8-4188-b2e5-25c12601e28c)

While on the title screen, Spacebar starts a new run, and Q quits the game.
