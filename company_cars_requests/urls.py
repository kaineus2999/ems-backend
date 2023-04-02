from django.urls import path
from . import views

urlpatterns = [
    path("", views.Company_cars_requests.as_view()),
    path("<int:pk>", views.Company_cars_requestDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
    path("documents/", views.Documents.as_view()),
    path("documents/<int:pk>", views.DocumentDetail.as_view()),
]