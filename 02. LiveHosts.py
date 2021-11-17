import socket
import nmap
import time

start_time = time.time()

ip_addr = input('Enter the network address: ')
host = socket.gethostbyname(ip_addr)
start = int(input("Enter the starting Number: "))
end = int(input("Enter the last Number: "))
scanner = nmap.PortScanner()
print("\n*** Scanning... ***\n")
for num in range(start, end+1):
    ip = host[0:-1] + str(num)
    scanner.scan(ip, '1', '-v')
    if scanner[ip].state() == "up":
        print(ip, "--> Live")

print("Scanning done after", time.time() - start_time, "s")

