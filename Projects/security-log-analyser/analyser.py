import argparse 
from datetime import datetime, timedelta 

def detect_suspicious_logins(file):
    failed_attempts = {}

    for line in file:
        if "FAILED" in line:
            part = line.split()

            if len(part) < 5: #check if index 4 exists
                continue

            if not part[4].startswith("ip="):
                continue

            timestamp = f"{part[0]} {part[1]}"
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") 
                    
            ip = part[4].replace("ip=","")

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

def main(): 
    parser = argparse.ArgumentParser(description="Analyse authentication logs for suspicious activity") 
    parser.add_argument("logfile", help="Path to the authentication log file") 
    args = parser.parse_args() 

    try:
        with open(args.logfile,"r") as file:
            result = detect_suspicious_logins(file)

    except FileNotFoundError:
        print("Log file not found")
        return 

    for ip, window in result.items():
        formatted_times = [timestamp.strftime("%H:%M:%S") for timestamp in window]

        time_text = ", ".join(formatted_times)

        print(f"Suspicious IP: {ip}")
        print(f"Failed attempts: {time_text}")
        print(f"Reason: {len(window)} failed login attempts within 5 minutes")
        
if __name__ == "__main__":
    main() 

