from django.shortcuts import render

# Create your views here.


def TecherPage(requests):
    return render(requests, 'teacher/index.html', {})