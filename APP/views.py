from django.shortcuts import render,redirect,HttpResponse
from APP import models
from APP import myforms
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from APP.serializers import UserInfoSerializers
from rest_framework.decorators import api_view
from django.views import View

class UserRequest(View):
    print('--------------------classViews(CBV)')
    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(UserRequest,self).dispatch(request,*args,**kwargs)
        print('after')
        return obj

    def get(self,request):
        print('request get ')
        return HttpResponse('........')
    def post(self,request):
        print('request post')
        return HttpResponse('........')



############FBV

def users(request):
    if request.method == "GET":
        userinfo = models.UserInfo.objects.all()
        serializer = UserInfoSerializers(userinfo,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        print("=============>")
        data = JSONParser().parse(request)
        serializer = UserInfoSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def users_detail(requset,pk):
    try:
        user = models.UserInfo.objects.get(pk=pk)
        print("users_detail:  ",dir(user))
    except Exception as e:
        return HttpResponse(status=404)
    if requset.method == "GET":
        serializer=UserInfoSerializers(user)
        return JsonResponse(serializer.data)
    if requset.method == "PUT":
        data = JSONParser().parse(requset)
        serializer = UserInfoSerializers(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    if requset.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)



def UserResgister(req):
    if req.method == "POST":
        data_from = myforms.UserRegister(req.POST)
        if data_from.is_valid():
            print("==========>",data_from.cleaned_data)
            data_from.clean_user()
            print("zou dao zhe le ")
        else:
            print(data_from.errors)
    else:
        data_from=myforms.UserRegister(initial={'username':'wangwu','password':'123123123'})
    return render(req,'UserRegister.html',{"forms":data_from})



def index(req):
    print('index')
    obj = render(req,'index.html')
    return obj

def user_index(request,name,uid):
    # v = request.COOKIES.get('username')
    v= request.session.get('username')
    print('---------COOKIES',v)
    if v:
        return render(request,'user.html',{'user_login':v})
    else:
        return render(request, 'login.html')


def UserLogin(request):
    if  request.method == "POST":
        user_login=request.POST.get('username')
        pwd_login =request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=user_login,password=pwd_login)[0]
        if obj:
            obj = redirect('/APP/user/{user}/{uid}'.format(user=user_login,uid=obj.nid))
            # obj.set_cookie(key='username',value=user_login,max_age=3,expires=3)
            request.session['username']=user_login
            # requset.session['password'] =pwd_login
            return obj
        else:
            print("账号密码错误")
            return render(request, 'login.html', {'msg':"账号密码错误"})
    return render(request, 'login.html')


def UserLogout(request):
    del request.session['username']
    # del request.session['password']
    return render(request,'login.html')

