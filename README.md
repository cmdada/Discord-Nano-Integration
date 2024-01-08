## Discord-Nano-Integration

Discord-Nano-Integration is a (the) solution for integrating GNU Nano with Discord on Linux cause its a full blown ide :3.

## Usage Instructions
1. Start the systemd service:
   - Place the script in `~/code/Discord-Nano-Integration/discordnano.py`
   - Move the systemd service file to `~/.config/systemd/user/discordnano.service`
   - Run: `systemctl --user enable discordnano.service --now`

2. default:
   - The integration is configured to use Micro by default cause if you're really using this you probably want the features of micro.

3. using nano:
   - to use nano instead of micro go to line 17 in the script and change micro to nano.
