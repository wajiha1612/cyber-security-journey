# Python
## Basics:
- String str e.g "house"
- Integer int e.g 3
- Decimal float e.g 3.4
- Boolean bool e.g True
- NoneType e.g None
- can check a variable's type using type(age) and to see output print(type(age))

## Conversions:
- int("19")
- float("1.2")
- str(19)
- bool(1)
- input always gives a string therefore need to use int() 

## Indexing and Slicing:
- text = "cybersecurity"
- python gives each character a position called index
    - print(text[0])   # c
    - print(text[3])   # e
### Negative:
- print(text[-1])  # y
- print(text[-2])  # t

## Slicing
- text[0:4] : start at 0. stop before 4 e.g cybe
- text[4:8] : start at 4, end at 7 e.g rsec
- text[:4]    # first 4 characters
- text[4:]    # from position 4 to the end

## .split():
takes a string and breaks it into a list of smaller strings
- text = "hello world"
- words = text.split()
- print(words)
- output: ['hello', 'world']
- Can use the brackets to decide what to split on e.g (".")

## .join():
It combines a list into a string
- parts = ["192", "168", "1", "10"]
- ip = ".".join(parts)
- print(ip)
- output: 192.168.1.10

## .replace()
Replaces one piece of text with another
- text = "user=admin"
- print(text.replace("admin", "guest"))
- output:user=guest

## Checking what is inside a string
- text = "failed login attempt"
- print("loging" in text)
- output: True

## Operators 
- print(10 // 3)   # 3
- print(10 % 3)    # 1
- print(2 ** 3)    # 8
- // : floor division(whole number)
- % : remainder
- ** : power

## Comparisons
- 5 == 5    # True
- 5 != 3    # True
- 5 > 3     # True
- 5 < 3     # False
- 5 >= 5    # True
- 5 <= 4    # False

- = assigns a value
- == compare two values

## f String
a string where {} can contain variable or experessions
- for : when you know what you are going through/repeating
- while: keep going until a condition changes

## Break and Continue
- break: completely stops the loop
- continue: skips the currect iteration and carries on

## Lists
list = ["ItemA" , "ItemB" , "ItemC"]
- adding: list.append("ItemD")
- removing: list.remove("ItemA")
- checking if it exists: "ItemB" in list
- number of time: len(list) 
- remove at position: list.pop(1)

# Dictionaries
- structured data: keys and values
- user = {
    - "name": "Waj",
    - "age": 19,
    - "student": True
- }
- Access a value using its key: print(user["name"])
- can add, change, check if key exists
### checking all items
- for key, value in user.items():
    - print(key, value)

# Security Log Analyser process:
- function can take data through parameters and return result using return
- dictionaries can store count using the ip address key
