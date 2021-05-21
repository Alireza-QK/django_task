from django.shortcuts import render, redirect

from .forms import UserRegisterForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

from .models import User
from django.http import HttpResponse


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, "Not found like this user")
    return render(request, 'account/login.html')


def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Account with email'
            message = render_to_string(
                'registration/account_activation.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/account_send_activation.html')

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
        print(uid)
        print(user)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
    else:
        return HttpResponse('Activation link is invalid!')
