# write up for the 'ice' on try hack me 
> This room focuses on exploiting and testing penetration skills on machine based on various exploits,vulnerblities and skills.
> ## Recon
> firstly, i scanned through all the orts using nmap ` sudo nmap -sS -p- <ip-addess> `,and found various inteesting stuff
> ![1](https://github.com/user-attachments/assets/6e0520b2-76e9-40f5-8221-1b53ffbbce5c)
```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-21 07:48 EDT
Warning: 10.10.109.243 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.10.109.243
Host is up (0.16s latency).
Not shown: 65515 closed tcp ports (reset)
PORT      STATE    SERVICE       VERSION
135/tcp   open     msrpc         Microsoft Windows RPC
139/tcp   open     netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds  Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open     ms-wbt-server Microsoft Terminal Service
5357/tcp  open     http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
8000/tcp  open     http          Icecast streaming media server
14298/tcp filtered unknown
17467/tcp filtered unknown
20835/tcp filtered unknown
21195/tcp filtered unknown
39711/tcp filtered unknown
49152/tcp open     msrpc         Microsoft Windows RPC
49153/tcp open     msrpc         Microsoft Windows RPC
49154/tcp open     msrpc         Microsoft Windows RPC
49158/tcp open     msrpc         Microsoft Windows RPC
49159/tcp open     msrpc         Microsoft Windows RPC
49160/tcp open     msrpc         Microsoft Windows RPC
50601/tcp filtered unknown
55110/tcp filtered unknown
60455/tcp filtered unknown
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 612.13 seconds
```
by usiing -s
