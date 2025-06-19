# **1~4 일차 요약 정리**
---
## **1일차 - Django에 대해, 프로젝트 세팅**
#### **Django**
    - Django는 파이썬으로 작성된 오픈 소스 웹 프레임워크로, 웹 애플리케이션 개발을 빠르고 쉽게 할 수 있도록 도와줍니다.
    - Django는 MTV(Model-Template-View) 아키텍처를 기반으로 하며, 보안, 확장성, 재사용성을 강조합니다.
    - 기본적인 기능들이 이미 내장되어 있어 빠르게 개발을 시작할 수 있습니다.
    - 강력한 ORM 기능으로 데이터베이스 작업이 편리합니다.
#### **프로젝트 세팅 순서**
    1. 가상환경 생성을 위한 Poetry 설치
    2. 프로젝트를 진행할 폴더 생성 후 폴더 내에서 'poetry init' 으로 초기화 진행 후 가상환경에 Django 설치
        - poetry 설치 시 .venv 폴더가 프로젝트 내에 생성이 되지 않으면 순서대로 코드 입력 후 파이참 재시작
            poetry config virtualenvs.in-project true
            poetry config virtualenvs.path "./.venv"
    3. 가상환경에서 Django 프로젝트 생성
        - poetry run django-admin startproject 프로젝트명

        - 수업들으면서 많이 썼던 명령어 (python manage.py ~)
            - startapp appname : 앱을 생성합니다.
            - runserver : 서버를 실행합니다.
            - createsuperuser : 관리자를 생성합니다.
            DB 업데이트
            - makemigrations (appname) : app의 모델 변경 사항 체크합니다.
            - migrate : 변경 사항을 DB에 반영합니다.
---
## **2일차 - URL, view, Model 개념**

#### **URL Dispatcher(urls.py)**
    URL Dispatcher는 Django의 URL 라우팅 시스템으로 Django 웹 프레임워크의 핵심 구성 요소 중 하나이며,
    웹 요청을 처리하고 해당 요청에 맞는 View 함수로 라우팅하는 역할을 한다.
    * 'Dispatcher'란, 어떤 요청이나 정보를 받아 적절한 목적지 또는 처리 절차로 전달하는 역할을 하는 컴포넌트를 지칭하는 언어로 사용한다.

#### **views.py**
    일치하는 URL 패턴을 찾으면, URL Dispatcher는 해당 URL 패턴에 연결된 View 함수를 호출한다.
    view 함수는 HTTP 요청을 처리하고 응답을 반환합니다.

#### **urls.py의 구조**
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls), = 'admin/' URL로 사이트에 접근
        path('feeds/', include("feeds.urls")),
    ]

#### **Model의 개념**
    Model은 Django의 웹 애플리케이션의 데이터 구조를 정의하고, ORM(Object-Relational Mapping) 시스템을 사용하여 데이터베이스와 간편하게 상호작용을 할 수 있다.
    (DB로 치면 테이블과 같은 개념이다.)
    * ORM(Object-Relational Mapping)란, 모델을 통해 CRUD (Create, Read, Update, Delete) 작업을 SQL 쿼리를 작성하지 않고도 수행할 수 있도록 해주는 기술이다.

