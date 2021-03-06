# Scrape Wikipedia and extract one table from page
import pandas as pd

wikiurl = "https://en.wikipedia.org/wiki/Comma-separated_values"
table_class = "wikitable"
response = requests.get(wikiurl)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
csv = soup.find('table',{'class':"wikitable"})


df = pd.read_html(str(csv))
df = pd.DataFrame(df[0])

print(df)
