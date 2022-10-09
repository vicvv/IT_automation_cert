
import re
import csv


logs = open("/Users/vicky/Desktop/Desktop/CodePracticePython/IT_Authomation/final_python_os/syslog.log","r").readlines()
err_count = {}

for log in logs:
    error = re.findall(r'ERROR.*\(',log)
    print(error)
    if len(error) > 0:
        log_text = error[0].replace("ERROR","").replace("(","").strip()
        #print(log_text)
        err_count[log_text]= err_count.get(log_text,0) + 1
        
rows = dict(sorted(err_count.items(), key=lambda item: item[1], reverse=True))
#print(rows)

with open('error_message.csv', 'w', newline='') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ['Error', 'Count'])
    writer.writeheader()

    for key,value in rows.items():
        writer.writerow({'Error' : key, 'Count': value})
   


all_count = {}
for log in logs:
    username = re.search(r'\(.*\)',log).group().strip("()")
    error = re.search(r'(ERROR|INFO)',log).group()
    if username not in all_count:
        all_count[username] = [error]
    else:
        all_count[username] += [error]

all_sorted = sorted(all_count.items(),key=lambda item: item[0])
#print(all_sorted)


with open('user_statistics.csv', 'w', newline='') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ["Username", "INFO", "ERROR"])
    writer.writeheader()
    
    for k,v in all_sorted:
        writer.writerow({"Username":k, "INFO":v.count('INFO'), "ERROR":v.count('ERROR')})
        
           