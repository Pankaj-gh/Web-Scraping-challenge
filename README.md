# Web-Scraping-challenge
This challenge has 3 parts
1) Scraping content from websites using Jupyter
2) Passing the above code within a funciton in a python file
3) Rendering the content on an HTML page

For part -1 it grabs the latest headline and content from the mars website alongwith the featued image, a table about mars facts and the images, content and names of the 4 hemispheres of mars.
For part -2 the above scraped content are stored in their respective variables and passed within a funciton in the scrape_mars.py file
The app.py file is used to import the scrape_mars.py file and call this scrpae function and the content is renderd on an HTML page.

The screenshots of the html page are added to the template folder within the repository

Libraries such as BS4,splinter,pandas were heavily used including, bootstrap for HTML and Mongo DB for app.py
