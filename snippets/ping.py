import platform
import subprocess


def is_online(host):
    os_name = platform.system()
    
    if os_name == 'Windows':
        ping_args = ['ping', '-n', '1', '-w', '500', host]
    else:
        ping_args = ['ping', '-c', '1', '-W', '500', host]

    output = subprocess.Popen(ping_args, stdout=subprocess.PIPE).communicate()[0]

    if output is None:
        raise Exception('Failed to ping host {}'.format(host))

    output = output.decode('utf-8')
    if "Destination host unreachable" in output:
        print(host, "is Offline")
        return False
    elif "Request timed out" in output:
        print(host, "is Offline")
        return False
    else:
        print(host, "is Online")
        return True
