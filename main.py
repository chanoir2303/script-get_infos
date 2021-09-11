import socket
import platform
import getpass
import getmac

mac_address = getmac.get_mac_address()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('google.com', 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = 'N/A'
    return ip
    print(ip)

print('*IP ADDRESS: ' + get_local_ip())
print('*MAC ADDRESS: ' + mac_address)
print('*PROCESSOR: ' + platform.machine())

os = platform.system()
if os == 'Darwin':
    os_name = 'MACOS '
    print('*OS: ' + os_name + platform.mac_ver()[0])
else:
    print(os + ' ' + platform.version())

print('*USER: ' + getpass.getuser())
