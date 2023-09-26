import os
from app_classes_v2 import Candidate
from app_classes_v2 import Recruiter
from app_classes_v2 import Adviser_Bot
from app_classes_v2 import Job

# import app_functions
import time

Candidate.data = {
    "name": "Adrian",
    "surname": "Radu",
    "birthday": "11.03.1977",
    "sex": "male",
    "phone": "1234567890",
    "email": "jude.smiley.python@gmail.com",
    "address": "Justastr. 11b, 39124 Magdeburg",
    "user_language": "english",
    "short_description": None,
    "experience": [],
    "education": [],
    "hobbies": [],
    "skills": [],
    "languages": [],
}
Candidate.add_experience(
    {
        "title": "Webdesigner",
        "description": "Responsable for mentenance of the company websites.",
        "company": "IATOM",
        "date_start": "10.10.2010",
        "date_end": "23.09.2022",
    }
)
Candidate.add_experience(
    {
        "title": "Art Director",
        "description": "Creation and implementing of web ads.",
        "company": "Stream Line",
        "date_start": "01.01.2000",
        "date_end": "10.10.2010",
    }
)
Candidate.add_experience(
    {
        "title": "Janitor",
        "description": "Cleaning of office rooms.",
        "company": "Amazon",
        "date_start": "01.01.1998",
        "date_end": "01.01.2000",
    }
)
Candidate.add_education(
    {
        "title": "Python Backend Programming",
        "description": "Cours",
        "school": "DCI",
        "date_start": "15.12.2022",
        "date_end": "10.01.2024",
    }
)
Candidate.add_education(
    {
        "title": "Graphic designer",
        "description": "Barcelors degree",
        "school": "University of Arts - Nicolae Grigorescu - Bucharest",
        "date_start": "01.09.1995",
        "date_end": "01.01.2000",
    }
)
Candidate.add_hobbies({"hobby": "music, games"})
Candidate.add_hobbies({"hobby": "reading, travel"})
Candidate.add_skills({"skill": "Python, PHP, mySQL"})
Candidate.add_languages({"language": "English (B1 - lower intermediate)"})
Candidate.add_languages({"language": "German (B2 - lower intermediate)"})
Candidate.save_infos()

Recruiter.data = {
    "name": "Nicolas",
    "surname": "Tesla",
    "sex": "male",
    "email": "jude.smiley.python@gmai.com",
    "position": "CEO",
    "company": "Elli - a brand of the Volkswagen Group",
    "company_address": "Berlinerstr. 11b, 39124 Berlin",
    "atitude": "sarcastic",
}
Recruiter.save_infos()

Job.data = {"position": None, "description": None, "source": None}
Job.data[
    "description"
] = """
What the candidate will do
- Actively learn and be always up-to-date with the industry trends and developments 
- You will be part of an agile and independent team with end to end responsibility for a product
- Design, build and operate scalable production systems
- Advocate for maintaining a high quality bar, making sure quality and testing are part of the development work from day one
- Contribute to the team's effectiveness and efficiency through setting an example of best SW development practices
- Contribute in one of our Communities of Practice 

What the candidate has
- Experience in developing high quality software in one of the modern programming languages (TypeScript, Python, Go, Ruby, etc.) 
- Experience in modern software development tools and systems including Git, Bash, Docker, Linux
- Experience with automated software testing, Continuous Integration and Continuous Delivery practices
- Readiness to work in cross-functional agile teams
- Knowledge in design patterns, data structures and algorithms
- Passion for continuous improvement, technical and operational excellence
- Passion and eagerness to learn different tools, technologies and practices that are needed to get the job done

Ideally the candidate has
- Experience in Typescript
- Experience with one of the leading public clouds (GCP, AWS, Azure) preferably GCP
- Experience in infrastructure provisioning tools like Terraform
- Experience in modern software development and delivery practices including Cloud Native and Microservices architecture, Everything as Code and Test Driven Development
- Experience in working in true DevOps teams where “you build it, you run it”
- Experience in EV charging field
"""
Job.data["position"] = "Software Engineer Backend"
Job.data["source"] = "www.stepstone.de"
Job.save_infos()

os.system("clear")
print("==============================================================================")
Adviser_Bot.update_user_input()
print(Adviser_Bot.show_user_input())
print("==============================================================================")
print()
input("Ready for SHORT DESCRIPTION FOR CV? ")
os.system("clear")
print("SHORT DESCRIPTION FOR CV:")
print(Adviser_Bot.generate_cv_short_description())
print("==============================================================================")
input("Ready for COVER LETTER? ")
print()
print("COVER LETTER:")
print(Adviser_Bot.generate_letter())
input("Ready for interview? ")
os.system("clear")
# A real interview simulation:
os.system("clear")
print(f"{Recruiter.data['name']}: Welcome {Candidate.data['name']}.")
interview_on = True
while interview_on:
    user_message = input(f"{Candidate.data['name']}: ")
    Adviser_Bot.simulate_interview(user_message)
    os.system("clear")
    # print interview_history
    for m in Adviser_Bot.interview_history[1:]:
        if m["role"] == "assistant":
            person = Recruiter.data["name"]
        else:
            person = Candidate.data["name"]
        print(f'{person}: {m["content"]}')
        if m["content"] == "EXIT":
            interview_on = False

input("Ready for interview analyse? ")
# An interview analyse
interview = ""
for m in Adviser_Bot.interview_history[1:]:
    if Adviser_Bot.interview_history.index(m) % 2 == 0:
        person = "Candidate"
    else:
        person = "Recruiter"
    interview += f"{person}: {m['content']}\n"
print("==============================================================================")
print()
print("INTERVIEW ANALYSE:")
print(Adviser_Bot.analize_interview(interview))
