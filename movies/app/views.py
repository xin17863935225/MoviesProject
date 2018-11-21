import random

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
# 加密，验证模块
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login as login1, logout as logout1
from django.contrib.auth.decorators import login_required

from django.urls import reverse

from app.models import LoginImg, Movies, User, ShoppingCart


# Create your views here.
# 主页
def home(request, pagenum=1):
    movies = Movies.objects.all()
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '首页',
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'navlist/home.html', context=data)


# 电影
def movies(request, pagenum=1):
    movies = Movies.objects.all()
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        # 'movies': movies,
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '首页',
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'navlist/movies.html', context=data)


# 电视剧
def tvplay(request, pagenum=1):
    movies = Movies.objects.all()
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        # 'movies': movies,
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '首页',
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'navlist/tvplay.html', context=data)


# 综艺
def variety(request, pagenum=1):
    movies = Movies.objects.all()
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        # 'movies': movies,
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '首页',
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'navlist/variety.html', context=data)


# 动漫
def comic(request, pagenum=1):
    movies = Movies.objects.all()
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        # 'movies': movies,
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '首页',
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'navlist/comic.html', context=data)


# 搜索
def search_details(request, keyword, pagenum=1):
    # 获取搜索的内容
    if request.method == 'POST':
        keyword = request.POST.get('search', '')
    else:
        # keyword = request.args.get('search', '')
        keyword = keyword
    movies = Movies.objects.filter(Q(name__icontains=keyword) | Q(content__contains=keyword))
    # 将全部数据每5个分为一组
    pageInator = Paginator(movies, 5)
    # 当前页面
    currectpage = pageInator.page(pagenum)
    # 当前页面的数据
    moviespage = currectpage.object_list
    data = {
        # 'movies': movies,
        'currectpage': currectpage,
        'currectnum': int(pagenum),
        'pagerange': pageInator.page_range,
        'moviespage': moviespage,
        'title': '搜索' + keyword + '中...',
        'keyword': keyword,
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'movies/search_details.html', context=data)


# 电影详情
def movie_details(request, mvid):
    movie = Movies.objects.filter(id=mvid).first()
    # 将简介信息格式整理
    content = movie.content
    content = content.split('◎')
    content = '<br>◎'.join(content)
    # print(content)
    data = {
        'movie': movie,
        'content': content,
        'title': movie.name,
    }
    # 判断是否登录
    userid = request.session.get("user_id")
    # print(userid)
    if userid:  # 登录
        user1 = User.objects.filter(pk=userid).first()
        data['user1'] = user1
    return render(request, 'movies/movie_details.html', context=data)


