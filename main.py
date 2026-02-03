from adbutils import adb
from client import Client
from runner import Runner

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
    user_input = ''
    input_message = f'Please select an emulator:\n'
    for index, emulator in enumerate(emulator_list):
        input_message += f'{index + 1}. {emulator}\n'    
    input_message += 'Your choice: '

    while user_input.lower() not in map(str, range(1, len(emulator_list) + 1)):
        user_input = input(input_message)
    # Create client instance
    emulator_serial = emulator_list[int(user_input) - 1]

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