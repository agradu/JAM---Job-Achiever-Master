from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from profiles.models import (
    Education,
    Experience,
    ProfileSkill,
    ProfileLanguage,
    ProfileHobby,
)
from applications.models import Application
from dependencies import gpt_functions as gpt
from django.shortcuts import render, HttpResponse
from datetime import date
import pdfkit, os
from django.template.loader import render_to_string


# Download the cover letter in a pdf
class DownloadCoverLetter(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            template = "generator_letter/letter.html"
            application = Application.objects.get(pk=pk)
            profile = application.profile
            user = profile.user
            today = date.today()
        except:
            return Response({"error": "Application does not exist."}, status=404)

        context = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "address": profile.address,
            "phone": profile.phone,
            "email": user.email,
            "company": application.company,
            "company_email": application.company_email,
            "company_address": application.company_address,
            "recruiter_name": application.recruiter_name,
            "subject": application.position,
            "body": application.cover_letter_text,
            "date": today.strftime("%d.%m.%Y"),
        }

        options = {
            "page-size": "A4",
            "margin-top": "20mm",
            "margin-right": "20mm",
            "margin-bottom": "20mm",
            "margin-left": "20mm",
            "enable-local-file-access": True,
        }
        output_file_name = f"cover-letter {user.first_name} {user.last_name}.pdf"
        html_content = render(request, template, context)
        source = html_content.content.decode()
        pdf = pdfkit.from_string(source, False, options=options)
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{output_file_name}"'
        return response


# Update the fields of the cover letter on the basis of the data in DB
class UpdateCoverLetterWithGPT(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            application = Application.objects.get(pk=pk)
            profile = application.profile
            user = profile.user
            education_list = Education.objects.filter(profile=profile)
            experience_list = Experience.objects.filter(profile=profile)
            skill_list = ProfileSkill.objects.filter(profile=profile)
            language_list = ProfileLanguage.objects.filter(profile=profile)
            hobby_list = ProfileHobby.objects.filter(profile=profile)

            formated_info = ""
            formated_info += "CANDIDATE PERSONAL DATES: "
            formated_info += f"{user.first_name} {user.last_name} ({profile.gender}), born on {profile.birthday.strftime('%d.%m.%Y')}.\n\n"
            formated_info += "CANDIDATE EDUCATION:\n\n"
            for i in education_list:
                formated_info += f"{i.start_date.strftime('%d.%m.%Y')}-{i.end_date.strftime('%d.%m.%Y')} in {i.school}\nTitle: {i.title}\nDescription:\n{i.description}\n\n"
            formated_info += "CANDIDATE EXPERIENCE:\n\n"
            for i in experience_list:
                formated_info += f"{i.start_date.strftime('%d.%m.%Y')}-{i.end_date.strftime('%d.%m.%Y')} in {i.company}\nTitle: {i.title}\nDescription:\n{i.description}\n\n"
            formated_info += "CANDIDATE SKILLS:\n"
            for i in skill_list:
                formated_info += f"- {i.description}\n"
            formated_info += "\nLANGUAGES KNOWN BY THE CANDIDATE:\n"
            for i in language_list:
                formated_info += f"- {i.description}\n"
            formated_info += "\nCANDIDATE HOBBIES:\n\n"
            for i in hobby_list:
                formated_info += f"- {i.description}\n"
            formated_info += "RECRUTIER PERSONAL INFOS: "
            formated_info += f"{application.recruiter_name} ({application.recruiter_gender}), having {application.recruiter_position} position by {application.company}.\n"
            formated_info += "JOB INFORMATIONS: "
            formated_info += f"The job was found on {application.source} having '{application.position}' as position.\n"
            formated_info += "\nDESIRED JOB DESCRIPTION:\n\n"
            formated_info += f"{application.description}"

            role_description = f"""You are a cover letter creator for jobs.
Based on the input you receive, you will compose the content of a cover letter for the desired job based only on the data provided.
Provide only the body text of the cover letter without header or footer.
Don't mention unnecesary informations from my experience or education.
Write the text Profileof the letter in {application.application_language} in a concise and bold style suitable for the job to which the candidate is applying.
You don't ask questions or say anything other than the content of the cover letter."""
            messages = [
                gpt.bot_message("system", role_description),
                gpt.bot_message("user", formated_info),
            ]
            try:
                if profile.api_key not in ["", None]:
                    gpt.openai.api_key = profile.api_key
                    response = gpt.bot_request(messages)
                else:
                    response = """Dear Hiring Manager,

I am writing to express my strong interest in the Working Student Cloud Services position at Adobe Systems Europe Limited, as advertised on Stepstone. With a passion for technology and a solid foundation in web development, I am excited about the opportunity to contribute to Adobe's innovative and dynamic team.

My educational background includes a PHP and MySQL Developer course at Avantaj Consulting in Bucharest, where I honed my skills in HTML, PHP, and MySQL. During this time, I developed a complex web application with a login system and user interface, utilizing databases. Additionally, I recently completed a Python Back-end Developer course at DCI Digital Career Institute GmbH in Berlin, which provided me with training in Python, databases, Django, APIs, and cloud services.

I believe that my technical skills, along with my curiosity about application and infrastructure security and compliance topics, make me a strong candidate for this role. I have experience reading and writing code in various programming languages, including Python, and I am comfortable working with command line interfaces and shell scripts. My education and training have equipped me with a basic understanding of cloud platforms, containerization, and distributed systems.

What excites me about the Working Student Cloud Services position at Adobe is the opportunity to learn and contribute to a secure and compliant cloud service environment. I am dedicated to ensuring that large-scale web services are designed, developed, tested, and operated securely. My automation-first mentality and willingness to speak up when necessary align with Adobe's commitment to excellence in security and compliance.

Furthermore, I am fluent in English and am eager to learn German to enhance my communication skills. I believe that my background and enthusiasm for technology, along with my commitment to teamwork and self-organization, make me a valuable addition to the Adobe Cloud Platform - Security & Compliance team.

Thank you for considering my application. I look forward to the possibility of contributing to Adobe's mission of creating exceptional digital experiences. Please feel free to reach out to me at your earliest convenience to discuss my qualifications in more detail.

Sincerely,

John Doe"""
                application.cover_letter_text = response
            except:
                application.cover_letter_text = "Error processing request."
                return Response({"error": f"Error processing request."}, status=500)
            application.save()
            return Response({"response": response})
        except:
            return Response({"error": "Application does not exist."}, status=404)
