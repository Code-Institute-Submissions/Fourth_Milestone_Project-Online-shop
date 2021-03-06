"""Fourth_Milestone_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from products import urls as urls_product
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT
from blog import urls as blog_urls
from home import urls as home_urls
from feed import urls as feed_urls
from search import urls as search_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls), name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cart/', include(urls_cart)),
    url(r'^products/', include(urls_product)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^blog/', include(blog_urls)),
    url(r'^feed/', include(feed_urls)),
    url(r'^search/', include(search_urls))
]
