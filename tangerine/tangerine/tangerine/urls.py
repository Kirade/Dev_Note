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
"""

"""
^ 문자열이 시작할 때
$ 문자열이 끝날 때
\d 숫자
+ 바로 앞에 나오는 항목이 계속 나올 때
() 패턴의 부분을 저장할 때

usage)
r'^$' -> 아무 문자열이 없을때

"""


from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # admin 페이지 라우팅
    url(r'^admin/', admin.site.urls),

    # localhost:port 로 접근하는 모든 내용을 'web.urls'에서 처리하도록 라우팅
    url(r'', include('web.urls')),

]

