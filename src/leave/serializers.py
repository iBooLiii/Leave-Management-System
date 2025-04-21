from rest_framework import serializers 
from .models import Leave

# ���u�а��檺����ഫ�B�z
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

# �޲z���f�ְ���Ϊ��ഫ��
class LeaveApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['status', 'manager_comment']
