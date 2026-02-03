from adbutils import adb
from pick import pick
from client import Client
from runner import Runner
import configparser

KEY_CTRL_C = 3
KEY_ESCAPE = 27
QUIT_KEYS = (KEY_CTRL_C, KEY_ESCAPE, ord("q"))

connected_emulators = []
emulators = adb.device_list()
emulator_list = [emulator.serial for emulator in emulators if emulator.serial not in connected_emulators and emulator.serial is not None]
emulator_serial = ""

if not emulator_list:
    raise Exception("No emulators found.")
elif len(emulator_list) == 1: 
    emulator_serial = emulator_list[0]
else:
    title = 'Choose an emulator'
    options = emulator_list
    option, index = pick(
        options, title, indicator="=>", default_index=0, quit_keys=QUIT_KEYS
    )    
    # Create client instance
    emulator_serial = option

print(f"Connected to {emulator_serial}")
client = Client(emulator_serial)
runner = Runner(client)
run = 0
try:
    print("Starting runs. Press ctrl+c to stop.")
    while True:
        run += 1
        print(f"Run {run}")
        runner.start_run()
        for i in range(10):
            print(f"Floor: {i + 1}")
            runner.floor_loop(i + 1)
        runner.handle_floor_10()
        runner.reset_abyss()
except KeyboardInterrupt:
    print("Ending run.")
    print(f"Total runs: {run}")
    pass