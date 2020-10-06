
from django.urls import path

from myAuth.views import *
from main.views import *
from .views import *

urlpatterns = [
	#Auth
	path('register/', register),
	path('login/', login_view),
	path('logout/', logout_view),
	
	#Users
	path('me/', me),
	path('editEmail/', edit_email),
	path('editPass/', editPass),
	path('editPic/', editPic),
    path('getAllUsers/', getAllUsers ),
    path('getUser/<str:id>/', getUser),
    
   
    
      #Ads
    path('getAllAds/', getAllAds),
    path('getAd/<str:id>/', getAd),
    path('postAd/', post_ad),
    path('editAd_price/<str:id>/',editAd_price),
    path('editAd_title/<str:id>/',editAd_title),
    path('editAd_des/<str:id>/',editAd_des),
    path('editAd_loc/<str:id>/',editAd_loc),
    path('deleteAd/<str:id>/', delAd),
    
    
    #Forum
    path('getAllPost/', getAllPost),
    path('getPost/<str:id>/', getPost),
    path('getMyPost/', getMyPost),
    path('createPost/', create_post),
    
    
    #Comment
    path('getComments/<str:id>/', getComments),
    path('newComment/<str:id>/', newComment),
    
    
    #Artisan
    path('getAllArtisan/', getAllArtisan),
    path('getArtisan/<str:id>/', getArtisan),
    path('newArtisan/', newArtisan),
    path('likeArtisan/<str:id>/', likeArtisan),
    
    
    #Filter
    path('search/', search_view),
    
]



