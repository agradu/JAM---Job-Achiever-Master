from django.contrib.auth.models import User
from dependencies.models import *
from profiles.models import *
from applications.models import Application
from schedulers.models import Scheduler
from datetime import datetime


def run():    
    username = f"fake_user"
    first_name = "John"
    last_name = "Doe"
    email = f"john_doe@example.com"
    password = "Pa$$w0rd1234!"
    try:
        user = User.objects.get(username=username)
        print("User already exist: delete the user...")
    except Exception:
        user = User.objects.create(
            username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        print("Fake user created!")
    
    languages = [
        "Arabic",
        "Bengali",
        "Czech",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
        "Danish",
        "Dutch",
        "English",
        "Esperanto",
        "Finnish",
        "French",
        "German",
        "Greek",
        "Hebrew",
        "Hindi",
        "Hungarian",
        "Indonesian",
        "Italian",
        "Japanese",
        "Korean",
        "Malay",
        "Norwegian",
        "Persgenderh",
        "Portuguese",
        "Romanian",
        "Russian",
        "Spanish",
        "Swahili",
        "Swedish",
        "Tagalog",
        "Thai",
        "Tamil",
        "Turkish",
        "Ukrainian",
        "Urdu",
        "Vietnamese",
    ]
    for language in languages: 
        Language.objects.get_or_create(language=language)
        
    genders = ["Male", "Female", "Other"]
    
    for gender in genders: 
        Gender.objects.get_or_create(gender=gender)
    
    statuses = ["Saved", "Applied", "Scheduled", "Accepted", "Rejected"]
    
    for status in statuses: 
        Status.objects.get_or_create(status=status)
        
    profile, created = Profile.objects.get_or_create(
        user = user,
        gender = Gender.objects.get(gender="Male"),  
        phone = "0123456789",
        address = "High Street 1 Cambridge CB1 NB1"
    )
    
    Education.objects.get_or_create(
        profile = profile,
        title = "B.Sc. History",
        school = "University",
        description = "Course about ...",
        start_date = datetime.now(),
        end_date = datetime.now(),
    )
    
    Experience.objects.get_or_create(
        profile = profile,
        title = "Junior Developer",
        company = "Searchmetrics",
        description = "Helped to develop...",
        start_date = datetime.now(),
        end_date = datetime.now(),        
    )
    
    ProfileSkill.objects.get_or_create(
        profile = profile,
        description = "Teamwork, critical thinking",
    )
    
    ProfileHobby.objects.get_or_create(
        profile = profile,
        description = "Board game, reading",     
    )
    
    ProfileLanguage.objects.get_or_create(
        profile = profile,
        description = "English, Language",
    )
    
    application, created = Application.objects.get_or_create(
        profile = profile,
        position = "Senior Developer",
        company = "Google",
        description = "Develop ...",
        company_email = "jude.smiley.python@gmail.com"   
    )
    
    Scheduler.objects.get_or_create(
        user = user,
        application = application,
        interview_shedule = "2023-10-12 12:00:00",
        interview_time_before = "11:00",
        interview_time_after = "14:00",
    )