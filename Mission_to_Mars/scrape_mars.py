from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


app = Flask(__name__)
@app.route("/scrape")
def scrape():
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)  
    # #Creating and Assigining URL

    # url='https://mars.nasa.gov/news/'
    # browser.visit(url)
    # html=browser.html
    # soup=BeautifulSoup(html,"html.parser")

    # # Assigining desired values to required variables

    # news_title=soup.find("li",class_="slide").h3.text.split()
    # news_p=soup.find("div",class_="article_teaser_body").text.strip()


    # #Creating and Assigining URL

    # url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # # Vising URL in browser
    # browser.visit(url)
    # html=browser.html

    # #Using Beautiful soup

    # soup=BeautifulSoup(html,"html.parser")

    # #Writing for loop to capture required text

    # imags=soup.find_all("a",class_="fancybox")
    # large_img=[]
    # for image in imags:
    #     featured_image_url=image['data-fancybox-href']
    #     large_img.append(featured_image_url)


    # #Creating and assigning URL

    # url="https://space-facts.com/mars/"

    # tables = pd.read_html(url)
    # len(tables)

    # #Assigning df to desired table

    # df=tables[0]

    # #Renaming columns

    # df.columns=['Description','']


    # #Adding Description as dataframe index

    # df=df.set_index('Description')

    # df

    # browser.quit()
    # html_table = df.to_html()
    # # print(html_table)


    # url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # browser.visit(url)


    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # headers=[]

    # #Creating a for loop to capture headers from the main page

    # for x in range(4):
    #     head=soup.find_all('div',class_="item")[x].h3.text
    #     headers.append(head)

    # #Creating a for loop to capture the links for the hemispheres

    # img_urls=[]
    # for x in range(4):
    #     url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #     browser.visit(url)
    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')
    #     browser.click_link_by_partial_text(headers[x])
    #     browser.click_link_by_partial_text("Open")
    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')
    #     img_url=soup.find_all('img',class_="wide-image")[0]['src']
    #     img_urls.append(img_url)
    # browser.quit()

    # hemisphere_image_urls=[{"title":"Cerberus Hemisphere Enhanced","image_url":"/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    #                     {"title":"Schiaparelli Hemisphere Enhanced","image_url":"/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    #                     {"title":"Syrtis Major Hemisphere Enhanced","image_url":"/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    #                     {"title":"Valles Marineris Hemisphere Enhanced","image_url":"/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"}]
                        

    
    main_dict={"news_title":"","news_p":""}




if __name__ == "__main__":
    app.run(debug=True)
