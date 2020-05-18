from django.urls import path

from . import views

app_name = 'questionnaire'
urlpatterns = [
    path('<slug:source>/<uuid:source_id>/<slug:target>/<uuid:target_id>/explanation', views.ExplanationView.as_view(), name='explanation'),
    path('<slug:source>/<uuid:source_id>/<slug:target>/<uuid:target_id>/<int:status>/questionnaire', views.QuestionnaireView.as_view(), name='questionnaire'),
    path('<slug:source>/<uuid:source_id>/<slug:target>/<uuid:target_id>/submitted/', views.submitted, name='submitted'),
    path('<slug:source>/<uuid:source_id>/<slug:target>/<uuid:target_id>/thankyou/', views.ThankYouView.as_view(), name='thankyou'),
    ]