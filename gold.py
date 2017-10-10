from bs4 import BeautifulSoup
import requests
import time
import os
from slacker import Slacker

slack = Slacker('insert slack api key here')
print "Started!"
while True: 
    try:
        s = requests.Session()
        response = s.get("https://www.pmbull.com/gold-price/")



        soup = BeautifulSoup(response.text, "html.parser")

        goldprice = soup.findAll("div",{"id":"gold_spot_3"})
        ya = soup.find('b')
        final = ya.text
        semi = final.split()
        goldprice = semi[0]
        percent1 = semi[2]
        semipercent = (percent1[:-1]) #makes percent just a number : 0.01 etc....
        percent = (semipercent[1:])

        print goldprice + ' ' + '//' + ' ' + percent1
       
        if float(percent) > 0.99:
            print percent
            slack.chat.post_message('#goldpriceforpapa', 'Current Price Per Ounce: ' + goldprice + '\n' + "RECORD HIGH PERCENT!!" + ' ' + '--->' + ' ' + '+' + percent + '%') 
            time.sleep(20)
        else:
            time.sleep(20)
        
    except KeyboardInterrupt:
        break
    
  
