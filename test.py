
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

doctors = fichier.find_all("div", class_="item-professionnel")

doctor_infos = []

for doctor in doctors[:50]:
    name = doctor.find("div", class_="nom_pictos").text.strip()
    phone = None
    if(doctor.find("div", class_="tel") is not None):
        phone = doctor.find("div", class_="tel").text.strip()

    address = doctor.find("div", class_="adresse").text.strip()
    doctor_infos.append({"name": name, "phone": phone, "address": address})
    print(name)
    df = pd.DataFrame(doctor_infos)
    df.to_csv("doctors.csv", index=False)





with open("post.html", "w") as file:
    file.write(str(fichier))