# Linux Basics

## What is Linux?
Linux is a free and open-source operating system based on the UNIX architecture. It's role is to serve as the core software that manages hardware resources like the CPU and memory, allowing communication between hardware and software.
Linux consists of :
- Kernel: manages hardware resources and system processes
- Shell: command-line interface that allows users to interact with the system by executing commands
- System Libraries: pre-written code that applications use to perform tasks, acting as an interface between the kernel and the user applications
- Desktop Environment: A graphical interface that provides icons and windows for user interaction

## Why is Linux used?
Linux is used for its security, flexibility and stability. It is less prone to malwares and viruses compared to other operatuing systems. Linux is open source therefure users can modify and distribute the code freely. Furthermore, linux is very customisable which makes it suitable for personal use, enterprise servers and embedded systems.

## Linux Distributions
Popular distributions include:
- Beginners: Ubuntu, Linux Mint, Elemntroy OS
- Advanced: Arch Linux, Fedora, Debian
- Servers: CentOS, Ubuntu Server, Red Gat Enterprise Linux(RHEL)
### Uses: 
- Ubuntu: development, servers and learning linux
- Kali Linux: deisgned for cybersecurity and penetration testing as it comes with pre-installed security tools for ethical hacking and digital forensics
- Debian: security and stability 

# Linux and Cybersecurity
Most security appliances, network devices and cloud servers run on Linuxm which make it crucial for cybersceurity professionals to master it for effective protection.

## Terminal
A text-based interface which allows users to enter commands and recieve output from the computer, often through a shell program that interprets those commands

### Why the terminal is used over Windows
- faster for many tasks
-provides greater control over the operating system
-allows automation using scripts
-manages servers

## Linux File System

## Basic Navigation Commands
- pwd: shows current location
- ls: list everything
- cd: move between folders
- mkdir: create folders
- touch: create files
- nano: edit files
- cat: view file contents
- cp: copy files
- mv: move or rename files
- rm: delete files
- rmdir: delete empty folders

## File Management Commands
- ls -l: shows permissions
- chmod: changes permissions

### Permissions:
ls -l will show permissions for e.g -rw-r--r--
- -: file
- d: folder
- owner|group|other
- r: read
- w: write
- x: execute

### Using chmod
- u: owner
- g: group
- o: other
- a: everyone
- +: add
- -: minus
- e.g chmod o-r files.txt : removes read from others

## Users and Privileges Commands
- whoami: shows user ID, group ID, groups you belong to id
- sudo: allows user to run a command as root

### Users vs Privileges Notes
- user is an account that interacts with the linux system
- groups allow permission to be given to multiple users
- root: superuser/administrator with extremely high privileges
- using as root makes system more prone to errors or malicious commands which can effect the whole sytsem
- privilege escalation: gaining higher privileges from normal account

## System Investigation Basics
shows who is using the system and the activity 
- who: currently logged in users
- w: more information on those currently logged
- last: previous login information and system session history

## System Information Commands
- hostname: hostname of the Linux system 
- uname: operating system/kernel family e.g Linux
- uname -a: gives more information about kernel inluding system name,kernel version and system architecture
- df -h: shows available.used disk space
- free -h: memory(RAM) usage
- ps: shows what processes are running
- ps aux: more information; USER, PID, %CPU, %MEM, COMMAND
- top: gives a live updating view
- q: to exit top

### System Information Notes
hostname: shows what machine I am currently working on as you might connect to several machines
Uname -a:Knowing the OS and kernel versioin can matter when assesing a system because certain vulnerabilities may only affect particular versions
- gives more information about kernel inluding system name,kernel version and system architecture
- df -h: disk free, human readable
This command includes size, usedm available space and Use%(percentage used)
- process: running program
- PID: every running process gets an ID
- CMD: the command/program running e.g bash
- sleeping processes aren't broken, waiting for something and dont need CPU time

