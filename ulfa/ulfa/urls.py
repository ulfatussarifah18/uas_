
from django.contrib import admin
from django.urls import include, path
from. import views
from blog import views as blogviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blogviews.fav),
    path('about/', include('about.urls')),
    path('', views.index),
]
