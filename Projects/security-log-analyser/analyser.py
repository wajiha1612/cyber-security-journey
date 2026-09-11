import argparse #so program can recieve argument from terminal
from datetime import datetime 

parser = argparse.ArgumentParser(description="Analyse authentication logs for suspicious activity") #creates parser and describes using --help
parser.add_argument("logfile", help="Path to the authentication log file") #what the parser is and explains user what to provide
args = parser.parse_args() #collects the argument user entered

def count_failed_logins(file):
    failed_attempts = {}

    for line in file:
        if "FAILED" in line:
            part = line.split()

            if len(part) < 5: #check if index 4 exists
                continue

            if not part[4].startswith("ip="):
                continue

            timestamp = f"{part[0]} {part[1]}"
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") #timestamp is  object
            datetime
            
            ip = part[4]            
            ip = ip.replace("ip=","")
            
            #counting failed attempts for each ip
            if ip in failed_attempts:
                failed_attempts[ip] = failed_attempts[ip] + 1
            else:
                failed_attempts[ip] = 1
                    
    return(failed_attempts)

def main():
    try:
        with open(args.logfile,"r") as file:
            result = count_failed_logins(file)

    except FileNotFoundError:
        print("Log file not found")
        return #means leave main() function and stop the rest of the program

    for ip, count in result.items():
        if count >= 3:
            print(f"IP: {ip} - Failed attempts: {count}")


main()