# 注册
def signup(request):
    if request.method == 'GET':
        imgs = LoginImg.objects.all()
        imglist = []
        for img in imgs:
            # print(img.imgname)
            imglist.append(img.imgname)
        rdimg = random.choice(imglist)
        data = {
            'rdimg': rdimg,
            'title': '注册',
        }
        # 判断是否登录
        userid = request.session.get("user_id")
        # print(userid)
        if userid:  # 登录
            user1 = User.objects.filter(pk=userid).first()
            data['user1'] = user1
        return render(request, 'user/signup.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 加密
        password_hash = make_password(password, None, 'pbkdf2_sha256')
        # 存储数据库
        user = User()
        user.username = username
        user.password = password_hash
        user.save()
        # 重定向登录页面
        return redirect(reverse('movies:login'))


# 检查用户名唯一性
def checkUser(request):
    # 获取到客户端传入的用户名
    username = request.GET.get("username")
    # 检查数据库是否拥有该用户名
    resQuery = User.objects.filter(username=username)
    data = {}
    if resQuery.exists():  # 存在
        data["code"] = 901  # 表示已经存在
    else:
        data["code"] = 200  # 表示用户名可用
    # 返回json数据
    return JsonResponse(data)


# 登录
def login(request):
    if request.method == 'GET':
        imgs = LoginImg.objects.all()
        imglist = []
        for img in imgs:
            # print(img.imgname)
            imglist.append(img.imgname)
        rdimg = random.choice(imglist)
        data = {
            'rdimg': rdimg,
            'title': '登录',
        }
        # 判断是否登录
        userid = request.session.get("user_id")
        # print(userid)
        if userid:  # 登录
            user1 = User.objects.filter(pk=userid).first()
            data['user1'] = user1
        return render(request, 'user/login.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        resUser = User.objects.filter(username=username)
        if resUser.exists():  # 用户名存在
            user = resUser.first()
            # 验证密码
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect(reverse('movies:home', args=[1]))
        return redirect(reverse('movies:login'))


# 登出
def logout(request):
    request.session.flush()
    return redirect(reverse('movies:login'))


# 用户信息
def userInfo(request):
    if request.method == 'GET':
        data = {
        }
        # 判断是否登录
        userid = request.session.get("user_id")
        # print(userid)
        if userid:  # 登录
            user1 = User.objects.filter(pk=userid).first()
            data['user1'] = user1
        return render(request, 'user/userInfo.html', context=data)
    elif request.method == 'POST':
        pass

# 检查密码是否正确
def checkPassword(request):
    userid = request.session.get("user_id")
    oldpwd = request.GET.get("oldpwd")
    # 检查数据库是否拥有该用户名
    resQuery = User.objects.filter(id=userid).first()
    data = {}
    if check_password(oldpwd, resQuery.password):
        data["code"] = 200  # 表示正确
    else:
        data["code"] = 901  # 表示不正确
    # 返回json数据
    return JsonResponse(data)

# 修改密码
def update_password(request):
    userid = request.session.get("user_id")
    if request.method == 'GET':
        data = {}
        # 判断是否登录
        if userid:  # 登录
            user1 = User.objects.filter(pk=userid).first()
            data['user1'] = user1
        return render(request, 'user/update_password.html', context=data)
    elif request.method == 'POST':
        password = request.POST.get('password')
        # 加密
        password_hash = make_password(password, None, 'pbkdf2_sha256')
        # 存储数据库
        user = User.objects.filter(pk=userid).first()
        user.password = password_hash
        user.save()
        return redirect(reverse('movies:userInfo'))

# 删除购物记录
def deleteCart(request,cartid):
    delCart = ShoppingCart.objects.filter(pk=cartid).first()
    delCart.delete()
    return redirect(reverse('movies:userCard'))

# 买票
def buy(request):
    userid = request.GET.get('userid')
    movieid = request.GET.get('movieid')
    price = request.GET.get('price')
    quantity = request.GET.get('quantity')
    seats = request.GET.get('seats')
    userfor = User.objects.filter(id=userid).first()
    moviesfor = Movies.objects.filter(id=movieid).first()
    shopping = ShoppingCart()
    shopping.userid = userfor
    shopping.movieid = moviesfor
    shopping.price = price
    shopping.quantity = quantity
    shopping.seats = seats
    shopping.save()
    return render(request, 'user/userInfo.html')


# 付款二维码验证
def QRcode(request):
    paystatus = request.GET.get("paystatus")
    # mode = request.GET.get("mode")
    # 初次未支付
    if str(paystatus) == '0':
        with open('static/app/paystatus.txt', 'w') as f:
            f.write('901')
            f.close()
    # 获取最终支付状态
    elif str(paystatus) == '1':
        pass
    # 付款成功
    elif str(paystatus) == '2':
        with open('static/app/paystatus.txt', 'w') as f:
            f.write('200')
            f.close()
    with open('static/app/paystatus.txt', 'r') as f:
        payinfo = f.read()
        data = {"code": payinfo}  # 表示已经付款
        f.close()
    return JsonResponse(data)


# 购物车
def userCard(request):
    userid = request.session.get("user_id")
    shopMovies = ShoppingCart.objects.filter(userid=userid)

    user1 = User.objects.filter(pk=userid).first()
    data = {
        'user1': user1,
        'shopMovies': shopMovies,
    }
    return render(request, 'user/userCart.html', context=data)
