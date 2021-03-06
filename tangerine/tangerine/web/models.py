# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    """
    name : 상품의 이름
    price : 상품의 가격
    inventory : 상품 재고 수
    detail : 상품 설명 (optional)
    """
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    inventory = models.IntegerField()
    detail = models.TextField(null=True)

    def is_empty(self):
        if self.inventory <= 0:
            return True

    def __str__(self):
        return self.name


# class User(AbstractUser):
#     """
#     기본 장고 User 모델을 상속받아 주소와 연락처 추가한 모델
#     address : 기본 배송 주소
#     contact : 연락처
#     """
#     address = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)


class Board(models.Model):
    """
    title : 게시글 제목
    writer : 게시글 작성자
    date : 게시글 작성 날짜
    content : 게시글 내용
    board_password : 게시글 비밀번호
    """
    title = models.CharField(max_length=100)
    # writer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField()
    content = models.TextField()  # 나중에 UI 패드 적용가능 (생활코딩 참조)
    board_password = models.CharField(max_length=100)

    def __str__(self):
        return self.title

