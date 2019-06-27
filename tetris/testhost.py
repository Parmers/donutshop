import urllib.request
import socket
import re
import urllib

def get_local_ip():
    '''find your own IP but gets only local address'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    host = s.getsockname()
    s.close()
    return host


# ip = tuple(re.findall("\"ip\":\"([\d\.]+)\"", 
        # urllib.request.urlopen('https://api.ipify.org?format=json').read()) + [0])

ip = urllib.request.urlopen('https://api.ipify.org?format=json').read().decode('utf8')
ip = ip.split(':')[1]
ip = ip.split('"')[1]

# ip = tuple(ip)
# ip = str(ip.split('"'))

print (ip)
print (type(ip))


print (str(get_local_ip()))
print (type(get_local_ip()))
# https://api.ipify.org?format=json