import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import os
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def credit(wd):
    credit1 =wd.find_element_by_xpath('//*[@id="theselectsimu"]/div/div/div[1]/a')
    wd.execute_script("arguments[0].click();", credit1)
    wd.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/div[1]/a').click()

    credit12 =wd.find_element_by_xpath('//*[@id="thesimu"]/div/div/div[1]/div/div[1]/div[2]/a')
    wd.execute_script("arguments[0].click();", credit12)
    # # find element username and password for inputting login info
    tauxNominal = wd.find_element_by_xpath('//*[@id="email"]')
    montant = wd.find_element_by_xpath('//*[@id="pass"]')
    duree = wd.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div[7]/div[1]/div/div/div/input')
    # Clear the fields
    tauxNominal.clear()
    montant.clear()
    duree.clear()
    # Ask user for the information
    bank_interet = getpass.getpass("SVP enter Taux d'intérêt (%)* ")
    tauxNominal.send_keys(bank_interet)
    bank_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité  inferieur a 5000000TND(FCFA)")
    montant.send_keys(bank_montant) 
    # bank_duree = getpass.getpass("SVP enter Durée de remboursement (ans) ")
    # duree.send_keys(bank_duree)

    time.sleep(5)

    # wd.find_element_by_xpath("//button[@type='submit']").click()
    # time.sleep(5)
    # time.sleep(5)
    return




def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('https://www.ubci.tn/particuliers/outils-et-guides/credit-conso/##str_content/')
    time.sleep(5)
    credit(wd)
    # resultat = wd.find_element_by_name("fieldname1_2")
    res = wd.find_element_by_xpath('')
    print("la resultat est :")
    print(res.text)
    print("Opss !! la resultat est vide ")


if __name__ == "__main__":
    main()