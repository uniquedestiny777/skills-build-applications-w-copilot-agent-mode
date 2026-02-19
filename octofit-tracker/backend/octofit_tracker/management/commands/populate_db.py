from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create users
        users = [
            User.objects.create(email='tony@stark.com', username='IronMan', team=marvel),
            User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User.objects.create(email='bruce@wayne.com', username='Batman', team=dc),
            User.objects.create(email='clark@kent.com', username='Superman', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date=date.today())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', difficulty='Hard')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', difficulty='Medium')
        w1.suggested_for.set([users[0], users[2]])
        w2.suggested_for.set([users[1], users[3]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=700, week=date.today())
        Leaderboard.objects.create(team=dc, total_points=600, week=date.today())

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
