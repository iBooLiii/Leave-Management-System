from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import LeaveListCreateAPIView, PendingLeaveListAPIView, ApproveLeaveAPIView, RejectLeaveAPIView  # 引入視圖（views），這些視圖處理不同的 API 請求

# Swagger 文件視圖
schema_view = get_schema_view(
    openapi.Info(
        title="Leave Management API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# url 設定
urlpatterns = [
    path('leaves/', LeaveListCreateAPIView.as_view(), name='leave-list-create'),
    path('manage/leaves/', PendingLeaveListAPIView.as_view(), name='pending-leave-list'),
    path('manage/leaves/<int:leave_id>/approve/', ApproveLeaveAPIView.as_view(), name='approve-leave'),
    path('manage/leaves/<int:leave_id>/reject/', RejectLeaveAPIView.as_view(), name='reject-leave'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
