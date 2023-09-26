from bs4 import BeautifulSoup
import requests
import json


def find_job():
    print("Put some skill that you are not familiar with")
    unfamiliar_skill = input("> ")
    print(f"Filtering out {unfamiliar_skill}")

    url = "https://www.stepstone.de/work/python"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("article", class_="res-1xbm2ji")

    job_details = []

    for job in jobs:
        company_name = job.find("div", class_="res-1v262t5").text.replace(" ", "")
        skills = job.find("div", class_="res-17md5or").text
        publish_date_tag = job.find("span", class_="res-qg8xf6")
        publish_date = publish_date_tag.get_text(strip=True) if publish_date_tag else ""
        link = "https://www.stepstone.de"
        more_info = link + job.h2.a["href"]

        if unfamiliar_skill not in skills:
            job_info = {
                "Company name": company_name,
                "Skills": skills,
                "Publish date": publish_date,
                "More info": more_info,
            }
            job_details.append(job_info)

    with open("json/job_details.json", "w") as f:
        json.dump(job_details, f, indent=4)

    print("Created json file successfuly!")


if __name__ == "__main__":
    find_job()
