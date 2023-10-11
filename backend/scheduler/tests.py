from django.test import TestCase
from .models import Scheduler
from django.contrib.auth.models import User
from applications.models import Application
from profiles.models import Profile
from dependencies.models import Gender, Language, Status
from django.utils import timezone
import datetime
from django.urls import reverse

# Create your tests here.
class SchedulerTest(TestCase):

    def test_scheduler_creation(self):
        user = User.objects.create(username='test', password='123')
        user.save()
        gender = Gender.objects.create(gender='Male')
        gender.save()
        language = Language.objects.create(language='English')
        language.save()
        status = Status.objects.create(status='Saved')
        status.save()
        profile = Profile.objects.create(user=user, gender=gender)
        profile.save()
        application = Application.objects.create(profile=profile, position='front', company='test', description='test', company_email='test@test.com', application_language=language, status=status, recruiter_gender=gender)
        application.save()
        time_saved = datetime.datetime.now()
        time_before = time_saved - datetime.timedelta(hours=1)
        time_after = time_saved + datetime.timedelta(hours=1)
        scheduler = Scheduler.objects.create(user=user, application=application, interview_shedule=time_saved, interview_time_before=time_before, interview_time_after=time_after)
        scheduler.save()
        self.assertEqual(time_saved, scheduler.interview_shedule)