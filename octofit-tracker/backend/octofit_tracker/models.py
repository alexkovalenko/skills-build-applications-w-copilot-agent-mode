from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    is_superhero = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user.name} - {self.activity_type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(Team, related_name='workouts')
    
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='leaderboard')
    total_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"
