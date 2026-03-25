from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Avengers", universe="Marvel")
        self.user = User.objects.create(email="tony@stark.com", name="Tony Stark", team=self.team)
        self.workout = Workout.objects.create(name="Cardio", description="Run 5km")
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type="run", duration_minutes=30, date="2024-01-01")
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)

    def test_users_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboards_endpoint(self):
        response = self.client.get("/api/leaderboards/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
