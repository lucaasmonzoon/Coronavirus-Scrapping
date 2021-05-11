from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(r.text,features="html.parser")
total=[]

def casostotales():
    elements = soup.find_all(id="maincounter-wrap")
    #print(elements)
    for elementos in elements:
        
        if elementos.find("h1").text=="Coronavirus Cases:":
            CasosTotaless=elementos.find("span").text
            total.append(elementos.find("span").text)

        if elementos.find("h1").text=="Deaths:":
            total.append(elementos.find("span").text)
        
        if elementos.find("h1").text=="Recovered:":
            total.append(elementos.find("span").text)
    
    
    
    
def ArgentinaCasos():

    paises=soup.find_all('tr')
    #print(paises)
    b=0
    for pais in paises:
        nombre=pais.find("a",{"class":"mt_a"})
        if nombre != None:
            if nombre.text=="Argentina" and b==0:
                b=+1
                

                aux=pais.find_all("td")
                totalCasos=aux[2]
                return(aux)
                
            

info=ArgentinaCasos()
casostotales()
print("En el mundo: \nCasos:",total[0],"\nMuertes:",total[1],"\nRecuperados:",total[2])
print("En argentina: \nCasos:",info[2].text,"\nMuertes:",info[4].text,"\nRecuperados:",info[6].text)
  
    
    
    


    



    




