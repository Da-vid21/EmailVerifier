import requests
from termcolor import colored
import time

def verifier(email):
    url = "https://email-checker.p.rapidapi.com/verify/v1"
    print(email)

    querystring = {"email": email}

    headers = {
        "X-RapidAPI-Key": "Your own API",
        "X-RapidAPI-Host": "email-checker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    isDisposable = response['disposable']
    status_color = "green" if response['status'] == "valid" else "red"
    status_text = colored(response['status'], status_color, attrs=["bold", "underline"])
    print(f"{email} is {status_text}\n \tReason: {response['reason'].strip()}\n \tIs Disposable: {isDisposable}")

with open("emails.txt", "r") as f:
    emailList = f.readlines()

count = int(open("count.txt", "r").readline())
# Limited requests for every 60 for the free plan
if(count <= 200):
    for email in emailList:
        if count % 5 == 0 and count != 0:
            time.sleep(2)
            print()
        verifier(email.strip())
        count+=1
    with open("count.txt", "w") as w:
        w.write(str(count))
else:
    print(colored("Monthly Usage Exceeded or reset your counter for this month under count.txt", 'red'))

