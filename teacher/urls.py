from django.urls import path

from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('<int:status_number>/detail/', views.DetailView.as_view(), name='detail'),
    path('update/', views.update, name="update"),
    path('<int:pk>/', views.TeacherView.as_view(), name='teacher'),
    path('children/', views.ChildrenView.as_view(), name='children'),

]