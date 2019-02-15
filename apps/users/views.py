# _*_ encoding: utf-8 _*_


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View

from users import models
from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from users.models import UserProfile, EmailVerifyRecord
# from utils.email_send import send_register_email
# Create your views here.
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin


class CustomBackends(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "账号尚未激活！"})

            else:
                return render(request, "login.html", {"msg": "账号或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})

# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get("username","")
#         pass_word = request.POST.get("password","")
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request,"login.html",{"msg": "用户名或密码错误！"})
#     elif request.method == 'GET':
#         return render(request, "login.html", {})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email = email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")

        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email","")
            try:
                if UserProfile.objects.get(email=email):
                    return render(request, "register.html", {"register_form": register_form, "msg": "邮箱已经存在！"})
            except UserProfile.DoesNotExist:
                pass
            password = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()

            send_status = send_register_email(email, "register")
            if send_status:
                return render(request, "login.html")
            else:
                return render(request, "register.html",{"register_form":register_form, "msg":"邮件发送失败"})
        else:
            return render(request, "register.html",{"register_form":register_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form":forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            try:
                if UserProfile.objects.get(email = email):
                    pass
            except UserProfile.DoesNotExist:
                return render(request, "forgetpwd.html",{"forget_form":forget_form, "msg":"用户并不存在"})
            send_status = send_register_email(email, "forget")
            if send_status:
                return render(request, "send_success.html")
            else:
                return render(request, "forgetpwd.html",{"forget_form":forget_form, "msg":"邮件发送失败"})
        else:
            return render(request, "forgetpwd.html", {"forget_form":forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html",  {"email": email, "active_code": active_code})
        else:
            return render(request, "active_fail.html")

class ModifyPwdView(View):
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)

        if modify_form.is_valid():
            #将active_code引入后，防止串改邮箱，修改其它用户密码！
            active_code = request.POST.get("active_code", "")
            all_records = EmailVerifyRecord.objects.filter(code=active_code)
            if all_records:
                for record in all_records:
                    email = record.email
                    break
            else:
                forget_form = ForgetForm()
                return render(request, "forgetpwd.html", {"forget_form": forget_form, "msg": "active_code无效，请从邮箱链接点开"})

            pwd1 = request.POST.get("password1","")
            pwd2 = request.POST.get("password2","")
            email = request.POST.get("email","")
            if pwd1 != pwd2:
                return render(request, "password_reset.html",{"email":email, "msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")
        else:
            email = request.POST.get("email","")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class UserinfoView(LoginRequiredMixin, View):
    """
    用户个人信息
    """
    def get(self,request):
        return render(request, 'usercenter-info.html', {

        })




