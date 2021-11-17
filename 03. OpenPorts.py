import socket
import nmap
import time

start_time = time.time()

ip_addr = input('Enter the remote host IP to scan: ')
host = socket.gethostbyname(ip_addr)
begin = int(input("Enter the start port number: "))
end = int(input("Enter the last port number: "))

scanner = nmap.PortScanner()
print("\n*** Searching for open ports... ***\n")
print("Open ports: ")
for num in range(begin, end+1):

    res = scanner.scan(host, str(num))

    status = res['scan'][host]['tcp'][num]['state']
    if status == 'open':
        print(num)

print("Scanning done after", time.time() - start_time, "s")