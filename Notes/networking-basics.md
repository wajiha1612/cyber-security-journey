# Networking Basics

## Network?
A collection of interconnected devices that communicate and share resources, either by cables or wirless connection
### Why networks exist
Networks have 3 fundamental purposes:
-Resource Sharing:Instead of one internet connection, file storage and software application per person, everyone uses one high quality one
-Communication: enables communication through email, messages and calls instead of physically moving storage devices
-Cantralised Management: IT administrators manage security, updates and user access from a central location

### Types of devices on a network
Some types of Devices: Laptops, phones, printers, servers, security cameras etc

## LAN, WAN and the Internet
### LAN
A LAN covers a small geographic area like home, office or school building. 
All devices can communicate directly with eachother
### WAN
A WAN covers a large geographical area connecting cities, countries etc
The internet is the largest WAN
Companies also create private WANs to connect their offices worldwide
### Internet
A global network of interconnected computer networks that allows devices to communicate and share information using internet protocols
### Home network vs company network
Home network is a small network for personal devices such as laptops or phones using a home router.Whereas company network is a larger network connecting many users, devies and servers with strong security controls

## Clients and Servers
### Client
A device or application that requests infromation or service from computer e.g laptop, phone, web browser

### Server
A computer that provides information, resources or services to client e.g google servers, website servers

Example: Your laptop(client) requests a webpage and the website server sends the webpage back

## IP Addresses
uAn IP address is an unique numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. it allows  devices to identify each other and send data to the correct destination
### IPv4
-This version uses 32-bit address scheme allowing for a total of 4.2 billion unique addresses
-typically written in dot-decimal notation,consisting of four decimal numbers separated by dots
### IPv6 (basic idea only)
-IPv6 was produced due to the exhaustion of IPv4 which uses a 128-bit address scheme which provides a larger number of addresses.
-written in hexadecimal and are separated by colons
### Private IP
Private IP is used within a :AN network and is assigned by a router or DHCP server. It allows internal communication between different devices without exposing them to the internet as they are not routable on the ppublic internet and require Network Address Translation to access external networks
### Public IP
Public IP is globally unique and is assigned by an Internet Service Provider(ISP). It enables devices or networks to communicate directly over the internet. They are visible to external networks and are required for hosting services like websites 
### Loopback (127.0.0.1)
Part of the IPv4 loopback range 127.0.0.0/8. Any traffic which is sent to this range is routed internally by the operating systen's TCP?IP stack and never reaches the physical internet interface. Bypassing network hardware makes it essential for testing, diagnostics and local development

## MAC Addresses

Learn:

What a MAC address is
Difference between IP and MAC
Why both are needed
## Packets

Learn:

What a packet is
Why data is split into packets
What information packets contain



## OSI Model

Don't memorise every layer immediately.

Understand:

Why it exists
What each layer generally does
Be able to explain it simply
## TCP vs UDP

Very important.

Learn:

Reliable vs unreliable
Three-way handshake (basic)
Which applications use TCP
Which use UDP
## Ports

Learn:

What a port is
Why ports exist
Common ports:
20/21 FTP
22 SSH
25 SMTP
53 DNS
80 HTTP
110 POP3
143 IMAP
443 HTTPS

You don't need to memorise them all on day one.
## DNS

Learn:

What DNS is
Why we need it
What happens when you type google.com
How should your note look?
