#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     09/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import needed object
import re
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

def geturl(url):
    #get the url, return an object of type NoneType
    driver.get(url)
    return driver

def grouponResearch(driver):
    """
    Make a research in Groupon website and return currentUrl
    """
    #get the location field,return the object locationField of type selenium.webdriver.remote.webelement.WebElement
    locationField= driver.find_element_by_id('ls-location')
    #get the location field,return the object searchField of type selenium.webdriver.remote.webelement.WebElement
    searchField = driver.find_element_by_id('ls-search')
    #get the formular,return the object submit of type selenium.webdriver.remote.webelement.WebElement
    formular = driver.find_element_by_id('ls-search-form')
    #wait 3 secondes
    time.sleep(3)
    #fill the location field
    locationField.clear()
    locationField.send_keys(location)
    #wait 3 secondes
    time.sleep(3)
    searchField.clear()
    #fill the search field
    searchField.send_keys(search)
    #wait 3 secondes
    time.sleep(3)
    #excecute the search
    formular.submit()
    #wait 3 secondes
    time.sleep(3)
    #get current url, return the object currentUrl of type
    currentUrl = driver.current_url

    #return the object currentUrl
    return currentUrl

def grouponPageScrapper(driver,dealLinks):
    """
    Scrappe groupon website, take all links of pages, return a table with all links
    """

    actions = ActionChains(driver)
    while True :
        actions.send_keys(Keys.END).perform()
        #initialise the object index to 0
        index = 0
        #wait 3 secondes
        time.sleep(3)
        while True :
            #try
            try :
                #get all element a in all figure
                links = driver.find_elements_by_xpath("//div[@id='pull-cards']/figure/a")[index]
                #get the href of all element a
                figlink = links.get_attribute("href")
                #condition to verify if the href is not in the object dealinks
                if figlink not in dealLinks :
                    #add the object figlink in the object dealinks
                    dealLinks.append(figlink)
            except :
                #go out of the infinity loop
                break
            #increment the objet index to 1
            index += 1

        #wait 3 secondes
        time.sleep(3)
        #try
        try:
            #get the element with the link text Suivant, return the object nextButton
            nextButton = driver.find_element_by_link_text("Suivant")
            #execute the script of the object nextButton
            driver.execute_script("arguments[0].click();", nextButton)
        except :
            #go out of the infinity loop
            break
    #return the object dealLinks
    return dealLinks

def getDomainName(driver,linkTable):
    """
    Get merchant website in groupon, find their domain name, return a table with all domain name founds
    """
    link = ""
    #wait 3 secondes
    time.sleep(3)
    #try
    try :
        #get the element with class name merchant-website, return the object linkText
        linkText = driver.find_element_by_class_name("merchant-website")
        #get the href of the object linkText, return the object link of type str
        link = linkText.get_attribute('href')
        #delete http(s)://www. in the object link, return the object link of type str
        link = re.sub(r'http[s]?://\w{3}\.',"",link)
        if link :
            pass
        #delete http(s): in the object link, return the object link of type str
        link = re.sub(r'http[s]?:',"",link)
        if link :
            pass
        #delete www. in the object link, return the object link of type str
        link = re.sub(r'www.',"",link)
        if link:
            pass
        link = re.sub(r'fr.',"",link)
        if link:
            pass
        link = re.sub(r'//',"",link)
        if link:
            pass

        #condition to verify if the object link is in the object linkTable
        if link not in linkTable :
            #add the object link in the object linkTable
            linkTable.append(link)
    except :
        pass

    #return the object linkkTable
    return linkTable

