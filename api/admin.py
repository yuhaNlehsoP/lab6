from django.contrib import admin
from .models import Trainer, WorkoutType, WorkoutSession, Membership

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'experience']
    list_filter = ['specialization']

@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'difficulty']
    list_filter = ['difficulty']

@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ['workout_type', 'trainer', 'date_time', 'current_participants', 'max_participants']
    list_filter = ['workout_type', 'trainer', 'date_time']

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'membership_type', 'start_date', 'end_date', 'is_active']
    list_filter = ['membership_type', 'is_active']