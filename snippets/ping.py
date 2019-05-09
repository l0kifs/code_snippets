import os


def ping(hostname):
    response = os.system("ping " + hostname)
    print(response)
    if response == 0:
        return True
    else:
        return False
