from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(),name='index'),
    path('404', NumberPageView.as_view(),name='number'),
    path('about', AboutPageView.as_view(),name='about'),
    path('blog-single', BlogSinglePageView.as_view(),name='blog-single'),
    path('blog', BlogPageView.as_view(),name='blog'),
    path('contact', ContactPageView.as_view(),name='contact'),
    path('faq', FAQPageView.as_view(),name='faq'),
    path('home-2', Index2PageView.as_view(),name='index-2'),
    path('price', PricePageView.as_view(),name='price'),
    path('project', ProjectPageView.as_view(),name='project'),
    path('service', ServicePageView.as_view(),name='service'),
    path('single-project', SingleProjectPageView.as_view(),name='single-project'),
    path('team', TeamPageView.as_view(),name='team')
]
