from rest_framework import serializers 
from .models import Leave

# 員工請假單的資料轉換處理
class LeaveSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.name', read_only=True) 

    class Meta:
        model = Leave
        fields = [
            'id',
            'employee',
            'employee_name',
            'start_date',
            'end_date',
            'reason',
            'status',
            'manager_comment'
        ]
        read_only_fields = ['status', 'manager_comment']

# 管理員審核假單用的轉換器
class LeaveApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['status', 'manager_comment']
