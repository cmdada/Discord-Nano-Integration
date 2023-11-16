import os
import time
from pypresence import Presence
import psutil

def setup_rich_presence(client_id):
    RPC = Presence(client_id)
    RPC.connect()

    return RPC

def update_rich_presence(RPC):
    while True:
        nano_process = [p.info for p in psutil.process_iter(['name', 'cmdline']) if 'nano' in p.info['name']]
        if nano_process:  # Check if nano is running
            cmdline = nano_process[0].get('cmdline', [])
            if len(cmdline) > 1:  # If there is more than one argument, we should have a file name.
                file_path = cmdline[1]  # Second element should be the file path.
                filename = os.path.basename(file_path)  # Get the base name as the file name.
                RPC.update(details='Editing a file', state=filename)
            else:
                RPC.update(details='Idle in nano', state='')
        else:
            RPC.update(details='Not using nano', state='')

        time.sleep(.1)  # Discord only allows updates every 15 seconds.

if __name__ == '__main__':
    client_id = '1174605779513389096'
    RPC = setup_rich_presence(client_id)
    update_rich_presence(RPC)
