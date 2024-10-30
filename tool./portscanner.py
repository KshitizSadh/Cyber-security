import socket
import termcolor


def scan(target, ports):
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] port Opened"+str(port))
		sock.close()
	except:
		print("[-] Port Closed"+str(port))
targets = input("[*] Enter targets to scan(split them by ,):")
ports = int(input("[*] Enter How many  Ports you want to scan: "))
if ',' in targets:
	print("[*} scanning Multiple targets")
	for ip_addr in target.split(','):
		scan(ip_addr.strip(' '),  ports)
else:
	scan(targets,ports)
