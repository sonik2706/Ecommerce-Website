from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm, UserLoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Moda Wólka Activate your account.'
            message = render_to_string('user/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request,'Proszę potwierdzić swój adres e-mail, aby zakończyć rejestrację.')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'user/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        message = 'Dziękujemy za twoje potwierdzenie mailowe. Teraz możesz zalogować się na swoje konto.'
        context = {'messages': message}
        return render(request, "user/login.html", context)
    else:
        message = 'Link aktywacyjny jest nieprawidłowy!'
        context = {'messages': message}
        return render(request, "user/login.html", context)
