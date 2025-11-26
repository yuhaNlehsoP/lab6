from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='trainers/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ]
    )
    
    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    current_participants = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.workout_type.name} - {self.date_time}"

class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.membership_type}"