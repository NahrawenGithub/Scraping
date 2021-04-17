import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import os
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit

def credit(wd, i):
    wd.get('http://m.attijaribank.com.tn/Fr/Simulateur_58_216_'+i)
    # find element username and password for inputting login info
    montant = wd.find_element_by_xpath('/html/body/div[2]/form[2]/div[1]/div/input')
    duree = wd.find_element_by_xpath('/html/body/div[2]/form[2]/div[2]/div/input')
    # Clear the fields
    print(duree)
    print(montant)
# Ask user for the information
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bank_montant)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    duree.send_keys(bank_duree)

    time.sleep(5)
    wd.find_element_by_xpath('/html/body/div[2]/form[2]/input[2]').click()
    res =wd.find_element_by_xpath('/html/body/div[2]/div[1]')
    print("la resultat est : ")
    print(res.text)
    time.sleep(5)
    # time.sleep(5)
    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('http://m.attijaribank.com.tn/Fr/Simulateur_58_216')
    select = Select(wd.find_element_by_xpath('//*[@id="credit"]'))
    time.sleep(5)
    print("Bonjour !   ")
    print("1/CREDEX (crédit à la consommation) (<Duree<) 	")
    print("2/TAHSSIN (crédit aménagement)(<Duree<) 	")
    print("3/CREDITAU NEUVE (<Duree<) 	")
    print("4/CREDITAU OCCASION (<Duree<) 	")
    print("5/Crédits immobiliers MEFTAH	(<Duree<) ")
    a = int (input("choisir un type de credit "))
    time.sleep(5)
    if a == 1 :
        select.select_by_index(1)
        credit(wd, "1")
    elif a == 2 :
        select.select_by_index(2)
        credit(wd, "2")
    elif a == 3 :
        select.select_by_index(3)
        credit(wd, "3")
    elif a == 4 :
        select.select_by_index(4)
        credit(wd,"4")
    elif a == 5 :
        select.select_by_index(5)
        credit(wd,"6")


if __name__ == "__main__":
    main()