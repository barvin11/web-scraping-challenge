from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
  executable_path = {'executable_path': ChromeDriverManager().install()}
  browser = Browser("chrome", **executable_path,headless=False)
  return browser

all_info = {}

def all_info_func():
  browser = start_browser()
  url = 'https://redplanetscience.com/'
  browser.visit(url)
  html = browser.html
  html_soup = soup(html,'html.parser')  
  title = html_soup.find('div', class_='content_title').text
  all_info['news_title'] = title
  body = html_soup.find('div', class_='article_teaser_body').text 
  all_info['news_body'] = body

  browser = start_browser()
  jpl_url = 'https://spaceimages-mars.com'
  browser.visit(jpl_url)
  html = browser.html

  html_soup = soup(html, 'html.parser')

  image = html_soup.find('img', class_='headerimage fade-in')['src']
  featured_image_url = jpl_url + "/" + image
  all_info['featured_image'] = featured_image_url

  mars_facts = 'https://space-facts.com/mars/'
  mars_facts_table = pd.read_html(mars_facts)
  df = mars_facts_table[1]
  df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
  html_table = df.to_html()
  all_info['mars_facts'] = html_table

  browser = start_browser()
  main_page = 'https://marshemispheres.com/'
  browser.visit(main_page)
  html = browser.html
  html_soup = soup(html, 'html.parser')
  urls = html_soup.find_all( 'div', class_='item')
  final_result = []

  for x in urls:
      title = x.find('h3').text
      sub_url = x.find('a')['href']
      
      subpage = main_page + sub_url
      browser.visit(subpage)
      html = browser.html
      html_soup = soup(html, 'html.parser')
      
      image_loc = html_soup.find('div', class_='downloads')
      jpeg_image = image_loc.find('a')['href']
      full_url = main_page + jpeg_image
      
      hemisphere_info = {}
      hemisphere_info['title'] = title
      hemisphere_info['img_url'] = full_url
      final_result.append(hemisphere_info)
 
  all_info['final_result'] = final_result
  return all_info











  