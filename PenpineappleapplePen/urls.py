"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from .views import PostList
from django.urls import include
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path('', PostList.as_view(), name="index"),
    path('index.html', PostList.as_view(), name="index"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('Dop_obraz.html', views.Dop_obraz, name="Dop_obraz"),
    path('EGE_I_GIA.html', views.EGE_I_GIA, name="EGE_I_GIA"),
    path('Mattex_obesp.html', views.Mattex_obesp, name="Mattex_obesp"),
    path('Obr_model.html', views.Obr_model, name="Obr_model"),
    path('Obr_stand.html', views.Obr_stand, name="Obr_stand"),
    path('contact.html', views.contact, name="contact"),
    path('Gallery.html', views.Gallery, name="Gallery"),
    path('History.html', views.History, name="History"),
    path('SMI.html', views.SMI, name="SMI"),
    path('Team.html', views.Team, name="Team"),
    path('full-width.html', views.fullwidth, name="fullwidth"),
    path('sidebar.html', views.sidebar, name="sidebar"),
    path('faq.html', views.faq, name="faq"),
    path('404.html', views.error, name="error"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('About_adm.html', views.About_adm, name="About_adm"),
    path('Recomendation_adm.html', views.Recomendation_adm, name="Recomendation_adm"),
    path('Results_adm.html', views.Results_adm, name="Results_adm"),
    path('Stipendia_adm.html', views.Stipendia_adm, name="Stipendia_adm"),

]
