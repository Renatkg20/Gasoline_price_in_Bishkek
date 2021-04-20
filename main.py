import requests
from bs4 import BeautifulSoup
import re



def get_url():
  list1 = []
  url = "http://bpetroleum.kg"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'petrol-prices'}).find_all('tr')
  result  = soup
  for i in result:
      list1.append(i.get_text())

  return f'Bishkek Pertorleum, Официальные цены \n============\n {list1[0]} \n {list1[1][0:6]} | {list1[1][6:]} \n {list1[2][0:7]} | {list1[2][7:]} \n {list1[3][0:10]} | {list1[3][10:]} \n {list1[4][0:10]} | {list1[4][10:]} \n {list1[5][0:10]} | {list1[5][10:]} \n {list1[6][0:2]} | {list1[6][2:]} \n {list1[7][0:3]} | {list1[7][3:]}\n ============\n Цена ГСМ по г. Бишкек \n {url}'



print(get_url())



def get_url_rosneft():
  url = "http://www.knp.kg/"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  # soup = soup.find('div', {'class': 'mb50'}).find_all('ul', {'class': 'retailPrice'})
  soup = soup.find('aside', {'class': 'informer'})
  result  = soup.get_text()
  total = result.split("\n")

  return f"РосНефть Кыргызстан, Розничная стоимость ГСМ\n\nДата: {total[1]}\n\nВид  | Стоимость (сом.л) \n\nАИ92 | {total[4]}\n\nАИ95 | {total[5]}\n\n  ДТ | {total[6]}"
 


#print(get_url_rosneft())

# def get_url():
#   url = "http://www.gazprom-neft.kg/article/fuel-price"
#   res = requests.get(url)
#   html_doc = res.text
#   soup = BeautifulSoup(html_doc, 'html.parser')
#   soup = soup.find('div', {'class': 'digit-group f95g'})
#   result = soup
#   for i in result:
#       print (i)
#   return result
 


# print(get_url())
"""
def get_url_gazprom():
  url = "http://www.gazprom-neft.kg/article/fuel-price"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'digit-group f95g'})
  result = soup
  t1 = re.findall("[0-9]", str(result))
  t = "".join(t1)
  t95 = f"G-Drive AN{t[0:2]} | {t[2:4]}.{t[4:6]}"
  return t95
 
print(get_url_gazprom())

def get_url_gazprom_all():
  lis = []
  lis_final = []
  url = "http://www.gazprom-neft.kg/article/fuel-price"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'prices-box'})
  # result = soup
  # t1 = re.findall("[0-9]", str(result))
  # t = "".join(t1)
  # t95 = f"G-Drive AN{t[0:2]} | {t[2:4]}.{t[4:6]}"
  # return t95

  res1 = str(soup)
  dict_price = {"f92g":"G-Drive AN92", "f95g\n":"G-Drive AN95", "f98":"AN98", "f92":"AN92", "f95":"AN95", "fdw":"Дизель Зима", "fd":"Дизель", "d1": 1, "d2": 2, "d3": 3, "d4\n": 4, "d5\n": 5, "d6": 6, "d7": 7, "d8\n": 8, "d9": 9, "d0": 0, "":"", "\n":" " }
  fin1 = res1.replace("<div class=", "")
  fin1.replace("<!-- <img src=http://www.gazprom-neft.kg/themes/gazprom-new/assets/images/posts-partials/price/stella.png --", "")
  fin2 = fin1.replace("</div>", "")
  fin2 = fin1.replace(">", "")
  fin3 = fin2.replace("</div", "")
  fin4 = fin3.replace("sp", " ")
  fin5 = fin4.replace("digit", "")
  fin6 = fin5.replace("\"", "").strip()
  fin7 = fin6.replace("<!-- <img src=http://www.gazprom-neft.kg/themes/gazprom-new/assets/images/posts-partials/price/stella.png --", "")
  fin8 = fin7.replace("prices-box\nbg\n", "")
  fin10 = fin8.replace("n-group", "")
  fin11 = (fin10.strip()).split(" ")
  # for i in fin11:
  #     o = dict_price[i]
  #     print(o)

  for i in soup:
      lis.append(i)
  return lis[5], lis[7], lis[9], lis[11], lis[13], lis[17], lis[21]


print(get_url_gazprom_all())
"""

# def get_url_oc():
#   url = "https://oc.kg/"
#   res = requests.get(url)
#   html_doc = res.text
#   soup = BeautifulSoup(html_doc, 'html.parser')
#   soup = soup.find('div', {'class': 'menu'})
#   result = soup
#   return result, html_doc

