from django.urls import path
from .views import car_recommendation, questionnaire

urlpatterns = [
    path('', questionnaire, name='questionnaire'),
    path('api/recommendations/', car_recommendation, name='car_recommendation'),
]
