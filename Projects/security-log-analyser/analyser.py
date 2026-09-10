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

with open("auth.log","r") as file:
    result = count_failed_logins(file)

    for ip, count in result.items():
        if count >= 3:
            print(f"IP: {ip} - Failed attempts: {count}")

try:
    with open("auth.log","r") as file:
        result = count_failed_logins(file)

except FileNotFoundError:
    print("Log file not found")

