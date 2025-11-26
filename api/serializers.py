from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Trainer, WorkoutType, WorkoutSession, Membership

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Trainer
        fields = '__all__'

class WorkoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutType
        fields = '__all__'

class WorkoutSessionSerializer(serializers.ModelSerializer):
    workout_type = WorkoutTypeSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)
    workout_type_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkoutType.objects.all(), 
        source='workout_type', 
        write_only=True
    )
    trainer_id = serializers.PrimaryKeyRelatedField(
        queryset=Trainer.objects.all(), 
        source='trainer', 
        write_only=True
    )
    
    class Meta:
        model = WorkoutSession
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        source='user', 
        write_only=True
    )
    
    class Meta:
        model = Membership
        fields = '__all__'