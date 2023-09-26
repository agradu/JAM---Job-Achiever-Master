import os
from time import sleep
from dotenv import load_dotenv
import app_functions
import cv_bot
from email_module import Email
from app_classes_v2 import Candidate, Adviser_Bot, Recruiter, Job
import cover_letter_bot


load_dotenv()


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("    ===== JOB ACHIEVER MASTER =====    ")
    print("    Your career success accelerator    ")
    print("---------------------------------------")
    update = ""
    if Candidate.data["name"] != "":
        update = app_functions.input_strict(
            "Do you want to update the info about the candidate (y/n)? ", ["y", "n"]
        )
    if update == "y" or Candidate.data["name"] == "":
        # 1) "Candidate info"
        # (which collects all the inputs for the personal info and the job)
        # Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)
        print("---------------------------------------")
        Candidate.data["user_language"] = input(
            "Which language do you choose for your documents? "
        )
        Candidate.data["name"] = input("Name: ")
        Candidate.data["surname"] = input("Surname: ")
        Candidate.data["birthday"] = app_functions.input_date("Birthday (dd.mm.yyyy): ")
        Candidate.data["sex"] = app_functions.input_strict(
            "Sex (male/female): ", ["male", "female"]
        )
        Candidate.data["phone"] = input("Phone: ")
        Candidate.data["email"] = app_functions.input_email("Email: ")
        Candidate.data["address"] = input("Address: ")
        print("---------------------------------------")
        print()
        print("Input some previous working experience.")
        print("---------------------------------------")
        Candidate.data["experience"] = []  # clear experience list in dictionary
        loop = True
        while loop:
            new_experience = {
                "title": input("Position: "),
                "description": input("Description: "),
                "company": input("Company: "),
                "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
                "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): "),
            }
            Candidate.add_experience(new_experience)
            answer = app_functions.input_strict(
                "Do you want to add a new experience? (y/n)? ", ["y", "n"]
            )
            print("---------------------------------------")
            if answer == "n":
                loop = False

        print()
        print("Input some previous education.")
        print("---------------------------------------")
        Candidate.data["education"] = []  # clear education list in dictionary
        loop = True
        while loop:
            new_education = {
                "title": input("Level of education: "),
                "description": input("Description: "),
                "school": input("Institution: "),
                "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
                "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): "),
            }
            Candidate.add_education(new_education)
            answer = app_functions.input_strict(
                "Do you want to add a new education? (y/n)? ", ["y", "n"]
            )
            print("---------------------------------------")
            if answer == "n":
                loop = False

        print()
        print("Input some hobbies. Ex: I play guitar with true passion.")
        print("---------------------------------------")
        Candidate.data["hobbies"] = []  # clear hobbies list in dictionary
        loop = True
        while loop:
            new_hobby = {
                "hobby": input("Hobby: "),
            }
            Candidate.add_hobbies(new_hobby)
            answer = app_functions.input_strict(
                "Do you want to add a new hobby? (y/n)? ", ["y", "n"]
            )
            print("---------------------------------------")
            if answer == "n":
                loop = False

        print()
        print("Input some skills. Ex: Python - expert level.")
        print("---------------------------------------")
        Candidate.data["skills"] = []  # clear skills list in dictionary
        loop = True
        while loop:
            new_skill = {
                "skill": input("Skill: "),
            }
            Candidate.add_skills(new_skill)
            answer = app_functions.input_strict(
                "Do you want to add a new skill? (y/n)? ", ["y", "n"]
            )
            print("---------------------------------------")
            if answer == "n":
                loop = False

        print()
        print("Input some languages. Ex: German - native.")
        print("---------------------------------------")
        Candidate.data["languages"] = []  # clear languages list in dictionary
        loop = True
        while loop:
            new_language = {
                "language": input("Language: "),
            }
            Candidate.add_languages(new_language)
            answer = app_functions.input_strict(
                "Do you want to add a new language? (y/n)? ", ["y", "n"]
            )
            print("---------------------------------------")
            if answer == "n":
                loop = False

        Candidate.save_infos()

    update = ""
    if Recruiter.data["name"] != "":
        update = app_functions.input_strict(
            "Do you want to update the info about the recuiter (y/n)? ", ["y", "n"]
        )
    if update == "y" or Recruiter.data["name"] == "":
        # 2) "Job"
        # Collect the information about the job description and the name of the Recruiter in HR
        print()
        print("Input some informations about the job.")
        print("---------------------------------------")
        Recruiter.data["name"] = input("Recriuter name: ")
        Recruiter.data["surname"] = input("Recriuter surname: ")
        Recruiter.data["sex"] = app_functions.input_strict(
            "Sex (male/female): ", ["male", "female"]
        )
        Recruiter.data["attitude"] = input("Recriuter attitude (for interview): ")
        Recruiter.data["email"] = app_functions.input_email("Recriuter email: ")
        Recruiter.data["position"] = input("Recriuter position: ")
        Recruiter.data["company"] = input("Company name: ")
        Recruiter.data["company_address"] = input("Company address: ")
        Recruiter.save_infos()

        Job.data["position"] = input("Job position: ")
        Job.data["description"] = input("""Job description: """)
        Job.data["source"] = input("Job anouncement source: ")
        Job.save_infos()

    Adviser_Bot.update_user_input()
    cv_description = Adviser_Bot.generate_cv_short_description()
    Candidate.data["short_description"] = cv_description
    Candidate.save_infos()
    Adviser_Bot.update_user_input()

    # 3) "CV"
    # Create the CV
    print()
    print("CV - module")
    print("---------------------------------------")
    print("Please, upload a picture for the CV.")
    resume = cv_bot.Resume(
        "json/candidate.json",
        cv_bot.HexColor("#D4AF37"),
        cv_bot.HexColor("#404040"),
        cv_bot.HexColor("#FFFFFF"),
    )
    resume.generate()
    sleep(2)

    # 4) "Cover letter
    # Writes the cover letter
    print()
    print("Cover Letter - module")
    print("---------------------------------------")
    Adviser_Bot.generate_letter()
    cover_letter_bot.generate()

    # 5) "Email"
    # Send the email, attaching cover letter and CV
    print()
    print("E-mail sender - module")
    print("---------------------------------------")
    email = Email(
        f"{Candidate.data['email']}",  # sender
        os.getenv("EMAIL_PASSWORD"),  # password
        [f"{Recruiter.data['email']}"],  # list of receivers
        f"Applying for the position of {Job.data['position']}",  # subject
    )

    body = Adviser_Bot.generate_letter()  # text of the email

    attachments = email.attachments(
        [f"pdfs/{Candidate.data['name']}_{Candidate.data['surname']}_CV.pdf"]
    )  # cv and cover letter

    email.send(email.password, body, attachments)  # Send the email

    # 6) "Interview"
    # Prepare for the job interview
    print()
    print("Interview - module")
    print("---------------------------------------")
    input("Ready for interview? ")
    os.system("clear")
    print(f"{Recruiter.data['name']}: Welcome {Candidate.data['name']}.")
    while True:
        user_message = input(f"{Candidate.data['name']}: ")
        if user_message == "EXIT":
            break
        Adviser_Bot.simulate_interview(user_message)
        os.system("clear")
        # print interview_history
        for m in Adviser_Bot.interview_history[1:]:
            if m["role"] == "assistant":
                person = Recruiter.data["name"]
            else:
                person = Candidate.data["name"]
            print(f'{person}: {m["content"]}')

    # 7) "Interview analyse"
    # Give a feedback about the interview
    os.system("cls" if os.name == "nt" else "clear")
    print("Interview analyse - module")
    print("---------------------------------------")
    input("Ready for interview analyse? ")
    # An interview analyse
    interview = ""
    for m in Adviser_Bot.interview_history[1:]:
        if Adviser_Bot.interview_history.index(m) % 2 == 0:
            person = "Candidate"
        else:
            person = "Recruiter"
        interview += f"{person}: {m['content']}\n"
    print("---------------------------------------")
    print()
    print("INTERVIEW ANALYSE:")
    print(Adviser_Bot.analize_interview(interview))


if __name__ == "__main__":
    main()