##### **models.py의 구조**

    class Board(CommonModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
    user = models.ForeignKey('users.user',on_delete=models.CASCADE)

### **모델 사용**
    - 마이그레이션: 모델을 정의하거나 변경한 후에는 **`makemigrations`**와 **`migrate`** 명령어를 사용하여 데이터베이스 스키마를 생성하거나 업데이트해야 합니다.
    - 데이터 조작: Django 셸을 사용하거나 View 내에서 모델을 임포트하여 데이터를 생성, 조회, 수정, 삭제할 수 있습니다.

### **수업하면서 많이 사용한 모델 필드**
    - **CharField** : 짧은 문자열을 저장할 때 사용한다. max_length 파라미터가 필요함
    - **TextField**: 긴 문자열을 저장하는 데 사용한다. 문자열 길이 제한이 없슴
    - **DateField**: 날짜를 저장합니다. **`auto_now`**와 **`auto_now_add`** 옵션을 사용할 수 있다.
    - **DateTimeField**: 날짜와 시간을 저장한다.
    - **ForeignKey**: 다른 모델에 대한 링크를 나타내며, 일대다 관계를 가진다.
                  on_delete=models.CASCADE는 게시글(Post)이 삭제될 때 해당 게시글에 속한 댓글(Comment)도 함께 삭제시킨다.
    - **OneToOneField**: 다른 모델에 대한 일대일 관계를 나타낸다.
    - **ManyToManyField**: 다른 모델에 대한 다대다 관계를 나타냅니다.
    ** 선택 사항 및 추가 기능 **
    - null=True: 데이터베이스에서 해당 필드가 NULL 값을 가질 수 있음을 의미한다.
    - blank=True: 폼에서 해당 필드를 비워둘 수 있음을 의미한다.
    - default: 필드의 기본값을 설정한다.
    - unique=True: 필드의 모든 값이 고유해야 함을 나타낸다.
---
## **3일차 - Admin Pannel관리, custom_admin**
#### **Admin Pannel**
    Admin Pannel은 웹 애플리케이션의 데이터를 관리할 수 있는 강력한 도구이며,
    Admin Pannel을 사용하면 모델 데이터를 쉽게 추가, 수정, 삭제할 수 있다.
    Admin Pannel은 기본적으로 Django 프로젝트에 포함되어 있으며, 관리자 계정을 생성하고 모델을 등록하여 사용할 수 있다.

#### **Admin Pannel 활성화 방법**
    1. 관리자 인터페이스 활성화 - settings.py 파일에서 INSTALLED_APPS에 'django.contrib.admin'이 있는지 확인
    2. 모델을 관리자 페이지에 등록 - 추가 하고 싶은 모델을 만든 후 admin.py 파일에 등록
    3. 관리자 계정을 생성 - python manage.py createsuperuser
    4. 관리자 페이지 접 - python manage.py runserver
#### **관리자 페이지 커스텀 방법**
    class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer','date', 'likes', 'reviews', 'content', 'updated_at', 'created_at') # 목록에 표시할 필드
    list_filter = ('likes', 'reviews') # 필터링 옵션
    search_fields = ('title', 'content') # 검색 필드
    ordering = ('date',) # 정렬 기준
    readonly_fields = ('writer',) # 읽기 전용 필드
    fieldsets = ( # 필드 그룹화
        (None, {'fields': ('title', 'content')}), # 기본 필드 그룹
        ('추가 옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}), # 추가 옵션 그룹
    )
    list_per_page = 10 # 페이지당 표시할 항목 수

#### **custom_admin**
    기본 Admin Pannel을 커스터마이징하여, 관리자가 데이터 관리 화면을 더 편리하게 사용할 수 있도록 변경하는 것을 의미한다.
    목록에 표시할 필드, 필터, 검색, 읽기 전용, 필드 그룹화 등 다양한 옵션을 admin.ModelAdmin 클래스를 상속받아 설정할 수 있다.
    이렇게 하면 관리자 페이지가 프로젝트의 요구에 맞게 맞춤화되어 효율적인 데이터 관리를 할 수 있다.
    * AbstractUser란, Django의 기본 User 모델의 기능을 상속받아 활용할 수 있게 해주는 클래스이다.
#### **custom_admin 만드는 순서**
    1. models.py에서 AbstractUser를 상속받아 사용자 모델을 정의한다.
    2. settings.py에서 AUTH_USER_MODEL을 커스텀 사용자 모델로 설정한다.
    3. users/migrations 폴더에서 숫자로 시작하는 파일 및 현재 생성되어 있는 데이터베이스를 삭제한다.
    4. makemigrations와 migrate 명령어를 실행한다.
    5.데이터베이스를 삭제하였으므로 createsuperuser 명령어로 관리자 계정을 다시 생성한다.
    6. users/models.py 를 수정하여 사용자 모델을 정의한다. -> 이 후 makemigrations를 다시 진행한다.
    7. common app을 생성하고, CommonModel 클래스를 정의한다(created_at, updated_at).
    8. 그 후 모델들의 상속 클래스들을 수정한다.
    9. DB에 반영 후 admin.py에서 커스터마이징한다.
---칟ㅁ
## **4일차 - ORM**
#### **ORM(Object-Relational Mapping)**
    객체 지향 프로그래밍 (클래스) <=== MAPPING ===> 관계형 데이터베이스 (테이블)
    - Object = 객체(Django)
    - Relational = 관계형 데이터베이스(MySQL, PostgreSQL 등) RDBMS
    - Mapping = 매핑(객체와 RDBMS의 연결을 도와주는 것)

#### *콘솔 들어가는 방법*
    - python manage.py shell

#### **QuerySet**
    QuerySet은 데이터베이스 쿼리를 표현 및 생성하는 도구이다.
    ** 수업들으면서 사용한 함수 **
    - filter(): 특정 조건에 맞는 객체를 필터링하여 출력해준다.
    - all(): 모든 객체를 출력한다.
    - get(): 특정 조건에 맞는 단일 객체를 출력한다.
    - count(): 객체의 개수를 출력한다.

#### **reverse accessors**
    관계를 역참조로 원하는 데이터를 조회할 수 있도록 도와주는 기능이다.(상속받은 쪽이 아닌 상속을 해주는 쪽에서 데이터를 찾을 수 있도록 해주는 기능)
---
## 실습 사진
![실습 사진](./images/실습사진.png)