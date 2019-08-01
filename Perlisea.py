#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author 7up#0001 and UrxuDotCom#8468 aka @perlise._ (instagram)


import os
import time
import urllib
import requests
from bs4 import BeautifulSoup
from terminaltables import SingleTable
import requests
import sys
import colorama
from modules import *
from colorama import init, Fore,  Back,  Style

r = requests.get("https://www.youtube.com")
print(r.text)

print("\r")
print("\r")
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
#bannière

def retourmenu():
	if sys.platform == 'linux2':
				os.system('clear')

	elif sys.platform == 'win32':
		os.system('cls')
	print("\r")
	print("\r")

	print("                                          _________________________")
	print("    _ \          | _)                    | {"+Fore.YELLOW + Style.BRIGHT + version +Fore.RESET+"}: 1.0.0        |")
	print("    __/ -_)   _| |  | (_-<   -_)   _` |  | {" + Fore.BLUE + Style.BRIGHT + author + Fore.RESET + "}: Perlise, 7up | ")
	print("   _| \___| _|  _| _| ___/ \___| \__,_|  |_________________________|")
	print("                                      ")

	print(" |!|" + Fore.WHITE + Back.RED + Style.BRIGHT + warning + Back.RESET + Fore.RESET +"|!| I am not responsible of your actions |!|"+ Fore.WHITE + Back.RED + warning + Fore.RESET + Back.RESET +"|!|")
	print("\r")
	print("["+ Fore.YELLOW + un + Fore.RESET + "] - Name Search")
	print("["+ Fore.YELLOW + deux + Fore.RESET + "] - Phone Search (use fax for best results)")
	print("["+ Fore.YELLOW + trois + Fore.RESET + "] - Username Search")
	print("["+ Fore.YELLOW + quatre + Fore.RESET + "] - Join our discord server")
	print("\r")
	print("["+ Fore.YELLOW + cent + Fore.RESET +"] - Clear Terminal")
	print("\r")
	choice = input(":"+ Fore.RED + answ + Fore.RESET + "> ")



	#MENU


	if choice == "1":

		Ville = input("Ville : ")
		personne = input("Personne : ")
		url = ("https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=")
		Search(personne,Ville,url)
		retourmenu()

		#debut code person seach
	elif choice == "2":
		num = input("Search a phone number : ")
		Search(num,"rien","https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui=")
		time.sleep(1.0)
		retourmenu()
		

	elif choice == "3":
		id = input("Search an username : ")
		print("\n["+ Fore.MAGENTA + star + Fore.RESET + "] Searching for ( "+ id +" ) in progress ...")
		time.sleep(1.0)
		#debut code username search
	elif choice == "4":
		print("Invitation : https://discord.gg/Zu76Wfp")
		input("[*]>> Retournez au menu !")
		retourmenu()
	elif choice == "100":
		retourmenu()
	else:
		print("|!| "+ Fore.WHITE + Back.RED + error + Fore.RESET + Back.RESET +" |!| Type a correct number ...")

		time.sleep(2.0)
		if sys.platform == 'linux2':
			os.system('clear')

		elif sys.platform == 'win32':
			os.system('cls')
		retourmenu()
retourmenu()	