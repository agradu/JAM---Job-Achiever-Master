from rest_framework.views import APIView
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


# Download the CV in a pdf
class DownloadCV(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        try:
            template = "generator_cv/cv.html"
            application = Application.objects.get(pk=pk)
            profile = application.profile
            user = profile.user
            education_list = Education.objects.filter(profile=profile)
            experience_list = Experience.objects.filter(profile=profile)
            skill_list = ProfileSkill.objects.filter(profile=profile)
            language_list = ProfileLanguage.objects.filter(profile=profile)
            hobby_list = ProfileHobby.objects.filter(profile=profile)
            today = date.today()
            if profile.picture in ["", None]:
                picture = ""
            else:
                picture = profile.picture
        except:
            return Response({"error": "Profile does not exist."}, status=404)

        context = {
            "picture": picture,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birthday": profile.birthday,
            "address": profile.address,
            "phone": profile.phone,
            "email": user.email,
            "portfolio": profile.portfolio_link,
            "facebook": profile.social_link,
            "educations": education_list,
            "experiences": experience_list,
            "skills": skill_list,
            "hobbies": hobby_list,
            "languages": language_list,
            "description": application.cv_short_description,
            "date": today.strftime("%d.%m.%Y"),
        }

        options = {
            "page-size": "A4",
            "margin-top": "20mm",
            "margin-right": "20mm",
            "margin-bottom": "20mm",
            "margin-left": "20mm",
            "enable-local-file-access": False,
        }
        output_file_name = f"cv {user.first_name} {user.last_name}.pdf"
        html_content = render(request, template, context)
        source = html_content.content.decode()
        pdf = pdfkit.from_string(source, False, options=options)
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{output_file_name}"'
        return response


# Update the fields of the actual CV on the basis of the data in DB
class UpdateCvDescriptionWithGPT(APIView):
    # permission_classes = [permissions.IsAuthenticated]

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

            role_description = f"""You are the candidate for a given job.
You must create a strong CV opening statement in {application.application_language} that highlights the sum of your strengths, experience and motivation to impress employer of that job.
You will create only the statement.
The statement must have less than 255 characters and must not contain your name."""

            messages = [
                gpt.bot_message("system", role_description),
                gpt.bot_message("user", formated_info),
            ]

            try:
                if profile.api_key not in ["", None]:
                    gpt.openai.api_key = profile.api_key
                    response = gpt.bot_request(messages)
                else:
                    response = """As a harmonious fusion of artistic insight and technical prowess, I embody the essence of a Full Stack Developer. 
Embracing the artistry within technology, I aspire to craft long lasting digital masterpieces."""
                application.cv_short_description = response
            except:
                application.cv_short_description = "Error processing request."
                return Response({"error": "Error processing request."}, status=500)
            application.cv_short_description = response
            application.save()
            return Response({"message": response})
        except:
            return Response({"error": "Profile does not exist."}, status=404)
