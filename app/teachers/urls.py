from django.urls import path
from .views import TecherPage

app_name = "teachers"

urlpatterns = [
    path("", TecherPage, name='techers'),
]
