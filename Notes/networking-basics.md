# Networking Basics

## Network?
A collection of interconnected devices that communicate and share resources, either by cables or wirless connection
### Why networks exist
Networks have 3 fundamental purposes:
- Resource Sharing:Instead of one internet connection, file storage and software application per person, everyone uses one high quality one
- Communication: enables communication through email, messages and calls instead of physically moving storage devices
- Cantralised Management: IT administrators manage security, updates and user access from a central location

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
Media Access Control: a unique identifier assigned to a network interface controller(NIC) for use as a network address in communications within a network segment
### Difference between IP and MAC
An IP address is an address assigned to a device by an Internet Service Provider, where it identifies the device's location on a network and is used for communication berween devices across different networks. IP addresses operate at network layer
A MAC address is a hardware-based address embedded into a device's Network Interface Card by manufactures. It remains constant regardless of the network environment and works within a local network
#### Key differences:
- Scope: MAC addresses work on local networks, while IP addresses work across networks.
- Permanence: MAC addresses are fixed, while IP addresses can change.
- Layer: MAC addresses use the Data Link layer (Layer 2), while IP addresses use the Network layer (Layer 3).
- Assignment: MAC addresses are assigned by the NIC manufacturer, while IP addresses are assigned by an ISP or router.

## Packets
A small unit of data which is sent across the network. When information is transmitted, it is first broken down into packets. Each packet travels across the network and is reassembled at the destination to recreate the orginial data e.g webpage or emails
### Why data is split into packets
Splitting data into packets makes communication more efficient and reliable. The benefits include large files being transmitted more quicly, if one packet is lost and corrupted then only that packet needs to be resent instead of the entire file, different packets cansometimes take different routes across the network to the same destination
### What information packets contain
A packet consists of the actual data being sent and information that helps it reach the correct destination.
This information includes:
- Source IP address – where the packet came from.
- Destination IP address – where the packet is going.
- Payload – the actual data being transmitted.
- Sequence number – helps the receiving device put packets back in the correct order.
- Error-checking information – helps detect if the packet was damaged during transmission.

## OSI Model
A framework that explains how data trave;s from one device to another over a network
### Why it exists
OSI model has several uses:
- Standardise how networks communicate.
- Break complex communication into smaller steps.
- Make it easier to troubleshoot network problems.
- Allow hardware and software from different manufacturers to work together.
### The layers:
- Application: Provides network services to applications (e.g. HTTP, DNS, SMTP)
- Presentation: Formats, encryots and compresses data so the recieving device can understand it (e.g SSL/TLS encryption)
- Session: Establishes, manages and terminates communication sessions between devices (e.g login sessions)
- Transport: Ensures data is delivered correctly (TCP/UDP)
- Network: Routes data using IP addresses
- Data Link: Transfers data on the local network using MAC addresses
- Physical: Sends data as electrical, radio or optical signals

## TCP vs UDP
Transmission Control Protocol is a connection oriented protocol that ensures data is delivered reliably and in the correct order. Therefore, if a packet is lost, TCP retransmits it
It ensures:
- Data arrives successfuly
- Data arrives in correct order
- Lost packets are retransmitted
- Errors are detected

User Datagram Protocol is a connectionless protocol that sends data without checking if it arrived, It is faster than TCP because it does not wait for acknowledgements or retransmit lost packets

- Does not establish a connection
- Does not retransmit lost packets
- Does not guarantee packet order
- Faster than TCP

###Reliable VS Unreliable
TCP (Reliable)
- Checks that packets arrive.
- Resends missing packets.
- Maintains packet order.

UDP (Unreliable)
- Sends packets without confirmation.
- Lost packets are not resent.
- Packet order is not guaranteed.

### Three-Way Handshake
Before TCP sends data, it establishes a connection using three steps:

1. SYN – The client requests a connection.
2. SYN-ACK – The server accepts the request.
3. ACK – The client confirms the connection.

After these three steps, data transmission begins

### Cybersecurity Relevance

TCP and UDP are important for analysing network traffic and understanding how applications communicate.

## Ports
A logical communication endpoint on a device. It allows multiple applications and services to send and recieve data over the same IP address. For example, a computer can browse the web and receive emails at the same time because each service uses a different port.

### Common ports:
#### Port 20/21 – FTP (File Transfer Protocol)
Used for transferring files between computers.

#### Port 22 – SSH (Secure Shell)
Used for securely connecting to and managing remote computers.

#### Port 25 – SMTP (Simple Mail Transfer Protocol)
Used for sending emails.

#### Port 53 – DNS (Domain Name System)
Used to translate domain names (e.g. google.com) into IP addresses.

#### Port 80 – HTTP (Hypertext Transfer Protocol)
Used for accessing websites without encryption.

#### Port 110 – POP3 (Post Office Protocol v3)
Used to download emails from a mail server.

#### Port 143 – IMAP (Internet Message Access Protocol)
Used to access and manage emails while keeping them on the mail server.

#### Port 443 – HTTPS (Hypertext Transfer Protocol Secure)
Used for secure, encrypted communication between a web browser and a website.


## DNS
Domain Name System translates domain names into IP addresses. It allows users to access websites using names instead of numerical IP addresses. For example:
google.com → 142.250.xxx.xxx
If DNS did not exist, users would have to remember the IP address of every website they wanted to visit.

### What happens when you type google.com?

1. You enter **google.com** into your web browser.
2. Your device sends a DNS request to a DNS server.
3. The DNS server looks up the IP address for **google.com**.
4. The DNS server returns the IP address to your device.
5. Your browser uses the IP address to connect to Google's web server.
6. Google's server sends the website back to your browser.
