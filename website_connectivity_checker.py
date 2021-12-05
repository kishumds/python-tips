import requests

def check_connection(site):
    status = requests.get(site).status_code
    print("Working") if status == 200 else print("Not Working")

check_connection(input("Enter Website: "))