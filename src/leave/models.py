from django.db import models
from django.contrib.auth.models import User

# 員工模型
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# 請假紀錄模型
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    # 請假狀態選項
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    manager_comment = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.employee.name} - {self.status}"
