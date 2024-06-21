from django.urls import path
from quiz.views import *

urlpatterns = [
    path('', home),
    path('create/', create ),
    path('pdf/', pdf ),
    path('json/', json ),
    path('bg/', bg ),
]
