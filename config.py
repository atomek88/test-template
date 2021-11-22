import os

TEMP_FOLDER = os.path.join(os.environ.get("ROBOT_ROOT", os.getcwd()), 'temp')
OUTPUT_FOLDER = os.path.join(os.environ.get("ROBOT_ROOT", os.getcwd()), 'output')

