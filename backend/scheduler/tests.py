from django.test import TestCase
from .models import Scheduler
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse

# Create your tests here.
# class SchedulerTest(TestCase):

#     def test_scheduler_creation(self):
#         self.user = User.objects.create(username='test')
#         time_before=timezone.now() - datetime.timedelta(hours=1)
#         time_after=timezone.now() + datetime.timedelta(hours=1)
#         scheduler = Scheduler(interview_shedule=timezone.now(), interview_time_before=time_before, interview_time_after=time_after)
#         scheduler.save()
#         self.assertEqual(timezone.now(), scheduler.interview_shedule)