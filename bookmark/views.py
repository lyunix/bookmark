from django.shortcuts import render

# Create your views here.

# MTV : 디자인 패턴
# 디자인 패턴: 설계상의 문제를 해결하기 위해 나온 방
# M : Model - 데이터베이스를 쉽게 사용하려고
# T: Template - HTML 같이 프론트코드
# V: View - 로직, 기능 같은 백엔드 코드

# 리스트 페이지

# 뷰 안에서 진행되는 일들
# 데이터베이스에서 북마크들을 불러온다 - 모델
# 해당 북마크를 템플릿에 넣어 가공한다. - 로직
# 가공한 결과 코드를 사용자(브라우저)에게 전달한다. - 로직

# 뷰 : 2종류
# 클래스형 뷰 : class 형태 - 보통 하는 일
# 보통 하는 일 뷰 : 장고에서 미리 만들어 뒀다. Generic View - Class Based View
# CRUD : Create Read Update Delete

# 함수형 뷰 : def 형태 - 내가 혼자 지지고 볶고 하고 싶을 때

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Generaic 뷰의 기본 템플릿 규칙
# 1. 앱 폴더 하위 templates 폴더 안에 모델 이름을 가진 폴더에서 찾는다.
# - bookmark/templates/bookmark/?
# 2. ListView - 모델명_list.html : bookmark_list.html
# CreateView, UpdateView - 모델명_form.html: bookmark_form.html


# 클래스형 뷰를 사용해도 옵션은 존재
from .models import Bookmark

class BookmarkListView(ListView) :
    model = Bookmark
    paginate_by = 3

from django.urls import reverse_lazy


# 함수형 뷰: 기능 자체를 직접 만들고 싶을때
# 클래스형 뷰: 기존에 많이 사용하는 기능을 그대로 상속받아서
# Ajax 뷰 - JsonResponse, HttpResponse

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 글쓰기를 완료했을때 이동할 페이지
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'
    # reverse : URL 패턴 이름을 가지고 URL 을 만드는 함수
    # reverse_lazy : URL 패턴 이름을 가지고 URL을 만드는 함수 - lazy 지연평가
    # 클래스형 뷰: 무조건 reverse_lazy를 사용한다.
    # 클래스 형 뷰가 URLConf 로드 전에 평가 된다.
    # 장고 애플리케이션 구동이 될 때 URLConf를 로드