# print(get_url_oc())




# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup as soup

# url = 'https://oc.kg/'

# req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

# webpage = urlopen(req).read()
# page_soup = soup(webpage, "html.parser")
# title = page_soup.find("title")
# print(title)


def get_url_gazprom_all():
  lis = []
  lis_final = []
  url = "http://www.gazprom-neft.kg/article/fuel-price"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'prices-box'})
  res1 = str(soup)
  fin1 = res1.replace("</div>", "")
  # fin2 = fin1.replace("<div class=\"digit", "")
  fin2 = fin1[154:]
  # fin3 = fin2.replace("\">", "")
  # fin4 = fin3.replace("<div class=\"", "")
  # fin5 = fin4.replace("  ", "")
  fin3 = fin2.replace("\n", "")
  fin4 = fin3.replace("\">", "")
  fin5 = fin4.replace("<div class=\"digit", "")
  fin6 = fin5.replace("<div class=\"sp", " .")
  fin7 = (fin6.replace("d", "")).replace(" ", "")
  fin8 = (fin7.replace("f95g", "G-Drive AN95 ")).replace("f92g", "G-Drive AN92 ")
  fin9 = (fin8.replace("f95", "AN95 ")).replace("f92", "AN92 ")
  fin10 = fin9.replace("f98", "AN98 ")
  
  # fin10 = (fin9.replace("f", "Diesel ")).replace("fw", "Diesel Winter ")
  # fin11 = fin10.replace("gaz", "Gas Auto ")


  # fin12 = fin11.split("-group")
  fin12 = fin10.split("-group")
  d1, d2, d3, d4, d5 = fin12[1], fin12[2], fin12[3], fin12[4],fin12[5]
  d7 = "".join(fin12[7]).replace("f", "Diesel ")
  d8 = "".join(fin12[8]).replace("fw", "Diesel Winter ")
  d9 = "".join(fin12[9]).replace("fgaz", "Auto Gaz ")


  return f"Цены на ГСМ и Газ в GazProm Neft Bishkek \n\n {d1}\n {d2}\n {d3}\n {d4}\n {d5}\n {d7}\n {d8}\n {d9} \n Цены c сайта {url}"


#print(get_url_gazprom_all())

def get_url_gazprom_all_final():
  url = "http://www.gazprom-neft.kg/article/fuel-price"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'prices-box'})
  res1 = str(soup)
  fin1 = res1.replace("</div>", "")
  fin2 = fin1[154:]
  fin3 = fin2.replace("\n", "")
  fin4 = fin3.replace("\">", "")
  fin5 = fin4.replace("<div class=\"digit", "")
  fin6 = fin5.replace("<div class=\"sp", " .")
  fin7 = (fin6.replace("d", "")).replace(" ", "")
  fin8 = (fin7.replace("f95g", "G-Drive AN95 ")).replace("f92g", "G-Drive AN92 ")
  fin9 = (fin8.replace("f95", "AN95 ")).replace("f92", "AN92 ")
  fin10 = fin9.replace("f98", "AN98 ")
  fin12 = fin10.split("-group")
  d1, d2, d3, d4, d5 = fin12[1], fin12[2], fin12[3], fin12[4],fin12[5]
  d7 = "".join(fin12[7]).replace("f", "Diesel ")
  d8 = "".join(fin12[8]).replace("fw", "Diesel Winter ")
  d9 = "".join(fin12[9]).replace("fgaz", "Auto Gaz ")
  return f"Цены на ГСМ и Газ в GazProm Neft Bishkek \n\n {d1}\n {d2}\n {d3}\n {d4}\n {d5}\n {d7}\n {d8}\n {d9} \n\n Цены c сайта {url}"


#print(get_url_gazprom_all_final())



def get_url_partner_neft():
  url = "http://partner-neft.kg/"
  user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
  res = requests.get(url, headers=user_agent, timeout= 2.50)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'id': 'tab-1'})
  lis1 = soup.get_text()
  lis2 = lis1.strip()
  lis3 = lis2.replace("\t", "")
  lis4 = lis3.split("\n")
  lis5 = [i for i in lis4 if i]
  return f"Цены на ГСМ и Газ Партнер Нефть Бишкек \n\n {lis5[0]} | {lis5[1]}\n {lis5[2]} | {lis5[3]}\n {lis5[4]} | {lis5[5]}\n {lis5[6]} | {lis5[7]}\n {lis5[8]} | {lis5[9]}\n {lis5[10]}| {lis5[11]}\n\n Цены c сайта {url}"
 

#print(get_url_partner_neft())

