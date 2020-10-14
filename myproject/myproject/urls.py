"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include, reverse
from django.conf import settings
from django.conf.urls.static import static
from rango import views
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return reverse('rango:register_profile')


urlpatterns = [
    path('',views.index,name='index'),
    path('rango/',include('rango.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
