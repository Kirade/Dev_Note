# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.TemplateView):
    """
    데이터를 나열하는 것을 포함하지 않는
    일반적인 뷰를 보여주기 위해서 TemplateView 클래스를 사용한다.
    """
    template_name = 'web/index.html'

"""

1. URL 라우팅을 받아서 뷰 클래스로 온다.
2. 해당하는 뷰 클래스에서 적절한 템플릿, 모델등을 오버라이딩을 한다.

인덱스는 Product 모델에서 존재하는 상품들의 목록을 불러온뒤, 템플릿에 렌더링한다.

상품을 클릭하면, 상품의 디테일이므로 DetailView클래스를 이용하여 상품 상세를 표시한다.

상품을 주문할 때에는 주문을 관리하는 모델이 필요할 것 같다.
- 주문 목록 저장, 해당 주문 번호에 대한 사용자 매칭?
- 사용자 모델이 필요한가? 필요하다. : 마이페이지, 게시판 글쓰기 기능

게시판, 회원 모델 제작 ( 스키마 구성 )



"""


# 밑에는 예시 클래스
"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        Return the last five published questions (not including those set to be
        published in the future).

        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):

        Excludes any questions that aren't published yet.

        return Question.objects.filter(pub_date__lte=timezone.now())
"""