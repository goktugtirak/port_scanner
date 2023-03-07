import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    if sys.argv[1] == "help":
        print("Syntax:\npython3 port_scanner.py <ip>\npython3 scanner.py <ip> <start_port> <end_port>")
    else:
        target=socket.gethostbyname(sys.argv[1]) #verilen hostun ip adresini getirir.
        start_port=1
        end_port=3000
elif len(sys.argv) == 4:
    target=socket.gethostbyname(sys.argv[1])
    start_port=int(sys.argv[2])
    end_port=int(sys.argv[3])
else:
    print("Invalid amount of arguments.")
    print("Syntax:\npython3 port_scanner.py <ip>\npython3 scanner.py <ip> <start_port> <end_port>")

print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(start_port,end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"{port} open")
        s.close()

except KeyboardInterrupt: #ctrl+c'ye basıldığında çalışır.
    print("\nExiting proram.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()