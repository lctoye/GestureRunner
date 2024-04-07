import subprocess
import time

python_interpreter_path = ".venv\\Scripts\\python.exe"

# Start gesture tracking and wait 10 seconds for it to start
subprocess.Popen([python_interpreter_path, "gesture.py"])
time.sleep(10)

# Run the game
subprocess.call([python_interpreter_path, "runner.py"])
