"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from calculator.views import (
    cook,
    show_recipe_omlet,
    show_recipe_pasta,
    show_recipe_buter,
    show_recipe_soup,
    show_recipe_pilaf
)


urlpatterns = [
    path('cook/', cook),
    path('cook/omlet/', show_recipe_omlet),
    path('cook/pasta/', show_recipe_pasta),
    path('cook/buter/', show_recipe_buter),
    path('cook/soup/', show_recipe_soup),
    path('cook/pilaf/', show_recipe_pilaf),
]
