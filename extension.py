from bs4 import BeautifulSoup
import requests

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
            elif "myjobmybag" in URL:
                URL = f"https://www.myjobmag.com/jobs/page/{currentPage}"
            
            # scraper = func(URL) 
            # page = requests.get(scraper)
            # content = BeautifulSoup(page.content, "html.parser")
            # print(f"The {content.__name__} is executed successfully")
            
                
            page = requests.get(URL)
            content = BeautifulSoup(page.content, "html.parser")
            scraper = func(content) 
            print(f"The {func.__name__} is executed successfully")
            return scraper
            
        except Exception as e:
            print("An Error Occured!",e)
    return inner
