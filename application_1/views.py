from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import auth,User

class Home(View):
    def get(self,request):
        return render(request,'index.html')


class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print('Password match')
        else:
            print("passwrd dont match")
        
        return redirect('login')


class LogIn(View):
    def get(self,request):
        return render(request,'login_page.html')

    def post(self,request):
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name,password=password)

        if user is None:
            return redirect('/')
        
        auth.login(request,user)
        return render(request,'index.html')


class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')
