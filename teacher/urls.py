from django.urls import path

from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/', views.auth, name='auth'),
    path('<int:status_number>/register/', views.RegisterView.as_view(), name='register'),
    path('update/', views.update, name="update"),
    path('<int:status_number>/detail/', views.DetailView.as_view(), name='detail'),
    path('<uuid:teacher_id>/adddata/', views.adddata, name="adddata"),
    path('<int:pk>/', views.TeacherView.as_view(), name='teacher'),
    path('<uuid:source_id>/children/', views.ChildrenView.as_view(), name='children'),

]

# index
# login --> auth
# ----> children
# register --> register --> update
# ----> details (source_id)
# ----------> questionnaire
# <------ children