import requests 
from bs4 import BeautifulSoup 
import threading

																		# эмуляция действия браузера 

base_url = 'https://kolesa.kz/cars/aktobe/?price[to]=7500000&year[from]=2012' 
headers = {'accept': '*/*', 
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' 
} 
counter = 0
# https://kolesa.kz/cars/aktobe/?price[to]=7%20500%20000&year[from]=2012 
# https://kolesa.kz/cars/aktobe/?price[to]=7500000&year[from]=2012&page=2 

def Kolesa_parser(base_url, headers, total_page_number,shag_cicla,start_cicla): 
	
																				#loops for next page
	for page in range(start_cicla, int(total_page_number),shag_cicla):
		session = requests.Session() 
		request = session.get(base_url+str(page), headers=headers) 
		if request.status_code == 200: 
																				# getting datas
			soup = BeautifulSoup(request.content, 'lxml') 
			#div_blue = soup.find_all('div', attrs={'class': 'row vw-item list-item blue a-elem'}) 
			#div_yellow = soup.find_all('div', attrs={'class': 'row vw-item list-item yellow a-elem'}) 
			#div_obi4 = soup.find_all('div', attrs={'class': 'row vw-item list-item a-elem'}) 
			#div_red = soup.find_all('div', attrs={'class': 'row vw-item list-item red a-elem'}) 
																				# extracting id 

			blue_adv_id    	 =	 [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item blue a-elem'})] 
			yellow_adv_id	 = 	 [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item yellow a-elem'})] 
			regular_adv_id	 = 	 [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item a-elem'})] 
			red_adv_id 		 = 	 [str(div.find('a')['data-product-id']) for div in soup.find_all('div', attrs={'class': 'row vw-item list-item red a-elem'})] 
			for a in range(len(blue_adv_id)):
				Opening(blue_adv_id[a],"blue")
			for a in range(len(yellow_adv_id)):
				Opening(yellow_adv_id[a],"yellow")
			for a in range(len(regular_adv_id)):
				Opening(regular_adv_id[a],"regular")
			for a in range(len(red_adv_id)):
				Opening(red_adv_id[a],"red")
			print("next page")
			global counter
			counter = counter + len(blue_adv_id)+len(yellow_adv_id)+len(regular_adv_id)+len(red_adv_id)
			print("на данный момент ботом просмотренно " + str(counter) + " обьявлении")
		else: 
			print('ERROR') 
		



def Opening(adv_id,adv_type): 
	session = requests.Session() 
	url_inside='https://kolesa.kz/a/show/' 
	request = session.get(url_inside+adv_id, headers=headers) 

	if request.status_code == 200: 
		soup = BeautifulSoup(request.content, 'html5lib') 
		if (len(soup.find_all('span', class_='kolesa-score-label cheaper')) <= 0): #dorozhe ubiraet kazhetsya
			pass
		else:
			deshevle = soup.find_all('span', class_='kolesa-score-label cheaper')[0].text	
			advka = advertisement(soup,adv_type)
			splitting_only_number(deshevle,adv_id,advka)
			
			
def advertisement(soup,adv_type):
	total_characteristics =[]
	if (adv_type == "blue"):
		adv_brand = soup.find('span', itemprop='brand').text
		adv_name  = soup.find('span', itemprop='name').text
		adv_year  = soup.find('span', class_='year').text
		#splitting_only_number(deshevle,adv_id,blue_adv_brand,blue_adv_name,blue_adv_year)
		total_characteristics.append(adv_brand)
		total_characteristics.append(adv_name)
		total_characteristics.append(adv_year)
		total_characteristics.append("Быстро")
		return(total_characteristics)
	if(adv_type == "yellow"):
		adv_brand = soup.find('span', itemprop='brand').text
		adv_name  = soup.find('span', itemprop='name').text
		adv_year  = soup.find('span', class_='year').text
		#splitting_only_number(deshevle,adv_id,yellow_adv_brand,yellow_adv_name,yellow_adv_year)
		total_characteristics.append(adv_brand)
		total_characteristics.append(adv_name)
		total_characteristics.append(adv_year)
		total_characteristics.append("Турбо")
		return(total_characteristics)
	if(adv_type == "regular"):		
		adv_brand = soup.find('span', itemprop='brand').text
		try:
			adv_name  = soup.find('span', itemprop='name').text
		except AttributeError:
			adv_name = "без названия"
		
		adv_year  = soup.find('span', class_='year').text
		#splitting_only_number(deshevle,adv_id,regular_adv_brand,regular_adv_name,regular_adv_year)
		total_characteristics.append(adv_brand)
		total_characteristics.append(adv_name)
		total_characteristics.append(adv_year)
		total_characteristics.append("обычное")
		return(total_characteristics)
	if(adv_type == "red"):
		adv_brand = soup.find('span', itemprop='brand').text
		adv_name  = soup.find('span', itemprop='name').text
		adv_year  = soup.find('span', class_='year').text
		#splitting_only_number(deshevle,adv_id,red_adv_brand,red_adv_name,red_adv_year)	
		total_characteristics.append(adv_brand)
		total_characteristics.append(adv_name)
		total_characteristics.append(adv_year)
		total_characteristics.append("просто желтое")
		return(total_characteristics)	

def splitting_only_number(deshevle,adv_id,advka):
										#extracting only digits
	deshevle = deshevle.split(' ')
	deshevle = deshevle[13].split(' ')
	deshevle = deshevle[0]				#only digital value is here!
	deshevle = deshevle.split('%')
	deshevle =deshevle[0] 
	Calculation(deshevle,adv_id,advka)


def Calculation(deshevle,adv_id,advka):
	if float(deshevle) >= 20:							#---------------PROCENT TUUUUUUUUUUUT!!!!------------------------
		print("good idea "+ "https://kolesa.kz/a/show/"+str(adv_id) + "   " + str(advka[0]) + " " + str(advka[1]) + str(advka[2]) + "  хозяин продает машину в режиме - " + str(advka[3]))
	else:
		print("This is not best offer, i am trying to find smth better:)")

def main():
	base_url = 'https://kolesa.kz/cars/?auto-car-grbody=2&auto-custom=2&auto-car-transm=2345&auto-car-volume[to]=3&year[from]=2007&price[to]=8%20000%20000' 
	base_url = base_url + "&page="
	total_page_number = 300

	#Kolesa_parser(base_url,headers,total_page_number)
	'''
	a = threading.Thread(target=Kolesa_parser, args=(base_url,headers,total_page_number,3,1))
	b = threading.Thread(target=Kolesa_parser, args=(base_url,headers,total_page_number,3,2))
	c = threading.Thread(target=Kolesa_parser, args=(base_url,headers,total_page_number,3,3))
	a.start()
	b.start()
	c.start()
	'''
	threads = list()
	for index in range(1,11):
		x = threading.Thread(target=Kolesa_parser, args=(base_url,headers,total_page_number,3,1))
		threads.append(x)
		x.start()


if __name__ == '__main__':
    main()