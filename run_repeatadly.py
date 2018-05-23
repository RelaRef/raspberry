import subprocess

# bashCommand = "sudo ifconfig | python3.6 /home/pi/raspberry/stdin_to_https.py"
bashCommand = "pwd"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
