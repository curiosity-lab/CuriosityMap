from django.urls import path

from . import views

app_name = 'parent'
urlpatterns = [
    path('<uuid:teacher_id>/', views.ParentIndexView.as_view(), name='index'),          # landing page
    path('<uuid:teacher_id>/<int:status_number>/consent/', views.ConsentView.as_view(), name='consent'),
    path('<uuid:teacher_id>/<int:status_number>/child/', views.ChildView.as_view(), name='child'),
    path('<uuid:child_id>/childadddata/', views.childadddata, name="childadddata"),
    path('<uuid:child_id>/<int:status_number>/parent/', views.ParentView.as_view(), name='parent'),
    path('<uuid:parent_id>/parentadddata/', views.parentadddata, name="parentadddata"),
    path('<uuid:parent_id>/childquestionnaire/', views.childquestionnaire, name="childquestionnaire"),
    path('<uuid:parent_id>/thankyou/', views.ThankyouView.as_view(), name="thankyou"),
]


