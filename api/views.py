from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Trainer, WorkoutType, WorkoutSession, Membership
from .serializers import (
    UserSerializer, TrainerSerializer, WorkoutTypeSerializer,
    WorkoutSessionSerializer, MembershipSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class WorkoutTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkoutType.objects.all()
    serializer_class = WorkoutTypeSerializer

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        session = self.get_object()
        if session.current_participants < session.max_participants:
            session.current_participants += 1
            session.save()
            return Response({'status': 'Joined workout session'})
        return Response(
            {'error': 'Workout session is full'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        session = self.get_object()
        if session.current_participants > 0:
            session.current_participants -= 1
            session.save()
            return Response({'status': 'Left workout session'})
        return Response(
            {'error': 'No participants in workout session'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer