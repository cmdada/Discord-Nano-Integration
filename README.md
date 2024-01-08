## Discord-Nano-Integration

Discord-Nano-Integration is a simple solution for seamlessly integrating GNU Nano with Discord on Linux for a smoother user experience.

## Usage Instructions
1. Start the systemd service by following these steps:
   - Place the script in `~/code/Discord-Nano-Integration/discordnano.py`
   - Move the systemd service file to `~/.config/systemd/user/discordnano.service`
   - Run: `systemctl --user enable discordnano.service --now`

2. Default Configuration:
   - The integration is configured to use Micro by default for an optimal experience. Feel free to keep this configuration unless you realllllly want to use nano.

3. Customization:
   - to use nano instead of micro go to line 17 in the script and change micro to nano.
