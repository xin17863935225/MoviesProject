from django.conf.urls import url

from app import views

urlpatterns = [
    # 导航栏分类内容
    url(r'^home/pagenum=(\d*)/', views.home, name='home'),
    url(r'^movies/pagenum=(\d*)/', views.movies, name='movies'),
    url(r'^tvplay/pagenum=(\d*)/', views.tvplay, name='tvplay'),
    url(r'^variety/pagenum=(\d*)/', views.variety, name='variety'),
    url(r'^comic/pagenum=(\d*)/', views.comic, name='comic'),
    url(r'^search_details/keyword=(\w*)pagenum=(\d*)/',views.search_details,name='search_details'),
    # 电影详情
    url(r'^movie_details/mvid=(\d*)/', views.movie_details, name='movie_details'),
    # 用户相关
    url(r'^signup/', views.signup,name='signup'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', views.logout,name='logout'),
    url(r'^checkUser/',views.checkUser),  # 检查用户名唯一性的
    url(r'^checkPassword/', views.checkPassword),  # 检查用户名唯一性的
    url(r'^userInfo/', views.userInfo, name='userInfo'),
    url(r'^update_password/', views.update_password, name='update_password'),
    # 购物
    url(r'^buy/',views.buy,name='buy'),
    url(r'^QRcode/',views.QRcode,name='QRcode'),
    url(r'^userCard/', views.userCard, name='userCard'),
    url(r'^deleteCart/cartid=(\d*)/', views.deleteCart, name='deleteCart'),


]
