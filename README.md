# 🚀 TryHackMe: Injectics — Write-Up  
**Room URL:** [https://tryhackme.com/room/injectics](https://tryhackme.com/room/injectics)  
**Author:** *Irregular*  
**Date:** *14-06-2025*

---
## 📝 Overview  

> *Injectics is a room focused on exploiting injection vulnerabilities such as SQL Injection, SSTi,ORM  and others. The room provides hands-on practice with identifying and exploiting these issues to gain RCE or system access.*
>
> ## 🛠️ Tools Used  

- `nmap`
-  `dirsearch`
- `Burp Suite`
- `curl`
- `Web browser`

---
##RECON FINDINGS

*Nmap*

```
nmap -A -T5 10.10.186.30
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-14 06:51 EDT
Nmap scan report for 10.10.186.30
Host is up (0.16s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b7:21:88:c8:15:5f:7c:7c:be:50:00:9f:27:7a:06:7e (RSA)
|   256 3c:bf:29:b6:80:25:58:74:eb:32:d8:fb:05:53:25:98 (ECDSA)
|_  256 34:f5:76:85:2d:5a:5e:0d:27:c4:cc:10:a5:b4:5d:ee (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Injectics Leaderboard
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 993/tcp)
HOP RTT       ADDRESS
1   26.70 ms  10.17.0.1
2   ... 4
5   148.69 ms 10.10.186.30

```
*Dirsearch*
```
dirsearch -u 10.10.186.30

 _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/Downloads/reports/_10.10.186.30/_25-06-14_06-53-40.txt

Target: http://10.10.186.30/

[06:53:40] Starting: 
[06:53:44] 301 -  309B  - /js  ->  http://10.10.186.30/js/                  
[06:53:50] 403 -  277B  - /.htaccess_orig                                   
[06:53:50] 403 -  277B  - /.htaccess.orig                                   
[06:53:50] 403 -  277B  - /.htaccess_extra                                  
[06:53:50] 403 -  277B  - /.htaccessBAK
[06:53:50] 403 -  277B  - /.ht_wsr.txt
[06:53:50] 403 -  277B  - /.htaccessOLD
[06:53:50] 403 -  277B  - /.htaccess_sc
[06:53:50] 403 -  277B  - /.htaccess.bak1
[06:53:50] 403 -  277B  - /.htaccess.sample
[06:53:50] 403 -  277B  - /.htaccessOLD2
[06:53:50] 403 -  277B  - /.htaccess.save                                   
[06:53:51] 403 -  277B  - /.htm                                             
[06:53:51] 403 -  277B  - /.htpasswd_test                                   
[06:53:51] 403 -  277B  - /.httr-oauth                                      
[06:53:51] 403 -  277B  - /.htpasswds                                       
[06:53:51] 403 -  277B  - /.html                                            
[06:53:55] 403 -  277B  - /.php                                             
[06:54:57] 200 -   48B  - /composer.json                                    
[06:54:57] 200 -    9KB - /composer.lock                                    
[06:55:03] 301 -  310B  - /css  ->  http://10.10.186.30/css/                
[06:55:04] 302 -    0B  - /dashboard.php  ->  dashboard.php                 
[06:55:22] 301 -  312B  - /flags  ->  http://10.10.186.30/flags/            
[06:55:38] 301 -  317B  - /javascript  ->  http://10.10.186.30/javascript/  
[06:55:39] 403 -  277B  - /js/                                              
[06:55:45] 200 -    1KB - /login.php                                        
[06:55:46] 302 -    0B  - /logout.php  ->  index.php                        
[06:55:47] 200 -    1KB - /mail.log                                         
[06:56:09] 301 -  317B  - /phpmyadmin  ->  http://10.10.186.30/phpmyadmin/  
[06:56:13] 200 -    3KB - /phpmyadmin/doc/html/index.html                   
[06:56:15] 200 -    3KB - /phpmyadmin/                                      
[06:56:15] 200 -    3KB - /phpmyadmin/index.php                             
[06:56:31] 403 -  277B  - /server-status/                                   
[06:56:31] 403 -  277B  - /server-status
[06:57:01] 403 -  277B  - /vendor/                                          
[06:57:02] 200 -    0B  - /vendor/composer/autoload_static.php              
[06:57:02] 200 -    0B  - /vendor/composer/autoload_files.php
[06:57:02] 200 -    0B  - /vendor/composer/autoload_classmap.php
[06:57:02] 200 -    0B  - /vendor/composer/autoload_psr4.php
[06:57:02] 200 -    1KB - /vendor/composer/LICENSE
[06:57:02] 200 -   12KB - /vendor/composer/installed.json
[06:57:02] 200 -    0B  - /vendor/autoload.php
[06:57:02] 200 -    0B  - /vendor/composer/ClassLoader.php
[06:57:02] 200 -    0B  - /vendor/composer/autoload_real.php
[06:57:02] 200 -    0B  - /vendor/composer/autoload_namespaces.php          
                                                                             
Task Completed
```
*Intresting Findings*
![image](https://github.com/user-attachments/assets/3a1829fb-1348-4180-bcbb-55557c9b93ee)

![image](https://github.com/user-attachments/assets/25ec408b-f65b-418d-a8c9-3f690cbb02ca)

**QUESTIONS FROM THE ROOM**
***Q1.What is the flag value after logging into the admin panel?***
for this first visited the login page and tried to intercept the request using burp suite community edition as i have the creditial already i just need to delete tha 'users' table from the database.
![burp](https://github.com/user-attachments/assets/4b049b91-d7ba-4dbd-91f8-a47abab018a4)

then, i sent the request to intruder and used the SQLi payload from `https://github.com/payloadbox/sql-injection-payload-list/blob/master/Intruder/exploit/Auth_Bypass.txt`
![intrude](https://github.com/user-attachments/assets/87f756e5-f424-4b2a-8c11-158e4044b667)

![VirtualBox_kali-linux-2024 3-virtualbox-amd64_14_06_2025_17_28_03](https://github.com/user-attachments/assets/3c2707bd-d2f3-4745-8202-e8ac686963a9)

and from this i got the payload and refreshed the page and i got into it,also To get access to the admin panel for the challenge question, I need to delete the ‘users’ table. So I want to find somewhere to inject:
`drop table users -- -`
after refreshing 
 and  after logging out we use the admincredentials and _voila_
 ![VirtualBox_kali-linux-2024 3-virtualbox-amd64_14_06_2025_18_12_06](https://github.com/user-attachments/assets/b1215812-4205-4d57-8b90-abd6d115eb2d)

 ***What is the content of the hidden text file in the flags folder?***
 for this we'll look for a SSTI on the page where the input can give us RCE or directly get the result
 



