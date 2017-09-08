from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form(request):
    form = forms.FormName(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print("Form validated")
            print(form.cleaned_data)
    return render(request, 'basicapp/form.html', {'form': form})

def modelform(request):
    form = forms.UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'basicapp/form.html', {'form': form})
