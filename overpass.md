
## 🛡️ TryHackMe Room Write-up Template

````markdown
# 🏠 TryHackMe Room: overpass
> Difficulty: medium 
> Category: Web Exploitation , Enumeration , Privilege Escalation>  
> Room URL: [https://tryhackme.com/room/Overpass](https://tryhackme.com/room/Overpass)

---

## 🧠 Overview

**Objective**:  
A brief description of the room’s goals. For example:  
"Compromise the target machine through enumeration, exploit vulnerabilities, and escalate privileges to root."

---

## 🧰 Tools Used

- `nmap`
- `gobuster`
- `hydra`
- `dirb`
- `burpsuite`
- `linpeas`
- `netcat`
- `john/hashcat`
- Any others used...

---

## 🌐 Enumeration

### 🔍 Nmap Scan

```bash
nmap -sC -sV -T4 -Pn <target-ip> -oN nmap.txt
````

**Output Summary**:

* Port 22 (SSH): Open
* Port 80 (HTTP): Apache 2.4.29
* Service versions, banners, vulnerabilities...

---

## 📁 Web Enumeration

### Gobuster/Dirb Scan

```bash
gobuster dir -u http://<target-ip> -w /usr/share/wordlists/dirb/common.txt -x php,txt,html -o gobuster.txt
```

**Interesting Findings**:

* `/admin`
* `/login.php`
* `/robots.txt`

---

## 🔓 Exploitation

### Vulnerability Found

* Description of the vulnerability (e.g., LFI, SQLi, file upload).
* CVE if applicable.
* Proof of concept or exploit steps.

### Shell Access

```bash
nc -lvnp 4444
# or reverse shell payload used
```

**Initial Shell**: `www-data@target`

---

## 📈 Privilege Escalation

### Enumeration with LinPEAS

* Use `linpeas.sh`, `sudo -l`, or manual checks:

```bash
sudo -l
cat /etc/passwd
```

### Vulnerability Found

* Misconfigured sudo
* Cron job
* SUID binary
* Kernel exploit

---

## 🔑 Flags

* `user.txt`: `THM{xxxxxxxxxxxxxxxxxxxxxxxx}`
* `root.txt`: `THM{yyyyyyyyyyyyyyyyyyyyyyyy}`

---

## 💡 Lessons Learned

* Key takeaways from the room.
* New tools or techniques learned.
* Any real-world relevance.

---

## 📁 Bonus: GitHub Structure Suggestion

If you’re uploading this write-up to GitHub:

```
tryhackme-writeups/
└── <room-name>/
    ├── README.md    # ← Write-up
    ├── nmap.txt
    ├── gobuster.txt
    ├── linpeas.log
    └── exploit.py   # If applicable
```

---

## 🧠 References

* [TryHackMe Room](https://tryhackme.com/room/<room-name>)
* [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [GTFOBins](https://gtfobins.github.io/)

```

---

Would you like me to auto-generate this as a **Markdown file** or fill it in with data from a specific room you’ve done (e.g., *Vulnversity* or *Mr Robot*)?
```
