from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create Users
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=20, date=date.today())

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Flight School', description='Aerobic workout for flying heroes')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100, rank=1)
        Leaderboard.objects.create(team=dc, total_points=80, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
