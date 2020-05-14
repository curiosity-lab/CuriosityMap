from django.urls import path

from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('update/', views.update, name="update"),
    path('<int:pk>/', views.TeacherView.as_view(), name='teacher')
]