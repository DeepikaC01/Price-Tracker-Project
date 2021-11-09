import requests
from bs4 import BeautifulSoup
Products_to_Track = [
    {
        "Product_URL": "https://www.amazon.in/DJ-GREENS-Micro-greens-Gardening-Amaranths/dp/B08MCFZFZT/ref=sr_1_4?crid=3LNNG78LIBWMN&dchild=1&keywords=DJ+Greens&qid=1635685532&sprefix=dj+greens%2Caps%2C226&sr=8-4",
        "Name" : "DJ GREENS 5 Variety of Micro-greens Seeds",
        "Target_Price": 300
    },
    {
        "Product_URL": "https://www.amazon.in/DJ-GREENS-Micro-greens-Gardening-Amaranths/dp/B08MCGH5FV/ref=sr_1_4?crid=Y2QF4X0EY3CN&dchild=1&keywords=DJ%2BGreens&qid=1635685913&sprefix=dj%2Bgreens%2Caps%2C233&sr=8-4&th=1",
        "Name": "DJ GREENS 10 Variety Of Microgreens Seeds",
        "Target_Price": 600
    },
    {
        "Product_URL": "https://www.amazon.in/DJ-GREENS-Simple-Easy-Microgreens/dp/B08KWGZN1R/ref=sr_1_56?crid=Y2QF4X0EY3CN&dchild=1&keywords=DJ+Greens&qid=1635685615&sprefix=dj+greens%2Caps%2C233&sr=8-56",
        "Name": "DJ GREENS DIY Simple & Easy Microgreens Grow Kit",
        "Target_Price": 500
    },
    {
        "Product_URL": "https://www.amazon.in/Samsung-Metallic-Storage-Additional-Exchange/dp/B089MT16TZ/ref=sr_1_1?crid=2YVYD54Y8KW5D&keywords=samsung+a51&qid=1635948318&sprefix=Samsung+A51%2Caps%2C936&sr=8-1",
        "Name": "Samsung Galaxy A51",
        "Target_Price": 26000
    },
    {
        "Product_URL": "https://www.amazon.in/OPPO-Smart-Extra-Sport-Strap/dp/B08XM3VFNT/ref=sr_1_4?crid=YP9ABQE4V2A4&dchild=1&keywords=Oppo+band&qid=1635686353&sprefix=oppo+ban%2Caps%2C456&sr=8-4",
        "Name": "OPPO Smart Band",
        "Target_Price": 3000
    }
]
def Give_Product_Price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }
    Page = requests.get(URL, headers=headers)
    Soup = BeautifulSoup(Page.content, 'html.parser')
    Product_Price = Soup.find(id="priceblock_ourprice")
    if(Product_Price == None):
        Product_Price = Soup.find(id="priceblock_dealprice")
    return Product_Price.getText()
Result_File = open('my_result_file.txt','w')
try:
    for Every_Product in Products_to_Track:
        Product_Price_Returned = Give_Product_Price(Every_Product.get("Product_URL"))
        print(Product_Price_Returned + " - " + Every_Product.get("Name"))
        My_Product_Price = Product_Price_Returned[1:]
        My_Product_Price = My_Product_Price.replace(',','')
        My_Product_Price = int(float(My_Product_Price))
        print(My_Product_Price)
        if My_Product_Price < Every_Product.get("Target_Price"):
            print("Available at your required price")
            Result_File.write(Every_Product.get("Name") + ' - \t' + ' Available at Target Price ' + ' Current Price - ' + str(My_Product_Price) + '\n')
        else:
            print("Still at current price")
finally:
    Result_File.close()
