from django.urls import path, re_path, include
from rango import views
from rango.views import AboutView, AddCategoryView, ProfileView

app_name = 'rango'

urlpatterns = [
    path('',views.index,name='index'),
    #path('rango/',include('rango.urls')),
    path('about/', AboutView.as_view(),name='about'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
    #path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    #path('logout/', views.user_logout, name='logout')
    #path('search/', views.search, name='search'),
    path('goto/', views.goto_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile' ),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category'),
    path('add/', views.auto_add_page, name='auto_add_page'),
    ]