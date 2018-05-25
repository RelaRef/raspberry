import subprocess
from time import sleep

import post_to_https


def do(bash_command):
    try:
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    except FileNotFoundError:
        return post_to_https.do("FileNotFoundError while executing bash command: " + bash_command)

    if output:
        return post_to_https.do(output)
    else:
        return post_to_https.do(error)


loop = True
while loop:
    try:
        result = do("sudo ifconfig")
    except:
        result = "some error"

    result = "result/" + str(result)

    print(result)

    if result.find("200"):
        break
    sleep(10)
