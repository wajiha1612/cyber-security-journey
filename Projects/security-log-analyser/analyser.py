import argparse #so program can recieve argument from terminal

parser = argparse.ArgumentParser()
parser.add_argument("logfile")
args = parser.parse_args()

def count_failed_logins(file):
    failed_attempts = {}

    for line in file:
        if "FAILED" in line:
            part = line.split()
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

