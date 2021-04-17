import urllib
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup as bs
import os
import getpass
import re
from pynput.keyboard import Key, Controller

# simulateur credit
def bnacreditsDirects(wd):
    montant = wd.find_element_by_id("montant")
    duree = wd.find_element_by_xpath('//*[@id="slider_duree"]/span')
    date_pre_echeance = wd.find_element_by_xpath('//*[@id="date_echeance"]')
    periodicite = wd.find_element_by_name("periodicite")
    # Clear the fields
    date_pre_echeance.clear()
    montant.clear()

    # find element username and password for inputting login info
    wd.find_element_by_xpath('//*[@id="horizontalTab"]/div/h2[1]').click()
    produit = Select(wd.find_element_by_id("produit"))

    date_pre_echeance.clear()


    # Ask user for the information
    bna_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bna_montant)
    bna_date_echeance = getpass.getpass("SVP enter date d'echeance* ")
    date_pre_echeance.send_keys(bna_date_echeance)
    bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    duree.send_keys(bank_duree)
    wd.find_element_by_xpath( '//*[@id="envoyer"]').click()

    time.sleep(5)
    time.sleep(5)
    time.sleep(5)
    return
def  banacreditsPlacement(wd) :
    return
def banacreditsCompagnes(wd) :
    return
def banacreditsACourtTerme(wd) :
    return
def CertifivatDeDepot(wd) :
    return


def numbers_to_months(argument):
    switcher = {
        1: "",
        2: "two",
        3: "",
        4: "fothreeur",
        5: "five",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print (func())


def main():
    DRIVER_PATH = 'C:/Users/NBH/Downloads/chromedriver.exe'
    wd = webdriver.Chrome(executable_path = DRIVER_PATH)
    wd.get('http://www.bna.tn/fr/simulateurs.189.html')
    time.sleep(5)

    print("Crédits Directs (PRETS PERSO-AUTO-IMMO)")
    wd.find_element_by_xpath('//*[@id="section_produits"]/div/div/div/div[2]/div[1]/div/div[3]/a').click()
    montant = wd.find_element_by_id("montant")
    duree = wd.find_element_by_xpath('//*[@id="slider_duree"]/span')
    date_pre_echeance = wd.find_element_by_xpath('//*[@id="date_echeance"]')
    periodicite = wd.find_element_by_name("periodicite")
    # Clear the fields

    # find element username and password for inputting login info
    wd.find_element_by_class_name('resp-arrow').click()
    produit = Select(wd.find_element_by_id("produit"))



    # Ask user for the information
    bna_montant = getpass.getpass("SVp entrer le  Montant du prêt souhaité (FCFA)")
    montant.send_keys(bna_montant)
    bna_date_echeance = getpass.getpass("SVP enter date d'echeance* ")
    date_pre_echeance.send_keys(bna_date_echeance)
    # bank_duree = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    # duree.send_keys(bank_duree)
    slider = wd.find_element_by_xpath('//*[@id="slider_duree"]')
    output = wd.find_element_by_xpath('//*[@id="duree"]')
    slid = getpass.getpass("SVP enter Durée de remboursement (Mois) ")
    print(output)
    wd.find_element_by_xpath( '//*[@id="envoyer"]').click()

    # elif wd.find_element_by_xpath('//*[@id="section_produits"]/div/div/div/div[2]/div[2]/div/div[3]/a').click() :
    #     banacreditsPlacement(wd)
    # elif wd.find_element_by_xpath('//*[@id="section_produits"]/div/div/div/div[2]/div[3]/div/div[3]/a').click() :
    #     banacreditsCompagnes(wd)
    # elif wd.find_element_by_xpath('//*[@id="section_produits"]/div/div/div/div[2]/div[4]/div/div[3]/a').click() :
    #     banacreditsACourtTerme(wd)
    # elif wd.find_element_by_xpath('//*[@id="section_produits"]/div/div/div/div[2]/div[5]/div/div[3]/a').click() :
    #     CertifivatDeDepot(wd)
    # wd.find_elements_by_xpath('//*[@id="fieldname1_2"]')
    # pd = wd.find_element_by_id("fieldname1_2")
    # print("la resultat est :")
    # print(pd.text)
    # print("Opss !! la resultat est vide ")


if __name__ == "__main__":
    main()