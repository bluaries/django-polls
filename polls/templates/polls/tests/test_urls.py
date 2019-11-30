import requests
from selenium import webdriver

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32/chromedriver.exe")
    browser.get(url)
    elements_tag = browser.find_elements_by_tag_name("a")
    links = [element.get_attribute("href") for element in elements_tag]
    browser.close()
    return links

def invalid_urls(urllist):
   list_invalid = []
   for url in urllist:
      r = requests.head(url)
      if r.status_code == 404:
         list_invalid.append(url)
   return list_invalid
      
if __name__ == "__main__":
   list_links = get_links("https://cpske.github.io/ISP/")
   for link in list_links:
      print("Valid link:" + link)
      
   invalid_links = invalid_urls(list_links)
   for invalid_link in invalid_links:
      print("Invalid link:" + invalid_link)