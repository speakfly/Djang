from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
# Create your views here.
class UserForm(forms.Form):
    account  = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)

class PasswordForm(forms.Form):
	old_password  = forms.CharField(max_length = 20)
	new_password1 = forms.CharField(max_length = 20)
	new_password2 = forms.CharField(max_length = 20)

def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			account = uf.cleaned_data['account']
			password = uf.cleaned_data['password']
			users = User.objects.filter(account=account,password=password)
			if users:
				request.session['account'] = account
				return HttpResponseRedirect('/index/')
	uf = UserForm()
	return render(request,'login.html',{'uf':'uf'})

def index(request):
    account = request.session.get("account","anybody")
    users = User.objects.filter(account=account)
    if len(users) == 0:
        return HttpResponseRedirect('/login/')
    led_statu = users[0].led_statu
    return render(request,'index.html',{'led_statu':led_statu})

def logout(request):
	account = request.session.get("account","anybody")
	users = User.objects.filter(account=account)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	del request.session['account']
	return HttpResponseRedirect("/login/")

def updatepassword(request):
    account = request.session.get("account","anybody")
    users = User.objects.filter(account=account)
    if len(users) == 0:
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        uf = PasswordForm(request.POST)
        if uf.is_valid():
            old_password = uf.cleaned_data['old_password']
            new_password1 = uf.cleaned_data['new_password1']
            new_password2 = uf.cleaned_data['new_password2']
            if new_password1 != new_password2:
                return HttpResponse(u"两次密码不匹配")
            users = User.objects.filter(account=account,password=old_password)
            if len(users)==0:
                return HttpResponse(u"旧密码错误")
            User.objects.filter(account=account).update(password=new_password2)
            return HttpResponseRedirect('/index/')
    return render(request,'updatepassword.html')

def close_led(request):
    account = request.session.get("account","anybody")
	users = User.objects.filter(account=account)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
    User.objects.filter(account=account).update(led_statu=Flase)
    return HttpResponseRedirect('/index/')

def open_led(request):
    account = request.session.get("account","anybody")
	users = User.objects.filter(account=account)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
    User.objects.filter(account=account).update(led_statu=True)
    return HttpResponseRedirect('/index/')
