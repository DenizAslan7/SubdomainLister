import requests


def mak_request(url):
    try:
        return requests.get(url)
    except:
        pass

target_input = "google.com"

with open("subdomainlist.txt","r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "https://" + word + "." + target_input
        response = mak_request(url)
        if response:
            print("Found Subdomain ------> " + url)