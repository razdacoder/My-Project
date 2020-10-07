
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from myAuth.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication Routes
    path('', index_view, name="home"),
    path('register', register_view, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),


    # #Ads Routes
    path("ads/", ads_view, name="ads"),
    path("like_ads/<str:pk>/", ads_like_view, name="like_ad"),
    path("ads/<str:id>/", ads_details_view, name="ads_details"),




    path('api/', include('api.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
