# 請假管理系統 (Leave Management System)
這是一個基於 Django 的員工請假管理系統。

## 功能
**員工功能**:
    提交請假單
    查詢自己的請假紀錄
**管理者功能**:
    查詢所有待審核請假單
    核准或駁回請假申請

## 安裝與配置
**安裝依賴**:
    pip install -r requirements.txt
**資料表**:
    python manage.py migrate
**創建創建超級用戶**:
    python manage.py createsuperuser
**啟動伺服器**:
    python manage.py runserver

## 目錄結構
leave-management-system/
├─ manage.py
├─ src/
│   ├─ config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├─ leave/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├─ __init__.py
├─ requirements.txt
├─ README.md

## Swagger API 文件
    http:///localhost:8000/api/swagger/
