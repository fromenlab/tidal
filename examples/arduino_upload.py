import os
import subprocess

board = 'arduino:avr:mega'
sketch = 'protocol/blink'
port = 'COM3'

###
# Run commands
###

# Compile
# arduino-cli compile --fqbn arduino:avr:mega protocol/motor_complete

cmd_verify = ['arduino-cli', 'compile', '--fqbn', board, sketch]
# subprocess.run(cmd_verify)

# Upload
# arduino-cli upload -p COM3 --fqbn arduino:avr:mega protocol/motor_complete

cmd_upload = ['arduino-cli', 'upload', '-p', port, '--fqbn', board, sketch, '--verbose', '--verify']
# subprocess.run(cmd_upload)

###
# Logging
###

with subprocess.Popen(cmd_verify, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
    lines = proc.stdout.readlines()

    with open("arduino.log", "a", encoding="utf-8") as f:
        for line in lines:
            text = line.decode('ascii').rstrip("\n")
            f.writelines(text)

with subprocess.Popen(cmd_upload, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
    lines = proc.stdout.readlines()

    with open("arduino.log", "a", encoding="utf-8") as f:
        for line in lines:
            text = line.decode('ascii').rstrip("\n")
            f.writelines(text)