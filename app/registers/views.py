from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm,  ProfileEditForm
from django.contrib import messages
# Create your views here.
from .models import Profile,  User


def edit(request, id):
    user = get_object_or_404(User, id=id)
    profile = getattr(user, 'profile', None)  # Foydalanuvchining profilini olish yoki bo'shligini tekshirish

    # Agar profil mavjud bo'lmasa, yangi profil yaratish
    if not profile:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)  # Profilni formaga qo'shish
        if form.is_valid():
            form.save()  # Formani saqlash
            messages.success(request, "Profile successfully updated!")
            return redirect('quizes:quizlist')  # Saqlashdan keyin redirect qilish
        else:
            messages.error(request, "Form contains errors. Please fix them.")
            print(form.errors)  # Formadagi xatolarni ko'rsatish
    else:
        form = ProfileEditForm(instance=profile)  # Profil bilan forma yaratish

    return render(request, 'authuser/edit.html', {'form': form})

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('teachers:techers')
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga kirgansiz.") # message
                return redirect('quizes:quizlist')
            else:
                messages.debug(request, 'Siz Ro\'yhatdan o\'tmagansiz?')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', context={"form":form})

def LogoutPage(request):
    if request.POST:
        logout(request)
        messages.success(request, "Siz tizimdan chiqdingiz!")
        return redirect('users:login')
    else:
        return render(request, 'logout.html',{})