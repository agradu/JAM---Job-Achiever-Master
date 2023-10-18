from django.contrib.auth.models import User
from dependencies.models import *
from profiles.models import *
from applications.models import Application
from schedulers.models import Scheduler
from datetime import datetime


def run():
    username = "jane92"
    first_name = "Jane"
    last_name = "Doe"
    email = "jane_doe@example.com"
    password = "Pa$$w0rd1234!"
    try:
        user = User.objects.get(username=username)
        print("User already exist: delete the user...")
    except Exception:
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()
        print(f"User {username} created!")

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
        user=user,
        gender=Gender.objects.get(gender="Male"),
        phone="(+44) 0123456789",
        address="11 The Spires, Canterbury CT2 8SD, UK",
    )

    Education.objects.get_or_create(
        profile=profile,
        title="M.Sc. Machine Learning",
        school="University of Nottingham",
        description="I learned how to identify and use relevant computational tools and programming techniques, apply statistical and physical principles to break down algorithms, and explain how they work.",
        start_date="2015-09-01",
        end_date="2018-06-30",
    )
    
    Education.objects.get_or_create(
        profile=profile,
        title="B.Sc. Computer Science",
        school="University of Manchester",
        description="The course focused on the study of computer systems and software development: it provided me with a solid foundation in computer science principles, as well as practical skills in programming, data structures, algorithms, and software engineering.",
        start_date="2012-09-01",
        end_date="2015-06-30",
    )

    Experience.objects.get_or_create(
        profile=profile,
        title="Call Agent",
        company="Shoelando",
        description="I provided assistance and technical support to the custormers in a friendly and polite manner"
        start_date="2018-08-01",
        end_date="2021-07-31",
    )

    Experience.objects.get_or_create(
        profile=profile,
        title="Junior Developer",
        company="SmartUp Software",
        description="I provided assistance to support continuous improvement throughout the development life cycle of computer applications and wrote basic code, maintain applications, address bugs, and deploy app enhancements.",
        start_date="2021-08-01",
        end_date="2023-07-31",
    )

    ProfileSkill.objects.get_or_create(
        profile=profile,
        description="Teamwork"
    )
    ProfileSkill.objects.get_or_create(
        profile=profile,
        description="Critical thinking"
    )

    ProfileHobby.objects.get_or_create(
        profile=profile,
        description="Board game"
    )

    ProfileHobby.objects.get_or_create(
        profile=profile,
        description="Reading"
    )ProfileHobby.objects.get_or_create(
        profile=profile,
        description="Board game, reading",
    )

    ProfileLanguage.objects.get_or_create(
        profile=profile,
        description="English, German",
    )

    application, created = Application.objects.get_or_create(
        profile=profile,
        position="Senior Developer",
        company="Google",
        description="Develop ...",
        company_email="jude.smiley.python@gmail.com",
    )

    Scheduler.objects.get_or_create(
        user=user,
        application=application,
        interview_shedule="2023-10-12 12:00:00",
        interview_time_before="11:00",
        interview_time_after="14:00",
    )
