from . linkmysql import linkmysql
from . towords import towords
from . openkoapi import Judge
from . openkoapi import Passage
from . openkoapi import t
from django.http import HttpResponse
from . myemail import send
import json 
import qrcode
import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from demoapp.models import album
from demoapp.models import album_desc
from demoapp.models import album_user
from demoapp.models import imgs
from demoapp.models import praise
from demoapp.models import send
from demoapp.models import user
from django.db.models import F, Sum
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
def blog(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        article=data.getAllArticle()
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/blog-list.html',{"articles":article})
def sendemail(request):
        address=request.GET.get("semail")
        from_addr = '1697935859@qq.com'
        password = 'yokhrbcxhllleceg'
        to_addr = []
        to_addr.append(address)
        data=linkmysql("47.107.227.208","root","hismine","blog")
        data.addemail(address)
        smtp_server = 'smtp.qq.com'
        send(from_addr, password, to_addr, smtp_server, 'Hi, my name is Kitsch. Briefly introduce yourself here. You can also provide a link to the about page.', 'Welcome!', 'Hi')
        return HttpResponseRedirect("../blog/")
def article(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        id=request.GET.get("id")
        article=data.selectbyid(id)
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/blog-post.html',{"a":article})
def index(request):
        data=linkmysql("47.107.227.208","root","hismine","blog")
        
        article=data.getAllArticle()
         
#        return render(request, 'base.html',{"p":passage})
        return render(request, 'devblog/index.html',{"articles":article})
def about(request):
        return render(request,"devblog/about.html")
def add(request):
    password=''
    title=request.POST.get('title','')
    content=request.POST.get('content','')
    code=request.POST.get('code','')
    intro=request.POST.get('intro','')
    password=request.POST.get('password','')
    if password=="fan":
        print(password)
        data=linkmysql("47.107.227.208","root","hismine","blog")
        
        data.addarticle(title=title,code=code,content=content,intro=intro)
        from_addr = '1697935859@qq.com'
        pd = 'yokhrbcxhllleceg'
        to_addr = data.getallemail()
        
        
        smtp_server = 'smtp.qq.com'
        send(from_addr, pd, to_addr, smtp_server, '您关注的Kitsch ,发布了新文章', '新品达到!', 'Hi')
        return HttpResponseRedirect("../blog/")
    else:
        return render(request,"403.html")
def myadmin(request):
    
    return render(request,"devblog/admin2.html")
def get_recmd_imgs(request):#先用praise表找出点赞最高的几个表，然后使用album，album_desc，album_user等表返回需要的参数
        recmdImgs = []
        reasultTab = album.objects.get(praise.objects.get(num gt Avg).albumId)
        albumIdIn = reasultTab.albumId
        albumNameIn = reasultTab.albumName
        urlIn = reasultTab.albumUrl
        descIn = album_desc.objects.get(albumId = reasultTab.albumId).desc
        userIdIn = album_user.objects.get(albumId = reasultTab.albumId).userId
        dateIn = reasultTab.date
        praiseNumIn = praise.objects.get(num gt Avg).num
        recmdImgsBag = {albumIdIn,albumNameIn,urlIn,descIn,userIdIn,dateIn,praiseNumIn}#把结果放在列表里然后在发出去
        return render(request,"前端需求页面.html",{"recmdImgsBag":recmdImgsBag})
def send_praise(request):
        albumId = request.GET("albumId")
        username = request.GET("username")
        praise.objects.get(albumId = albumId).update(num = num + 1)
        newNum = praise.objects.get(albumId = albumId)
        return render(request,"前端请求页面.html",{"num":newNum})
def get_user_imgs(request):
        user_id = request.GET("userId")
        imgId = user_id.objects.create(userId = user_id, imgId = user_id.objects.get(Max(userId = user_id).imgId + 1))#新的图片id等于已有图片的最大id + 1
        url = "/demo/static/images"
        imgs.objects.create(pic = request.GET("图片"),imgId = imgId, imgUrl = url + imgId)
        date = imgs.objects.get(imgId = imgId).date
        return render(request , "前端请求页面.html", {"imgId":imgId,"url":url,"date":date})
def send_loginInfo(request):
        userName = request.GET("username")
        pwd = request.GET("pwd")
        permit = request.GET("permit")
        if user.objects.GET(userName = userName).DoesNotExist != True:
                if pwd == uer.objects.GET(userName = userName).pswd:
                        return render(request,"登陆成功.html")
                else return render(request,"当前页面.html"{"pwd":"密码错误"})
        else return render(request,"注册页面.html"{"userName":userName})
def send_registerInfo(request):
        userName = request.GET("username")
        npwd = request.GET("pwd")
        if userName == user.objects.GET(userName = userName) == True:
                return render(request, "当前页面.html", {"userName":"当前用户名已被注册"})
        else:
                user.objects.create(userId = user.objects.get(Max(userId).userId + 1),userName = userName, pwd = npwd)
                return render(request,"注册成功.html")
