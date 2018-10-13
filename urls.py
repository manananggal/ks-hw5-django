from django.urls import path

import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('blog', views.blog),
    path('projects', views.projects),
    path('github', views.github_api),
]


from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
