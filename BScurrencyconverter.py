from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    #hämtar själva content -htmltexten
    html_data = requests.get(url).content

    #skapar ett html-objekt
    soup = BeautifulSoup(html_data, 'html.parser')
    #hittar span-elementet med classnamnet ccOutputRslt. Tar bara texten
    result = soup.find('span', class_='ccOutputRslt').get_text()

    return float(result[:-4])


print(get_currency('EUR', 'SEK'))
#<span class="ccOutputRslt">10.51<span class="ccOutputTrail">8588</span><span class="ccOutputCode"> SEK</span></span>
#</div>

