from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Leave, Employee
from .serializers import LeaveSerializer, LeaveApprovalSerializer

# 員工功能：查看自己的假單 / 提交請假
class LeaveListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # 查看自己所有假單
    def get(self, request):
        employee = get_object_or_404(Employee, user=request.user)
        leaves = Leave.objects.filter(employee=employee)
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

    # 提交請假
    def post(self, request):
        employee = get_object_or_404(Employee, user=request.user)
        data["employee"] = employee.id
        serializer = LeaveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# 管理員功能：查看所有待審核的假單
class PendingLeaveListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = get_object_or_404(Employee, user=request.user)
        if not employee.is_manager:
            return Response(status=status.HTTP_403_FORBIDDEN)
        leaves = Leave.objects.all()
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

# 管理員功能：核准請假
class ApproveLeaveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, leave_id):
        employee = get_object_or_404(Employee, user=request.user)
        if not employee.is_manager:
            return Response(status=status.HTTP_403_FORBIDDEN)
        leaves = Leave.objects.all()
        serializer = LeaveApprovalSerializer(leave, data={"status": "approved"}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 管理員功能：駁回請假
class RejectLeaveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, leave_id):
        employee = get_object_or_404(Employee, user=request.user)
        if not employee.is_manager:
            return Response(status=status.HTTP_403_FORBIDDEN)
        leaves = Leave.objects.all()
        serializer = LeaveApprovalSerializer(leave, data={"status": "rejected"}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
