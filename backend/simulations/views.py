from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from profiles.models import (
    Education,
    Experience,
    ProfileSkill,
    ProfileLanguage,
    ProfileHobby,
)
from simulations.models import Simulation
from dependencies import gpt_functions as gpt
from .serialazers import SimulationSerialazer
import json


# Recover simulations data from the DB
class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerialazer
    permission_classes = [permissions.IsAuthenticated]


# Build the virtual job interviewer
class SimulateInterviewWithGPT(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            simulation = Simulation.objects.get(pk=request.data["pk"])
            user_response = request.data["user_response"]
            application = simulation.application
            profile = application.profile
            user = simulation.user
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

            role_description = f"""You'll interview in {simulation.language} a candidate for a job.
As a recruiter for this job you have to put important questions to the candidate acording to the job description and react to his answers.
You will be focused to cover all the necesary job questions with a {simulation.recruiter_attitude} attitude."""

            # Simulate the interview and save it in the DB in a json format text
            messages = [
                gpt.bot_message("system", role_description),
                gpt.bot_message("user", formated_info),
                gpt.bot_message("assistant", f"Nice to meet you {user.first_name}!"),
            ] + simulation.json_file[3:]
            messages.append(gpt.bot_message("user", user_response))
            simulation.json_file = messages
            simulation.save()
            try:
                if profile.api_key not in ["", None]:
                    gpt.openai.api_key = profile.api_key
                    bot_response = gpt.bot_request(messages)
                else:
                    bot_response = f"Due to the lack of an API key, I cannot answer more than this reply. More information on how to get one can be found on the website https://openai.com/pricing"
                messages.append(gpt.bot_message("assistant", bot_response))
                simulation.json_file = messages
                simulation.save()
            except:
                return Response({"error": f"Error processing request."}, status=500)
            return Response({"bot_response": bot_response})
        except:
            return Response(
                {"error": f"Simulation {request.data['pk']} does not exist."},
                status=404,
            )


# Build the virtual job analyzer
class AnalyzeInterviewWithGPT(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            simulation = Simulation.objects.get(pk=request.data["pk"])
            application = simulation.application
            profile = application.profile
            user = simulation.user
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
            formated_info += f"{application.description}\n\n"
            formated_info += "THE INTERVIEW CONTENT IN JSON FORMAT:\n\n"
            formated_info += json.dumps(simulation.json_file[3:])

            role_description = f"""You are a job interview adviser.
Based on the input you receive, you will comment in {simulation.language} the answers of the candidate named 'user' provided in a json format.
You will sugest better answers for candidate when his are not good enough.
You don't ask questions or say anything other than the comments on the dialogs from job interview."""

            # Analyse the simulated job interview and save in the DB
            messages = [
                gpt.bot_message("system", role_description),
                gpt.bot_message("user", formated_info),
            ]
            try:
                if profile.api_key not in ["", None]:
                    gpt.openai.api_key = profile.api_key
                    bot_response = gpt.bot_request(messages)
                else:
                    bot_response = f"Due to the lack of an API key, I cannot analyze the given informations. But you can try to buy one here https://openai.com/pricing"
                simulation.review = bot_response
                simulation.save()
            except:
                return Response({"error": f"Error processing request."}, status=500)
            return Response({"bot_response": bot_response})
        except:
            return Response(
                {"error": f"Simulation {request.data['pk']} does not exist."},
                status=404,
            )
