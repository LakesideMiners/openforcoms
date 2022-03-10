import requests
import in_place
import os
from bs4 import BeautifulSoup as bs


cookies = {'a': 'GLITCHisAredPANDA', 'b': 'PSPSPSPSPSPSPSPSPSPSPSPSPSPSPSP'}



def check(user):
    if os.path.exists(user):
        os.remove(user)
    else:
        pass
        
    r = requests.get("https://www.furaffinity.net/user/" + user, cookies=cookies)
    soup = bs(r.text, 'html.parser')
    content = soup.find_all("div", class_="table-row")
    with open(user, "x") as f: 
        for i in content:
            f.write(i.get_text())
    
    with in_place.InPlace(user) as f:
        for line in f:
            f.write(line.strip() + "\n")
    
    with in_place.InPlace(user) as f:
        for line in f:
            if not line.isspace():
                f.write(line)
check("mattswolf")

