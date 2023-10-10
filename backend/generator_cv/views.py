from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import Profile, Education, Experience, ProfileSkill, ProfileLanguage, ProfileHobby
from applications.models import Application
from .serializers import CVSerializer
from dependencies import gpt_functions as gpt

# Create your views here.

class UpdateCvDescription(APIView):
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
            formated_info += f"{user.first_name} {user.last_name} ({profile.gender.gender}), born on {profile.birthday.strftime('%d.%m.%Y')}.\n\n"
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
            
            gpt.openai.api_key = profile.api_key

            messages = [
                gpt.bot_message("system", formated_info),
                gpt.bot_message("user", role_description),
            ]
            
            try:
                response = gpt.bot_request(messages)
                application.cv_short_description = response
                application.save()
                return Response({"response": response})
            except Exception as e:
                application.cv_short_description = "Error processing request."
                application.save()
                return Response({"error": "Error processing request."}, status=500)
        
        except Profile.DoesNotExist:
            return Response(status=404)
        