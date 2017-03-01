# coding=utf-8
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Product, Client, Board


class IndexView(generic.ListView):
    """
    데이터를 나열하는 것을 포함하지 않는
    일반적인 뷰를 보여주기 위해서 TemplateView 클래스를 사용한다.
    """
    template_name = 'web/index.html'
    context_object_name = 'product_list'

    # 제고 수량이 없으면 인덱스 페이지에서 아예 없애는 것이 아니라, 재고 없음으로 표시할 수 있게 만들자
    def get_queryset(self):
        return Product.objects.filter(

        )


class ProductView(generic.DetailView):
    """
    데이터의 세부사항을 표현하기위해
    DetailView 클래스를 사용한다.
    """
    model = Product
    template_name = 'web/detail.html'

    def get_queryset(self):
        return Product.objects.filter(
            # 필터기능 - 필요하면 추가
        )


class IntroView(generic.TemplateView):
    template_name = 'web/intro.html'


class BoardView(generic.ListView):
    template_name = 'web/board.html'

    def get_queryset(self):
        return Board.objects.filter(

        )

"""
class MypageView(generic.DetailView):
    model = Client
    template_name = 'web/mypage.html'

    def get_queryset(self):
        return Client.objects.filter(

        )
"""

def check_id(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    #test_session = json.dumps(request.session)

    return render(request,'web/mypage.html', {
        'client_id': client_id,
        'message': "message context에 들어간 정보입니다.",
        #'session': test_session
    })
    # return HttpResponseRedirect(reverse('web:mypage', args=(client.id,)))


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