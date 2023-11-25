import requests
from bs4 import BeautifulSoup as bs

#url = "https://app.ezshift.co.il/pages/ScheduleMy.aspx"
#r = requests.get(url)
#r.raise_for_status()

session= requests.Session()

auth_html= session.get("https://app.ezshift.co.il/pages/loginHE-il.aspx")
auth_bs=bs(auth_html.content,'html.parser')
view_state=auth_bs.select("input[name=__VIEWSTATE]")[0]['value']
view_state_generator=auth_bs.select("input[name=__VIEWSTATEGENERATOR]")[0]['value']
event_validation_state=auth_bs.select("input[name=__EVENTVALIDATION]")[0]['value']

payload = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator ,
    '__EVENTVALIDATION': event_validation_state,
    'Username': '*****',
    'Password': '***',
    'Company': '*******',
    'remember': 'on',
    '_ctl1': 'התחבר'
}      
session.post('https://app.ezshift.co.il/pages/loginHE-il.aspx', data=payload)

response = session.post('https://app.ezshift.co.il/pages/ScheduleMy.aspx')
html = bs(response.text, 'html.parser')
print(html.select(".table > .card"))

#html = bs(r.text, 'html.parser')
#print(html.select(".card"))
#for el in html.select("._default-grid_vrdym_258 > ._card_6bcao_1"):
 #   title = el.select('._card_6bcao_1 > a')
  #  if title:
   #     print(title[0].text)
