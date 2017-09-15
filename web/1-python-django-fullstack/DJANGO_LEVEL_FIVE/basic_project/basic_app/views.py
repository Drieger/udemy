from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserForm, UserProfileInfoForm


def index(request):
    """Index view."""
    return render(request, 'basic_app/index.html')


def user_login(request):
    """Log in view."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('Login failed')
    return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    """Log out view."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    """Profile page."""
    return HttpResponse('You\'re logged in')


def register(request):
    """Register view."""
    user_form = UserForm(request.POST or None)
    profile_form = UserProfileInfoForm(
        request.POST or None,
        request.FILES or None
    )
    registered = False
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            # Save user model information
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            # Save user profile model information
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            # Inform context that user was registered
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    return render(request, 'basic_app/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })