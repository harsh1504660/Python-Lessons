from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
   city = city.replace(" ", "+")
 
   try:
       res = requests.get(
           f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
      
       print("Loading...")
 
       soup = BeautifulSoup(res.text, 'html.parser')
       location = soup.select('#wob_loc')[0].getText().strip()
       time = soup.select('#wob_dts')[0].getText().strip()
       info = soup.select('#wob_dc')[0].getText().strip()
       temperature = soup.select('#wob_tm')[0].getText().strip()
 
       print("Location: " + location)
       print("Temperature: " + temperature + "&deg;C")
       print("Time: " + time)
       print("Weather Description: " + info)
   except:
       print("Please enter a valid city name")
print("enter the city name")
city=input()
city=city+" weather"
    
weather(city)