#recapping basic python to run it throught the terminal

#declaring variables
name = "waj"
age = 19

print("My name is",name)
print("My age is",age)

#checking variable type
name = "waj"
age = 19

print(type(name))
print(type(age))

#changing data types
age = "19" #age is a string
age = int(age) #age is now an integer

#indexing and slicing
text = "cybersecurity"
print(text[0]) #first letter
print(text[-1]) #last letter
print(text[0:5]) #cyber
print(text[5:]) #security

#splitting strings
ip = "192.168.1.10"

parts = ip.split(".")

print(parts)

##joining a list
parts = ["192", "168", "1", "10"]

ip = ".".join(parts)

print(ip)

#replacing piece of text with another
text = "user=admin"
print(text.replace("admin", "guest"))

## checking what's inside a string
log = "ERROR: failed login from 192.168.1.10"

print("failed" in log) #outputs True
print("SUCCESS" in log) #outputs False

#write a tiny program that asks the user for their name and age, then prints something like: Hello Waj, you are 19 years old.
name = input("What is your name?")
age = int(input("What is your age?"))

print(f"Hello {name}, you are {age} years old")

#write a program asking user age, checking if they are 18 or older and print adult or 18
age = int(input("What is your age? "))
if age >= 18:
    print("Adult")
else:
    print("You are under 18")

#lists
tools = ["nmap", "Wireshark", "Python"]

for tool in tools:
    print(tool)

#tuples
#tools = ("nmap","Wireshark")
#tools[0] = "Burp Suite"# will cause an error as tuples cannot be changed

#Sets:collection of values where duplicates are utomatically removed
ports = {22, 80, 443, 80, 22}

print(ports) #would get 22,80,443
#can add or remove using .add and .remove

#creating a function
def greet():
    print("Hello!")

greet()

#function can accept parameters
def greet(name):
    print("Hello", name)

greet("Waj")

#return can stop a function early
def check_user(username):
    if username == "admin":
        return "Admin"
    
    return "Regular user"

print(check_user("admin")) #matches and function returns Admin
print(check_user("waj")) #does not continue to the next return

#reading testlog.txt file through python
with open("testlog.txt","r") as file:
    data = file.read()

print(data)

#reading same file line by line
with open("testlog.txt","r") as file:
    for line in file:
        print(line)

#modify your loop so that it prints only the failed login lines
with open("testlog.txt","r") as file:
    for line in file:
        if "failed" in line :
            print(line)

#print just the IP from a failed line
with open("testlog.txt","r") as file:
    for line in file:
        if "failed" in line:
            parts = line.split()
            print(parts[3])

#counting value of failed attempt ip
failed_attempts = {}

with open("testlog.txt", "r") as file:
    for line in file:
        if "failed" in line:
            parts = line.split()
            ip = parts[3]

            if ip in failed_attempts:
                failed_attempts[ip] = failed_attempts[ip] + 1
            else:
                failed_attempts[ip] = 1

print(failed_attempts)

for ip, count in failed_attempts.items():
    print(f"IP: {ip} - Failed attempts: {count}")

#write to a file(write/replace)
with open("report.txt","w") as file:
    file.write("Security report")

#appending to file(adding to the end)
with open("report.txt", "a") as file:
    file.write("\nSecond line") # donest automatically add new line so use \n

#error
#with open("does_not_exist.txt", "r") as file:
#   data = file.read()

#exception handling
try:
    with open("does_not_exist.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("The file was not found")