from django.urls import path
from .views import EmployeeGetCreate,EmployeeUpdateDelte,DepartmentGetCreate,DepartmentUpdateDelte,TasksUpdateDelte,TasksGetCreate,AchivmentUpdateDelte,AchivmentGetCreate


urlpatterns = [
    path('employees',EmployeeGetCreate.as_view()),
    path('employee<int:pk>',EmployeeUpdateDelte.as_view()),
    path('departments',DepartmentGetCreate.as_view()),
    path('department<int:pk>',DepartmentUpdateDelte.as_view()),
    path('tasks',TasksGetCreate.as_view()),
    path('task<int:pk>',TasksUpdateDelte.as_view()),
    path('achivment',AchivmentGetCreate.as_view()),
    path('achivment<int:pk>',AchivmentUpdateDelte.as_view()),
]
