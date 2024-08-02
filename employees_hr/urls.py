from django.urls import path, include
import employees_hr
from employees_hr.views import *
from rest_framework.routers import DefaultRouter
from .views import *






urlpatterns = [
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('token/', ObtainTokenPairWithRoleView.as_view(), name='token_obtain_pair'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'),
    path('api/login/', ObtainTokenPairWithRoleView.as_view(), name='token_obtain_pair'),
    path('api/reset-password/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('features/', FeatureListCreate.as_view(), name='feature-list-create'),
    path('features/<int:pk>/', FeatureRetrieveUpdateDestroy.as_view(), name='feature-retrieve-update-destroy'),
    path('api/payrolls/', PayrollViewSet.as_view(), name='pay-roll-view-set'),
    path('api/attendaces/', AttendanceViewSet.as_view(), name='Attendance-View-Set'),
    path('api/leave/', LeaveRequestListCreate.as_view(), name='leave-request-list-create'),
    path('api/documents/', DocumentListCreate.as_view(), name='document-list-create'),
    path('api/performanceevaluation/', PerformanceEvaluationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='performance-evaluation-list'),
    
    path('api/performanceevaluation/<int:pk>/', PerformanceEvaluationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='performance-evaluation-detail'),
]
