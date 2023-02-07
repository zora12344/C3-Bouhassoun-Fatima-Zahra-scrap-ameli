
import requests
from bs4 import BeautifulSoup


payload= {
    "type": "ps",
    "ps_profession" : "34",
    "ps_profession_labe": "Médcin généraliste",
    "ps_localisation" : "HERAULT (34)",
    "localisation_category" : "département",

}

url = "http://annuairesante.ameli.fr/recherche.html"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

}
req = requests.Session()
page = req.get(url)


page = req.post(url, params=payload, headers= header)

if page.status_code == 200:
    lienrecherche = page.url

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)


for res in soup.find_all("div", "item-professionnel"):
    firstname_and_lastname = res.find("a")
    if len(firstname_and_lastname) != 2: # on skip les nom prénoms mal formatés
        continue
    firstname = firstname_and_lastname.contents[1].title()
    lastname_tag = firstname_and_lastname.contents[0]
    if lastname_tag:
        lastname = lastname_tag.string
        
    tel_tag = res.find("div", "tel")
    if tel_tag:
        tel = tel_tag.string
    else: 
        tel = ""

    address_with_tags = res.find("div", "adresse").contents

    address_without_tags = [address for address in address_with_tags if str(type(address)) != "<class 'bs4.element.Tag'>"]
    address = " - ".join(address_without_tags)

    print(f"{firstname},{lastname},{tel},{address}")
