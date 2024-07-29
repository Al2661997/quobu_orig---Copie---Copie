from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('ask_question', views.ask_question, name = 'ask_question'),
    path('answer/<str:i_question>/', views.answer, name = 'answer'),
    path('afficher/<int:pk>/', views.afficher, name = 'afficher'),
    path('j_aime/<str:i_body>/', views.j_aime, name = 'j_aime'),
    path('je_n_aime_pas/<str:i_body>/', views.je_n_aime_pas, name = 'je_n_aime_pas'),
]