# Legend Clover Abyssal Labyrinth Runner
Bot to automate running abyssal labyrinth to floor 10 then repeating.

## Setup
- [Python](https://www.python.org/downloads/) 3.14 (ADD TO PATH)
- Any Android emulator
- 1920x1080 resolution
- ADB Debugging Enabled
- Run `setup.bat` to create virtual environment and install dependencies

## How to use
1. Open Abyssal Labyrinth screen.
2. Run the script with `run.bat`.
3. Close the window or press `CTRL+C` to stop the run.

## Optional Settings
- You may change the times taken to beat fights in `config.txt`
  - `delay` is the time delay in seconds between button presses.
  - `normal_fight` is the time taken in seconds to clear a regular floor.
  - `lv5_fight` is the time taken in seconds to clear floor 5.
  - `lv10_fight` is the time taken in seconds to clear floor 10.
  - `timeout` is the time taken in seconds until the image recognition timesout and stops running.