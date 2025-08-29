from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

# SET MAX PAGES TO SCRAPE
MAX_PAGES = 5



def connectToJobSite(func):
    """
        Decorator that handles HTTP request and HTML parsing for a job site URL.

        Args:
            func (function): A function that accepts a BeautifulSoup object and returns structured data.

        Returns:
            function: The wrapped function with HTML content from the provided URL.
    """
    def inner(URL, currentPage):
        try:
            
            if "jobberman" in URL:
                URL = f"https://www.jobberman.com/jobs?page={currentPage}"
            elif "myjobmag" in URL:
                URL = f"https://www.myjobmag.com/jobs/page/{currentPage}"
            elif "snaphunt" in URL:
                URL = f"https://snaphunt.com/job-listing/nigeria"
            
            page = requests.get(URL)
            content = BeautifulSoup(page.content, "html.parser")
            scraper = func(content) 
            print(f"The {func.__name__} is executed successfully")

            return scraper
            
        except requests.exceptions.Timeout:
            print("Connecting to the URL timed out. Please try again later.")
            
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects. Please check the URL and try again.")
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the request: {e}")
    return inner
