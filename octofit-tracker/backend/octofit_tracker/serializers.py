from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

# Helper to convert ObjectId to string
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe']

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'is_superhero']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    suggested_for = TeamSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points', 'rank']
