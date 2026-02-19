from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        self.assertEqual(str(user), 'TestUser')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, calories=100, date='2024-01-01')
        self.assertEqual(activity.type, 'Run')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, week='2024-01-01')
        self.assertEqual(leaderboard.total_points, 100)
