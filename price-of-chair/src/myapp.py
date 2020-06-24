__author__: str = 'bernardino'
import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.johnlewis.com/john-lewis-partners-duhrer-dining-chair/grey/p3176433')
content = request.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find('span', {'class':'price__current'})
string_price = element.text.strip()
price = float(string_price[string_price.find('£')+1:])
print(price)

#https://www.johnlewis.com/john-lewis-partners-duhrer-dining-chair/grey/p3176433
# <span class="price__label">
#                                                                 Now
#                                                             </span>
