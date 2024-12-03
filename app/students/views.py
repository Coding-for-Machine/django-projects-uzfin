from django.shortcuts import render

# Create your views here.


def StudentPage(requests):
    return render(requests, 'student/index.html', {})