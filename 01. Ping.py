import os

ip_addr = input("Please enter your IP/Domain: ")
os.system("ping " + ip_addr)
print("\n*** Scanning the url... ***\n")
os.system("nmap " + ip_addr)
