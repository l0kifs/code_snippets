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

    fail_messages = ["Destination host unreachable", "Request timed out", "100% loss",
                     "Destination Host Unreachable", "100% packet loss"]

    for fail_message in fail_messages:
        if fail_message in output:
            print(host, "is Offline")
            return False

    print(host, "is Online")
    return True
