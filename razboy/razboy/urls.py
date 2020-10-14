
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from myAuth.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication Routes
    path('', index_view, name="home"),
    path('register', register_view, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("me/", profile_view, name="profile"),
    path("editPic/", edit_pic_view, name="editPic"),
    path("editName/", edit_name_view, name="editName"),
    path("editEmail/", edit_mail_view, name="editEmail"),
    path("editPhone/", edit_phone_view, name="editPhone"),
    path("editPass/", edit_pass_view, name="editPass"),

    path("password_reset/", auth_views.PasswordResetView.as_view(),
         name="reset_password"),
    path("password_reset_sent/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password_reset_complete/",
         auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    # Ads Routes
    path("ads/", ads_view, name="ads"),
    path("like_ads/<str:pk>/", ads_like_view, name="like_ad"),
    path("ads/<str:id>/", ads_details_view, name="ads_details"),
    path("post_ad/", create_ad_view, name="create_ad"),
    path("editAd/<str:id>/", edit_ad_view, name="edit_ad"),
    path("editAdTitle/<str:id>/", edit_ad_title, name="edit_ad_title"),
    path("editAdDes/<str:id>/", edit_ad_des, name="edit_ad_des"),
    path("editAdPrice/<str:id>/", edit_ad_price, name="edit_ad_price"),
    path("editAdLoc/<str:id>/", edit_ad_loc, name="edit_ad_loc"),
    path("deleteAd/<str:id>/", delete_ad, name="delete_ad"),


    # Artisan Routes
    path("artisans/", artisan_view, name="artisan"),
    path("artisan_details/<str:id>/", artisan_detail_view, name="artisan_details"),
    path("editArtJob/<str:id>/", edit_art_job, name="edit_art_job"),
    path("editArtAddress/<str:id>/", edit_art_address, name="edit_art_address"),
    path("editArtAbout/<str:id>/", edit_art_about, name="edit_art_about"),
    path("newArtisan/", new_artisan, name="new_artisan"),


    # Blog Post Routes
    path("blogs/", blogs_view, name="blogs"),
    path("addBlog/", add_post_view, name="add_post_view"),
    path("blogs/<str:id>/", blog_details_view, name="blog_details_view"),
    path("new_comment/<str:id>/", new_comment, name="new_comment"),
    path("delPost/<str:id>/", del_post, name="del_post"),







    path('api/', include('api.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
