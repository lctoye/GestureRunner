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
Gameplay is very straightforward. Your character endlessly runs towards the right while trying to avoid both flying and grounded enemies. The longer you can survive without colliding with an enemy, the higher your score.

## Controls
### ✊ RUN
### 🖐️ JUMP
In Gesture Runner, your character is controlled with hand gestures. Currently, only **right hand** tracking is supported. Sorry lefties :(
- To stay running on the ground, keep your right hand in a closed fist.
- To jump, open your hand and splay your fingers.

Spacebar starts (or restarts) a run, and Q quits the game.
