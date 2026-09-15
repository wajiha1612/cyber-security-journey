import argparse #so program can recieve argument from terminal
from datetime import datetime, timedelta 

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
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") #timestamp is  object
            
            ip = part[4]            
            ip = ip.replace("ip=","")

            #counting failed attempts for each ip
            if ip in failed_attempts:
                failed_attempts[ip].append(timestamp)
            else:
                failed_attempts[ip] = [timestamp]

    suspicious_ips = {}

    for ip, timestamps in failed_attempts.items():
        for i in range(0,len(timestamps)-2):
            if timestamps[i+2] - timestamps[i] <= timedelta(minutes=5):
                window = [timestamps[i], timestamps[i+1], timestamps[i+2]]
                if ip not in suspicious_ips: #avoid duplicate ips
                    suspicious_ips[ip] = window           
    return(suspicious_ips)

def main(): #needs to work with list rather than dictionary
    try:
        with open(args.logfile,"r") as file:
            result = count_failed_logins(file)

    except FileNotFoundError:
        print("Log file not found")
        return #means leave main() function and stop the rest of the program

    for ip, window in result.items():
        print(f"Suspicious IP:{ip}")
        print(f"Failed attempts:{window}")

        for timestamp in window:
            print(timestamp.strftime("%H:%M:%S"))
main() 


