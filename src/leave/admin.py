from django.contrib import admin
from .models import Employee, Leave

# Employee Admin 設定
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_manager')

# Leave Admin 設定
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status', 'manager_comment')

    # 是否為主管來設定請假狀態
    def get_readonly_fields(self, request, obj=None):
        employee = request.user.employee
        if not employee.is_manager:
            readonly_fields = self.readonly_fields + ('status', 'manager_comment')
        else:
            readonly_fields = self.readonly_fields
        return readonly_fields

    # 查詢自己請假紀錄
    def get_queryset(self, request):
        employee = request.user.employee
        queryset = super().get_queryset(request)
        if not employee.is_manager:
            queryset = queryset.filter(employee=employee)
        return queryset

    # 設定主管不能修改請假員工名自
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            employee = request.user.employee
            if employee.is_manager:
                kwargs["disabled"] = True
            else:
                kwargs["queryset"] = Employee.objects.filter(id=employee.id)
                kwargs["disabled"] = False
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# 註冊模型到 Django 後台
admin.site.register(Employee, EmployeeAdmin) 
admin.site.register(Leave, LeaveAdmin)
