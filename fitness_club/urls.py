from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api.views import (
    UserViewSet, TrainerViewSet, WorkoutTypeViewSet,
    WorkoutSessionViewSet, MembershipViewSet
)

# Swagger setup
schema_view = get_schema_view(
    openapi.Info(
        title="Fitness Club API",
        default_version='v1',
        description="API for fitness club management",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@fitnessclub.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# API Router
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'workout-types', WorkoutTypeViewSet)
router.register(r'workout-sessions', WorkoutSessionViewSet)
router.register(r'memberships', MembershipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]