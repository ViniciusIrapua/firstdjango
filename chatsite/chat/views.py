from django.shortcuts import redirect, render
import hashlib
from .models import Register
from .forms import RegisterForm

# Create your views here.


def index(request):
    return render(request, 'chat/index.html')


def about(request):
    print('\n\n\n', request, '\n\n\n')
    return render(request, 'chat/about.html')


def contact(request):
    return render(request, 'chat/contacts.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print('\n\n\n', form_data, '\n\n\n')

            # Criptografa a senha com SHA-1
            sha1 = hashlib.sha1()
            sha1.update(form_data['password'].encode('utf-8'))
            hashed_password = sha1.hexdigest()

            add_register = Register(
                re_name=form_data['name'],
                re_email=form_data['email'],
                re_birth=form_data['birth'],
                re_password=hashed_password
            )

            add_register.save()

            return redirect('success')
    else:
        form = RegisterForm()

    return render(request, 'chat/register.html', {'form': form})


def success(request):
    return render(request, 'chat/success.html')
