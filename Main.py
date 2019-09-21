import requests
from bs4 import BeautifulSoup

				# эмуляция действия браузера
headers = {'accept': '*/*',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
} 
base_url = 'https://kolesa.kz/cars/aktobe/?price[to]=7500000&year[from]=2012&page=2'

#	https://kolesa.kz/cars/aktobe/?price[to]=7%20500%20000&year[from]=2012
#	https://kolesa.kz/cars/aktobe/?price[to]=7500000&year[from]=2012&page=2

def Kolesa_parser(base_url, headers):
	session = requests.Session()
	request = session.get(base_url, headers=headers)
	if request.status_code == 200:
								# poluchenie dannyh
		soup = BeautifulSoup(request.content, 'html.parser')
		div_blue = soup.find_all('div', attrs={'class': 'row vw-item list-item blue a-elem'})
		div_yellow = soup.find_all('div', attrs={'class': 'row vw-item list-item yellow a-elem'})
		div_obi4 = soup.find_all('div', attrs={'class': 'row vw-item list-item a-elem'})
		div_red = soup.find_all('div', attrs={'class': 'row vw-item list-item red a-elem'})
								# vitaskivaem id

		
		blue_adv_id = [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item blue a-elem'})]
		yellow_adv_id = [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item yellow a-elem'})]
		obi4_adv_id = [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item a-elem'})]
		red_adv_id = [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item red a-elem'})]
		
		print(len(div_blue))
		print(len(div_yellow))
		print(len(div_obi4))
		print(len(div_red))

		print(blue_adv_id)
		print(yellow_adv_id)
		print(obi4_adv_id)
		print(red_adv_id)

		print(1)
	else:
		print('ERROR')


def Opening(adv_id):
	session = requests.Session()
	url_inside='https://kolesa.kz/a/show/'
	request = session.get(url_inside+adv_id, headers=headers)

	if request.status_code == 200:
		soup = BeautifulSoup(request.content, 'html5lib')
		deshevle = soup.find_all('span', class_='kolesa-score-label cheaper')


		

		#div_blue = soup.find_all('div', attrs={'class': 'row vw-item list-item blue a-elem'})

		print(deshevle)

Kolesa_parser(base_url, headers)
#Opening(str(96563049))