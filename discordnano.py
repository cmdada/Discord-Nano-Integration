import os
import time
from pypresence import Presence
import psutil

def setup_rich_presence(client_id):
    RPC = Presence(client_id)
    RPC.connect()

    return RPC

def update_rich_presence(RPC):
    start_time = time.time()
    last_filename = None
    last_state = "Not using nano"
    while True:
        nano_process = [p.info for p in psutil.process_iter(['name', 'cmdline']) if 'nano' in p.info['name']]
        if nano_process:  # Check if nano is running
            cmdline = nano_process[0].get('cmdline', [])
            current_state = 'Idle in nano'
            current_filename = ''
            if len(cmdline) > 1:  # If there is a file name.
                file_path = cmdline[1]  # Second element should be the file path.
                current_filename = os.path.basename(file_path)  # Get the base name as the file name.
                current_state = 'Editing a file'
                
            if current_filename != last_filename or current_state != last_state:
                start_time = time.time()
                last_filename = current_filename
                last_state = current_state

            RPC.update(details=current_state, state=current_filename, large_image="logosvg", start=start_time)
        else:
            if last_state != "Not using nano":  # Check if the state has changed
                start_time = time.time()
            last_state = "Not using nano"
            RPC.update(details='Not using nano', state='', large_image="logosvg", start=start_time)
      
        time.sleep(.1)

if __name__ == '__main__':
    client_id = '1174605779513389096'
    RPC = setup_rich_presence(client_id)
    update_rich_presence(RPC)
