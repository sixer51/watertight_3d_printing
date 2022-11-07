from printrun.printcore import printcore
from printrun import gcoder
import time

print_core = printcore('/dev/tty.usbmodem14201', 115200) # or p.printcore('COM3',115200) on Windows
gcode = [i.strip() for i in open('./gcodes/Square_6h51m.gcode')] # or pass in your own array of gcode lines instead of reading from a file
gcode = gcoder.LightGCode(gcode)

# startprint silently exits if not connected yet
while not print_core.online:
  time.sleep(0.1)

print_core.startprint(gcode) # this will start a print

command = input()
while command != 'quit':
  command = input()

print_core.disconnect()