from django.shortcuts import render
from modelForms.forms import NewUserForm
from modelForms.models import User

# Create your views here.
def index(request):
    return render(request, 'modelForms/index.html')

def signUp(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")

    return render(request, 'modelForms/signup.html', {'form': form})

def data(request):
    user_list = User.objects.all()
    return render(request, 'modelForms/data.html', {'all_users': user_list})

