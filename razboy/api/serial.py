from rest_framework import serializers
from myAuth.models import MyUser
from main.models import *


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = '__all__'
	#	exclude = ['password', ]
	
class AdsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ad
		fields = '__all__'

class AdImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdImage
		fields = ['image', ]	
		
	

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = ForumPost
		fields = '__all__'
		

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
		

class ArtisanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artisan
		fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
	class Meta:
		model = GalleryImage
		fields = ['image']