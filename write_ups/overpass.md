
## 🛡️ TryHackMe Room Write-up Template

````markdown
# 🏠 TryHackMe Room: overpass
> Difficulty: medium 
> Category: Web Exploitation , Enumeration , Privilege Escalation>  
> Room URL: [https://tryhackme.com/room/Overpass](https://tryhackme.com/room/Overpass)

---

## 🧠 Overview

**Objective**:  
"Compromise the target machine through enumeration, exploit vulnerabilities, and escalate privileges to root."

---

## 🧰 Tools Used

- `nmap`
- `gobuster`
- `linpeas`
- `john/hashcat`


---

## 🌐 Enumeration

### 🔍 Nmap Scan

```bash
nmap -sC -sV  -T4  -Pn  10.201.18.241

````

**Output Summary**:

* Port 22 (SSH): Open
* Port 80 (HTTP): Apache 2.4.29
* Service versions, banners, vulnerabilities...

---

## 📁 Web Enumeration

### Gobuster/Dirb Scan
```

gobuster dir -u http://10.201.18.24 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.201.18.24
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 0] [--> img/]
/downloads            (Status: 301) [Size: 0] [--> downloads/]
/aboutus              (Status: 301) [Size: 0] [--> aboutus/]
/admin                (Status: 301) [Size: 42] [--> /admin/]
/css
```
---

## 🔓 Exploitation

### Vulnerability Found
* the admin page was a intresting finding
* <img width="285" height="54" alt="image" src="https://github.com/user-attachments/assets/fb217303-b14b-4056-aec6-dd87c4019098" />

* Found a Private for username james by exploiting the cookie function and since there was ssh portt open i then used tthe key
* <img width="374" height="55" alt="image" src="https://github.com/user-attachments/assets/fad6b92f-d999-4f2f-8014-f23a80b70ee6" />
* <img width="618" height="430" alt="image" src="https://github.com/user-attachments/assets/cc072266-2518-4ccc-9fe7-c0a6dbbccc0b" />

### Shell Access

we use the rsa key to access ssh on the page and used john to crack the password for the ssh entry
<img width="620" height="203" alt="image" src="https://github.com/user-attachments/assets/69c4598c-0fb0-444b-b814-0c3356f439ca" />
<img width="570" height="388" alt="image" src="https://github.com/user-attachments/assets/6012b4e0-f38b-4581-8a93-a26b25c51fd2" />



**Initial Shell**: `/home/james`

---

## 📈 Privilege Escalation

## Enumertion
by accessing the todo list on james's machine we get a automated script is running meaning we can use cronjobs to get our privlges escalete
also,We get some interesting information from this:

There is some kind of password in the password manager they wrote
The encryption is weak
There is some kind of automated build script running
Ok, remember the source code we got from the first step? There is some interesting stuff in it:
```
func main() {
	credsPath, err := homedir.Expand("~/.overpass")
	if err != nil {
		fmt.Println("Error finding home path:", err.Error())
	}
	//Load credentials
    passlist, status := loadCredsFromFile(credsPath)
    ...
```
The credentials are stored in ~/.overpas
<img width="591" height="37" alt="image" src="https://github.com/user-attachments/assets/71741a61-0aeb-4035-9e20-a22f8a760043" />
There is another interesting function in the source code:
```
func rot47(input string) string {
	var result []string
	for i := range input[:len(input)] {
		j := int(input[i])
		if (j >= 33) && (j <= 126) {
			result = append(result, string(rune(33+((j+14)%94))))
		} else {
			result = append(result, string(input[i]))
		}
	}
	return strings.Join(result, "")
}

```
<img width="946" height="537" alt="image" src="https://github.com/user-attachments/assets/38173c01-08f6-42d2-a883-f89b649d9a49" />
<img width="847" height="284" alt="image" src="https://github.com/user-attachments/assets/59af810b-23f1-46b1-95eb-82a619bf3f88" />
<img width="766" height="198" alt="image" src="https://github.com/user-attachments/assets/c629e621-7a5c-40bc-8353-b36141839763" />
<img width="770" height="102" alt="image" src="https://github.com/user-attachments/assets/23bcddf1-a8bd-43f3-a231-72e156e10e1c" />
<img width="857" height="555" alt="image" src="https://github.com/user-attachments/assets/55d81be1-bb86-439e-99f2-d170b08c93c5" />


### Vulnerability Found

* Authenttication bypass

---


---

## 💡 Lessons Learned

* Key takeaways from the room.
* New tools or techniques learned.
* Any real-world relevance.

---



