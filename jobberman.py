from extension import connectToJobSite, MAX_PAGES
import pandas as pd 
pd.set_option('display.max_columns', 10)

# jobberman = "https://www.jobberman.com/jobs"
# title: string;
# company: string;
# location: string;
# link: string;
# source: string;
# timestamp: string;


@connectToJobSite
def jobberMan(content, currentPage=1):

    
    """
        Scrapes job listings from the JobberMan website.

        Args:
            content (BeautifulSoup): Parsed HTML content of the JobberMan jobs page.

        Returns:
            pd.DataFrame: A DataFrame containing job title, company, location, 
                        posting date, job URL, and source for each job listed.
    """
    # r = f"{str(content)}?page={currentPage}"
    # print(r)
    job_cards = content.find_all(attrs={"data-cy" : "listing-cards-components"})
    jobs = []

    while currentPage <= 1:
        try:
            for job in job_cards:
                posted_at = job.find("p", class_="ml-auto text-sm font-normal text-gray-700 text-loading-animate")

                jobs_info = job.find("div", class_="w-full")
                title_et_company = jobs_info.find_all("p")
                title = title_et_company[0].text.strip()
                company = title_et_company[1].text.strip()
                href = jobs_info.find("a", href=True)["href"].strip()
                location = job.find("span", class_="bg-brand-secondary-100")
            
                jobs.append({
                        "title": title,
                        "company": company,
                        "posted_at": "".join(posted_at),
                        "location": "".join(location).strip(),
                        "href": href,
                        "source": "JobberMan"
                    })
            
        except Exception as e:
            print(f"Error parsing job card: {e}")
            
        currentPage += 1

    return pd.DataFrame(jobs)
        

jobberman =  jobberMan("https://www.jobberman.com/jobs", 3)
# print(jobs)
