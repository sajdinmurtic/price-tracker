from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

def check_price():
    
   URL = 'https://www.amazon.com/Lenovo-ThinkPad-E15-1920x1080-i5-10210U/dp/B086MTSCLQ/ref=sr_1_15?_encoding=UTF8&keywords=laptop+lenovo&nav_sdd=aps&pd_rd_r=f54966e5-5541-43ef-82d2-9df0419dc404&pd_rd_w=SDuZo&pd_rd_wg=WVH5M&pf_rd_p=0b4fe531-c123-435e-ac22-f6a1bb4bce0c&pf_rd_r=YTZRAFC1D6BE4DG5TZ5W&qid=1642179260&refinements=p_36%3A2421891011&s=pc&sr=1-15'

   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

   page = requests.get(URL, headers=headers)

   soup = BeautifulSoup(page.contnet, "html.parser")

   

   title = soup.find(id="productTitle").get_text()

   price = soup.find('span','a-offscreen').get_text().replace(',', '').replace('$', '').strip()

   today = datetime.date.today()
   print(title.strip())
   
   decreased_price = float(price[0:5])
   print(decreased_price)
   if(decreased_price < 1000):
         send_mail()
   


def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('********@gmail.com',' xxxxxxxxxx')
    
        subject = "The price is down"
        body = "Now is chance to buy laptop"
   
        msg = f"Subject: {subject}\n\n{body}"
    
        server.sendmail(
        '********@gmail.com',
        msg
     
    )  
       
    
while(True):
    check_price()
    time.sleep(86400) 
    

    
 
