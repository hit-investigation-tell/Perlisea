import os
import time
import urllib
import requests
from bs4 import BeautifulSoup
from terminaltables import SingleTable
import requests
import sys
import colorama
from colorama import init, Fore,  Back,  Style

author = ("Authors")
warning = ("WARNING")
agree = ("AGREE")
error = ("ERROR")
version = ("Version")
name = ("UrxuDotCom#8468")
answ = ("$")
un = ("1")
deux = ("2")
trois = ("3")
quatre = ("4")
cent = ("100")
star = ("*")	

def Search(personne,Ville,url):
	if url == ("https://www.pagesjaunes.fr/recherche/") or ("https://www.infoannuaire.fr/res/search?q="):
		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Recherche pour ( " + personne + " à "+ Ville +" ) en cours ....")
	else:
		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Recherche de ( " + personne + "  ) en cours ....")
	headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
			'referrer': 'https://google.com',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'utf-8',
			'Accept-Language': 'en-US,en;q=0.9',
			'Pragma': 'no-cache'
		}
	if url == ("https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="):

		url=("https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="+personne+"&ou="+Ville+"&proximite=0")
		requete = requests.get(url, headers=headers)
		page = requete.content
		features="html.parser"
		soup = BeautifulSoup(page)	
		try:
			nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
			addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
			numList = soup.find_all("strong", {"class": "num"})

		except AttributeError:
			pass

		namesList2 = []
		addressesList2 = []
		numesList2 = []
		operatorList = []

		# try:
		for name in nameList:
			namesList2.append(name.text.strip())
		for addresse in addressList:
			addressesList2.append(addresse.text.strip())
		for num in numList: 
			numesList2.append(num.text.strip())

		regroup = zip(namesList2,addressesList2,numesList2)
		
		title = " Particulier "

		TABLE_DATA = [
			('Name', 'Adresse', 'Phone'),
		]

		listeInfos = []

		for infos in regroup:
			
			try:

				TABLE_DATA.append(infos)

			except AttributeError:
				pass

		table_instance = SingleTable(TABLE_DATA, title)
		url=("https://www.infoannuaire.fr/res/search?q="+personne+"&w="+Ville)
		requete = requests.get(url, headers=headers)
		page = requete.content
		features="html.parser"
		soup = BeautifulSoup(page)	
		try:
			nameList = soup.find_all("div", {"class": "nom-prenom__response"})
			addressList = soup.find_all("div", {"class": "adresse__response"})



		except AttributeError:
			pass

		namesList2 = []
		addressesList2 = []


		# try:
		for name in nameList:
			namesList2.append(name.text.strip())
		for addresse in addressList:
			addressesList2.append(addresse.text.strip())

		

		regroup = zip(namesList2,addressesList2)
		
		title = " Particulier "

		TABLE_DATA = [
			('Name', 'Adresse'),
		]

		listeInfos = []

		for infos in regroup:
			
			try:

				TABLE_DATA.append(infos)

			except AttributeError:
				pass

		table_instance1 = SingleTable(TABLE_DATA, title)
		if sys.platform == 'linux2':
				os.system('clear')

		elif sys.platform == 'win32':
				os.system('cls')

		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Resultat ...")
		print("\n"+table_instance.table)
		print("\n"+table_instance1.table)
		input(":"+ Fore.RED + answ + Fore.RESET + "> Press [ENTER] to go back to main menu :")




	else:
		headers = {
				'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
				'referrer': 'https://google.com',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Encoding': 'utf-8',
				'Accept-Language': 'en-US,en;q=0.9',
				'Pragma': 'no-cache'
			}
		url=(url+personne)
		requete = requests.get(url, headers=headers)
		page = requete.content
		features="html.parser"
		soup = BeautifulSoup(page)	
		try:
			nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
			addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
			numList = soup.find_all("strong", {"class": "num"})
		except AttributeError:
			pass

		namesList2 = []
		addressesList2 = []
		numesList2 = []
		operatorList = []

		# try:
		for name in nameList:
			namesList2.append(name.text.strip())
		for addresse in addressList:
			addressesList2.append(addresse.text.strip())
		for num in numList: 
			numesList2.append(num.text.strip())

		regroup = zip(namesList2,addressesList2,numesList2)
		
		title = " Particulier "

		TABLE_DATA = [
			('Name', 'Adresse', 'Phone'),
		]

		listeInfos = []

		for infos in regroup:
			
			try:

				TABLE_DATA.append(infos)

			except AttributeError:
				pass

		table_instance = SingleTable(TABLE_DATA, title)
		if sys.platform == 'linux2':
				os.system('clear')

		elif sys.platform == 'win32':
				os.system('cls')

		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Resultat pour ( " + personne + " à "+ Ville +" ) en cours ....")
		print("\n"+table_instance.table)
		input(":"+ Fore.RED + answ + Fore.RESET + "> Press [ENTER] to go back to main menu :")
