# coding=utf-8
"""tangerine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

* Regex Usage

^post/(?P<pk>[0-9]+)/$ 이 부분이 무섭게 보이지만, 걱정하지 마세요. 하나씩 차근차근 설명해드릴 거에요.

^은 "시작"을 뜻합니다.
첫 부분 다음부터 나오는 post/는 URL이 post 를 포함해야한다는 것을 뜻합니다. 아직까지 할 만 하죠?
(?P<pk>[0-9]+) - 이 부분은 좀 까다롭습니다. 이 정규 표현식의 의미는 장고가 여러분이 여기에 넣은 모든 것을 pk변수에 넣어 뷰로 전송하겠다는 뜻입니다. [0-9]은 문자를 제외하고, 숫자 0부터 9까지 하나의 숫자만 있다는 뜻입니다. +는 하나 또는 그 이상의 숫자가 와야한다는 것을 의미합니다. 따라서 http://127.0.0.1:8000/post//라고 하면 post/ 다음에 숫자가 없기 때문에 해당이 안되지만, http://127.0.0.1:8000/post/1234567890/는 완벽하게 매칭됩니다.
/ - 다음에 / 가 한번 더 와야 한다는 의미입니다.
$ - "마지막"! 입니다. 그 뒤로 더이상 문자가 오면 안됩니다.

"""

from django.conf.urls import url, include

from . import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.ProductView.as_view(), name="detail"),
    url(r'^intro/$', views.IntroView.as_view(), name="intro"),
    url(r'^board/$', views.BoardView.as_view(), name="board"),
    url(r'^register/$', views.UserCreateView.as_view(), name="register"),
    url(r'^register_ok/$', views.UserCreateDone.as_view(), name="register_ok"),
    #url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name="login"),
    url(r'^(?P<user_id>[0-9]+)/logout/$', views.logout, name="logout"),
#    url(r'^mypage/(?P<pk>[0-9]+)/$', views.MypageView.as_view(), name="mypage"),

]