def emailsFinder (valableLink,foundsEmails):
    """
    search email in the bing result website
    """
    valableLinktable.append(valableLink)
    foundsEmails.append("for www.{} we have founds : ".format(valableLink))
    #initialise the object pageNumber to 1, return an object of type int
    pageNumber = 1
    #put the url of the site into the object url of type str
    url = "https://www.bing.com/search?q=%40{}&first=1".format(valableLink,pageNumber)
    driver.get(url)
    emails = []
    emailSources = []
    output = []
    foundEmails = []

    pageNumber = 2
    #condition to run the program in infinity
    while  True :

        li_number = 0
        #condition to run the program in infinity
        while True:
            try:
                #get element with class name b_algo, return the object lipath
                lipath = driver.find_elements_by_class_name("b_algo")[li_number]
                #get the text of the object lipath; reutrn the object litext of typ str
                litext = lipath.text
                #for line in the drivertextclear
                for line in litext.splitlines():
                    #search all email in each line, return the objet searchNumbers of type list
                    searchEmails = re.findall(r"[a-zA-Z0-9\.\-\_]+@{}".format(valableLink),line, flags=re.MULTILINE)
                        #for email in email_1 list
                    if searchEmails:
                        #get elements with pacth h2/a, return the object apath
                        apath = driver.find_elements_by_xpath('//h2/a')[li_number]
                        #get the href of the object apath, return the object emailSource of type str
                        emailSource = apath.get_attribute("href")
                        for email in searchEmails:
                                # add email in the emails list: return an object oy type NoneType
                                emails.append(email)
                                # add emailSource in the object emailSources: return an object oy type NoneType
                                emailSources.append(emailSource)
                #increment the object li_number to 1
                li_number += 1
            except:
                break

        try:
            # look for the html tag that content a specific str number : return the object link of type str
            link = driver.find_element_by_link_text(str(pageNumber))
        # if an error occur
        except :
            #stop the while loop
            break
        #click of the link that is in the tag found in link : return an object of type NoneType
        link.click()
        #add 1 to the page number to have the number of the next pageL: return the object page_number of type int
        pageNumber += 1
    counter = 1

    for email,source in zip(emails,emailSources):
        foundEmails.append("{} {}".format(email,source))

    emails = []
    emailSources = []
    newEmails = []
    newEmailSources = []
    newCheck = []

    output = sorted(foundEmails)
    for items in output :
        emails.append(items.split(" ")[0])
        emailSources.append(items.split(" ")[1])

    index = 0
    for mail in emails:
        count = emails.count(mail)
        if mail not in newEmails:
            newEmails.append(mail)
            notDbleSources = []
            for elt in emailSources[index:index+count]:
                if elt not in notDbleSources :
                    notDbleSources.append(elt)
            newEmailSources.append(notDbleSources)
            index += count

    counter = 1
    for mail,source in zip(newEmails,newEmailSources):
        foundsEmails.append("{:<4} {:<30}".format(counter,mail))
        mails.append(mail)
        try :
            for elts in source :
                if elts[-1] :
                    foundsEmails.append("\t\tSource : {:<50}\n".format(elts))
                else :
                    foundsEmails.append("\t\tSource : {:<50}".format(elts))
            counter += 1
        except :
            pass

    return foundsEmails

def whriteInOuput(finalOutput):
    """
    Whrite the result in a file txt
    """

    os.chdir("D:/IIHT/Python/Project/Find lead business/groupon.fr/Ville et nom testé")
    lenEmail = len(mails)
    lenValidLinkTable = len(valableLinktable)
    pourcentage = (lenEmail*100) / lenValidLinkTable

    #open text file, return  an object of type io.TextIOWrapper
    with open("{}in{}.txt".format(search,location), "w") as writ:
        #write each line in the object op, return an object of type int
        writ.write("We have founds {} E-mails for {} links, {}% \n\n".format(lenEmail,lenValidLinkTable,pourcentage))
        writ.write('\n'.join(foundsEmails) + "\n")

#get the name to search, return an object of type str
search = input("Please enter the name : ")
#get the location, return an object of type str
location = input("PLease enter the location : ")

url = "https://www.groupon.fr/"

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option("prefs", prefs)
#initialise the object options with the options of chrome webdriver, return the object options of type selenium.webdriver.chrome.options.Options
options = Options()
#define the option of chrome webdriver,Returns whether or not the headless argument is set
options.headless = False
#create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver
driver = webdriver.Chrome(options=options,chrome_options=chromeOptions)
#driver.set_window_position(-3000, 0)

dealLinks = []
linkTable = []
mails = []
valableLinktable = []
driver = geturl(url)
currentUrl = grouponResearch(driver)
linksTable = grouponPageScrapper(driver,dealLinks)

for link in linksTable :
    driver = geturl(link)
    domainName = getDomainName(driver,linkTable)

foundsEmails = []
text = "Location : {} \n".format(location)
foundsEmails.append(text)
text = "Name : {}\n".format(search)
foundsEmails.append(text)

for link in domainName :
    try:
        valableLink = re.findall(r'[a-zA-Z0-9\-\@\.]+\.[a-zA-Z0-9]+', link)[0]
    except:
        pass
    if not re.findall('facebook',valableLink):
        foundsEmails = emailsFinder(valableLink,foundsEmails)

whriteInOuput(foundsEmails)
driver.quit()

