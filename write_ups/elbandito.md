
## 🛡️ TryHackMe Room Write-up Template

````markdown
# 🏠 TryHackMe Room:elbandito
> Difficulty: Hard 
> Category:Http requests/websocket smuggling 
> Room URL: [https://tryhackme.com/room/elbandito](https://tryhackme.com/room/elbandito)

---

## 🧠 Overview

**Objective**:  
Can you help capture El Bandito before he leaves the galaxy?

---

## 🧰 Tools Used

- `nmap`
- `gobuster`
- ` Burpsuite`

---

## 🌐 Enumeration

### 🔍 Nmap Scan

```bash
nmap -sC -sV -A  -T4 -p- 10.201.38.191
Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-21 02:36 EDT
Stats: 0:04:09 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 48.31% done; ETC: 02:45 (0:04:26 remaining)
Stats: 0:10:00 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 95.79% done; ETC: 02:46 (0:00:26 remaining)
Stats: 0:11:56 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 75.00% done; ETC: 02:48 (0:00:26 remaining)
Nmap scan report for 10.201.38.191
Host is up (0.26s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 99:79:e4:b9:55:65:2f:51:b3:ee:70:8c:58:69:06:86 (RSA)
|   256 a7:3a:06:e6:2f:79:0a:0f:bf:e1:37:47:06:7d:9f:88 (ECDSA)
|_  256 38:b7:58:1b:8b:3e:f5:d4:24:32:98:6b:d3:50:30:21 (ED25519)
80/tcp   open  ssl/http El Bandito Server
|_http-server-header: El Bandito Server
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2021-04-10T06:51:56
|_Not valid after:  2031-04-08T06:51:56
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 NOT FOUND
|     Date: Sun, 21 Sep 2025 06:48:39 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 207
|     Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     Feature-Policy: microphone 'none'; geolocation 'none';
|     Age: 0
|     Server: El Bandito Server
|     Connection: close
|     <!doctype html>
|     <html lang=en>
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Sun, 21 Sep 2025 06:47:31 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 58
|     Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     Feature-Policy: microphone 'none'; geolocation 'none';
|     Age: 0
|     Server: El Bandito Server
|     Accept-Ranges: bytes
|     Connection: close
|     nothing to see <script src='/static/messages.js'></script>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Sun, 21 Sep 2025 06:47:33 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 0
|     Allow: OPTIONS, POST, GET, HEAD
|     Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     Feature-Policy: microphone 'none'; geolocation 'none';
|     Age: 0
|     Server: El Bandito Server
|     Accept-Ranges: bytes
|     Connection: close
|   RTSPRequest: 
|_    HTTP/1.1 400 Bad Request
631/tcp  open  ipp      CUPS 2.4
|_http-title: Forbidden - CUPS v2.4.7
|_http-server-header: CUPS/2.4 IPP/2.1
8080/tcp open  http     nginx
|_http-favicon: Spring Java Framework
|_http-title: Site doesn't have a title (application/json;charset=UTF-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :

````

---

## 📁 Web Enumeration

###port80 and 8080 we have 
<img width="798" height="174" alt="image" src="https://github.com/user-attachments/assets/8cf46aa5-aa42-487f-b623-c3f8c9a2053a" />
<img width="1334" height="610" alt="image" src="https://github.com/user-attachments/assets/2d4c46f9-1017-44c2-b586-7f31d10e5b39" />
under the port 90 `messages.js` we get a redirection to `/getmessages`
<img width="958" height="621" alt="image" src="https://github.com/user-attachments/assets/bd57412a-905e-48cf-a091-411ce47d2dd1" />


### Gobuster/Dirb Scan

```bash

```

**Interesting Findings**:

* `/getmessages`
* `/info`
* `/health`
* `/assets`

---

## 🔓 Exploitation
<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/f173228e-8ef4-452e-b997-d6d8bdee1785" />

since the web page on 8080 uses spring java framework i tried some searching find there are acuators that i can use and found one called mapping
since i had just did wssmuggling rooom i found the flag using the python web server code from there
got  creds
```
`HTTP/1.1 101 
Server: nginx
Date: Sun, 21 Sep 2025 08:34:12 GMT
Connection: upgrade
X-Application-Context: application:8081

HTTP/1.1 200 
X-Application-Context: application:8081
Content-Type: text/plain
Content-Length: 55
Date: Sun, 21 Sep 2025 08:34:11 GMT

username:hAckLIEN password:YouCanCatchUsInYourDreams404`
```
got theflag

now use the login creds on login mask on port 80
