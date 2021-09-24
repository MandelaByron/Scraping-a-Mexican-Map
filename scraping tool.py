
from selenium import webdriver
import time
#import pygsheets
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#import mysql.connector
import gspread
Cueta_catastral=[]
Calle_Numero=[]
Colonia=[]
Codigo_Postal=[]
Superficie=[]
Uso_suelo=[]
Niveles=[]
Altura=[]
Area_libre=[]
Min_Vivienda=[]
Densidad=[]
Superficie=[]
Sup_Max_const=[]
Num_Viviendas=[]
Urls=[]
Delegations=[]
Colonias=[]
Calles=[]
Page_Links=[]


options=Options()
options.add_argument("--headless")
def save_to_google_sheets_(to_add):
    gc=gspread.service_account(filename="jaimescraper-creds.json")
    #sh=gc.open_by_key("1DsmpQ0TOlGLesZc6dvu5nc4ZEqed0fVDm-5pT_KcJPA")
    sh=gc.open_by_url("https://docs.google.com/spreadsheets/d/118KNSA4WvHnGelsQipG-Cf7x7fDMvWs6xRbf1pD1x2s/edit#gid=0")
    worksheet=sh.get_worksheet(0)
    worksheet.append_rows(to_add)

#driver=webdriver.Chrome("chromedriver.exe")

driver=webdriver.Chrome("chromedriver.exe")
driver.get("http://ciudadmx.cdmx.gob.mx:8080/seduvi/")
driver.find_element_by_xpath("//img[contains(@src,'seduviDiseno/Imagen2.png')]").click()
delegation=driver.find_element_by_xpath("//select[contains(@name,'delegacion')]")
choice1=Select(delegation)
choice1.select_by_value("cAzcapotzalco")
driver.implicitly_wait(10)
colnies=driver.find_elements_by_xpath("//select[contains(@name,'colonia')]/option")
print(len(colnies))

driver.implicitly_wait(10)
for i in range(1,len(colnies)):
    colony=driver.find_element_by_xpath("//select[contains(@name,'colonia')]")
    choice2=Select(colony)
    choice2.select_by_index(i)
    choice2=Select(colony)
    selected_option_1=choice2.first_selected_option
    for j in range(1,len(driver.find_elements_by_xpath("//select[contains(@name,'calle')]/option"))):
        calle=driver.find_element_by_xpath("//select[contains(@name,'calle')]")
        choice3=Select(calle)
        choice3.select_by_index(j)
        choice3=Select(calle)
        selected_option=choice3.first_selected_option
        print(selected_option.text)
        for n in range(1,len(driver.find_elements_by_xpath("//select[contains(@name,'numeroCalle')]/option"))):
            #driver.implicitly_wait(10)
            try:
                #choice1=Select(delegation)
                choice1.select_by_value("cAzcapotzalco")
                ##driver.implicitly_wait(10)
                colony=driver.find_element_by_xpath("//select[contains(@name,'colonia')]")
                choice2=Select(colony)
                choice2.select_by_value(selected_option_1.text)
                calle=driver.find_element_by_xpath("//select[contains(@name,'calle')]")
                choice3=Select(calle)
                choice3.select_by_value(selected_option.text)
            except:
                pass
            try:
                numero=driver.find_element_by_xpath("//select[contains(@name,'numeroCalle')]")
                choice4=Select(numero)
                choice4.select_by_index(n)
            except:
                pass
            try:
                frame=driver.find_element_by_xpath("(//iframe[contains(@id,'mapa')])[2]")
                driver.switch_to.frame(frame)
                driver.find_element_by_xpath('//*[@id="divEtiqueta0"]/div/table/tbody/tr/td/div/table/tbody/tr[6]/td/a').click()
        
                tabs=driver.window_handles
                driver.switch_to.window(tabs[1])
                #print(driver.current_url)
                Urls.append(driver.current_url)
                driver.switch_to.window(tabs[0])
                #driver.refresh()
            except:
                pass

print(len(Urls),"Links to be scraped\n\n")

    
        


    
                    

        
    



  






                    
                        

                        
                
                      

                
def scrapping():

    
    time.sleep(1)
    try:
        cuenta_catastral=driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]")
        Cueta_catastral.append(cuenta_catastral.text)
        #print(cuenta_catastral.text)
    except:
        Cueta_catastral.append("N/A")


    try:
        calle_numero=driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]")
        Calle_Numero.append(calle_numero.text)
        #print(calle_numero.text)
    except:
        Calle_Numero.append("N/A")
    try:
        colonia=driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]")
        Colonia.append(colonia.text)
        #print(colonia.text)
    except:
        Colonia.append("N/A")
    try:
        postal=driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]")
        Codigo_Postal.append(postal.text)
        #print(postal.text)
    except:
        Codigo_Postal.append("N/A")
    
    try:
        superficie_predio=driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]")
        Superficie.append(superficie_predio.text)
        #print(superficie_predio.text
    except:
        Superficie.append("N/A")


    try:
        uso_suelo=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:194px;']")
        Uso_suelo.append(uso_suelo.text)
        #print(uso_suelo.text)
    except:
        Uso_suelo.append("N/A")
    try:
        niveles=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:152px;']")
        Niveles.append(niveles.text)
        #print(niveles.text)
    except:
        Niveles.append("N/A")
    try:
        altura=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:44px;']")
        Altura.append(altura.text)
        #print(altura.text)
    except:
        Altura.append("N/A")
    try:
        area_libre=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:49px;']")
        Area_libre.append(area_libre.text)
        #print(area_libre.text)
    except:
        Area_libre.append("N/A")
    try:
        m2_min=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:62px;']")
        Min_Vivienda.append(m2_min.text)
        #print(m2_min.text)
    except:
        Min_Vivienda.append("N/A")
    
    

    try:
        densidad=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:59px;']")
        Densidad.append(densidad.text)
        #print(densidad.text)
    except:
        Densidad.append("N/A")
    try:
        sup_max_construccion=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:91px;']")
        Sup_Max_const.append(sup_max_construccion.text)
        #print(sup_max_construccion.text)
    except:
        Sup_Max_const.append("N/A")
    try:
        num_viviendas=driver.find_element_by_xpath("//tbody/tr/td[@class='zon' and @style='width:99px;']")
        Num_Viviendas.append(num_viviendas.text)
        #print(num_viviendas.text)
    except:
        Num_Viviendas.append("N/A")

    Page_link=driver.current_url
    Page_Links.append(Page_link)

for link in Urls:
    driver.get(link)
    scrapping()
    print("scraping")
    time.sleep(1)

data=zip(Cueta_catastral,Calle_Numero,Colonia,Codigo_Postal,Superficie,Uso_suelo,Niveles,Altura,Area_libre,Min_Vivienda,Densidad,Sup_Max_const,Num_Viviendas,Page_Links)
final_data=list(data)            
save_to_google_sheets_(to_add=final_data)
print("Scraping Complete. Check the Google sheet for entered data")


                   



                    
                    
    
    


    
 
    
       

                

                



    

                     



                    




            


    