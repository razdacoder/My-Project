from rest_framework.decorators import api_view
from myAuth.models import MyUser
from .serial import *
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from main.models import Ad,AdImage,ForumPost,Comment,Artisan,GalleryImage

# Create your views here.
@api_view(['GET', ])
def getAllUsers(request):
	qs = MyUser.objects.all()
	serializer = UsersSerializer(qs, many=True)
	return Response(serializer.data)

@api_view(['GET', ])
def getUser(request, id):
	qs = MyUser.objects.get(pk = id)
	serializer = UsersSerializer(qs, many=False)
	return Response(serializer.data)
	
	
@api_view(['GET', ])
def getAllAds(request):
	qs = Ad.objects.all()
	print(qs)
	response = []
	
	for ad in qs:
		serializer = AdsSerializer(ad, many=False)
		imgs = AdImage.objects.filter(ad = ad.id)
		adimgs = AdImageSerializer(imgs, many=True)

		data = {"ad": serializer.data, "images": adimgs.data}
		response.append(data)
	return Response(response)
	


@api_view(['GET', ])
def getAd(request, id):
	try:
		qs = Ad.objects.get(pk = id)
		im = AdImage.objects.filter(ad = qs.id)
		serializer = AdsSerializer(qs, many=False)
		imgs = AdImageSerializer(im, many=True)
		response = {
		"ad": serializer.data,
		"images": imgs.data,
		"ok": True,
	}
		
	except Exception as e:
		response = {
			"ok": False,
			"msg": "Internal Server Error"
		}
	return Response(response)


@api_view(['POST', ])
def register(request):
	response =	{}
	if request.method == 'POST':
		data = request.data
		if data["pass1"] == data["pass2"]:
			if MyUser.objects.filter(email=data["email"]).exists():
				response = {'erorr': "Email already exsits"}
				return Response(response, status=status.HTTP_401_BAD_REQUEST)
			elif MyUser.objects.filter(phone=data['phone']).exists():
				response = {'erorr': "Phone Number already exsits"}
				return Response(response, status=status.HTTP_401_BAD_REQUEST)
			else:
				user = MyUser.objects.create_user(
				email=data['email'],
				fullname=data['fullname'],
				phone=data['phone'],
				password=data['pass1'])
				user.save()
				response = {'success': "User Created Sucessfully"}
				return Response(response, status=status.HTTP_201_CREATED)
		else:
			response = {'erorr': "Password do not match"}
			return Response(response, status=status.HTTP_401_BAD_REQUEST)


@api_view(['POST',])
def login_view(request):
	response = {}
	if request.method == 'POST':
		data = request.data
		email = data['email']
		password = data['password']
		
		user = authenticate(request,email=email,password=password)
		if user is not None:
			login(request,user)
			response = {'msg': "Login Succesfull" }
			return Response(response, status=status.HTTP_200_OK)

		else:
			response = {'erorr': "Invalid Username or Password"}
			return Response(response, status=status.HTTP_401_BAD_REQUEST)


@login_required()
@api_view(['GET', ])
def me(request):
	qs = MyUser.objects.get(email = request.user.email)
	serializer = UsersSerializer(qs,many=False)
	return Response(serializer.data)

@login_required()
@api_view(['GET'])
def logout_view(request):
	logout(request)
	response = { "msg": "Logout Sucessfull" }
	return Response(response, status=status.HTTP_200_OK)

	

@login_required()
@api_view(['POST'])
def post_ad(request):
	response = {}
	if request.method == 'POST':
		data =	request.data
		title = data["title"]
		des = data["des"]
		cat = data["cat"]
		loc = data["location"]
		price = data["price"]
		boosted = data["boosted"]
		imgs = data.getlist("images")
		
		ad = Ad.objects.create(
			title = title,
			description = des,
			categories = cat,
			location = loc,
			price = price,
			boosted = boosted,
			user = request.user
		)
		
		for i in imgs:
			im = AdImage.objects.create(
				ad = ad,
				image = i
			)
			
			im.save()
		ad.save()
		response = {"sucess":"Ad Created Sucessfully"}
		return Response(response,status=status.HTTP_201_CREATED)
		
		
@login_required()
@api_view(['PATCH'])
def editAd_price(request, id):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		price = data["price"]
		ad = Ad.objects.get(pk=id)
		ad.price = price
		ad.save()
		serializer = AdsSerializer(ad,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"ad": serializer.data
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)


@login_required()
@api_view(['PATCH'])
def edit_email(request):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		email = data["email"]
		user = MyUser.objects.get(email = request.user.email)
		user.email = email
		user.save()
		serializer = UsersSerializer(user,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"user": serializer.data
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)


@login_required()
@api_view(['PATCH'])
def editAd_title(request, id):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		title = data["title"]
		ad = Ad.objects.get(pk=id)
		ad.title = title
		ad.save()
		serializer = AdsSerializer(ad,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"ad": serializer.data,
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)
		
@login_required()
@api_view(['PATCH'])
def editPass(request):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		password = data["password"]
		user = MyUser.objects.get(email = request.user.email)
		user.set_password(password)
		user.save()
		serializer = UsersSerializer(user,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"user": serializer.data,
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)


@login_required()
@api_view(['PATCH'])
def editAd_des(request, id):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		des = data["des"]
		ad = Ad.objects.get(pk=id)
		ad.description = des
		ad.save()
		serializer = AdsSerializer(ad,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"ad": serializer.data,
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)
		


@login_required()
@api_view(['PATCH'])
def editAd_loc(request, id):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		loc = data["location"]
		ad = Ad.objects.get(pk=id)
		ad.location = loc
		ad.save()
		serializer = AdsSerializer(ad,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"ad": serializer.data,
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)
	
	
@login_required()
@api_view(['PATCH'])
def editPic(request):
	response = {}
	if request.method ==	'PATCH':
		data = request.data
		image = data["image"]
		im = Image.open(image)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (500,500) )
		im = im.convert('RGB')

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=100)
		output.seek(0)
		#change the imagefield value to be the newley modifed image value
		pic = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		
		user = MyUser.objects.get(email = request.user.email)
		user.photo = pic
		user.save()
		serializer = UsersSerializer(user,many=False)
		response = {
			"msg": "Updtated Succesfully",
			"user": serializer.data,
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)
	



@login_required()
@api_view(['DELETE'])
def delAd(request, id):
	response = {}
	if request.method ==	'DELETE':
		ad = Ad.objects.get(pk=id)
		ad.delete()
		serializer = AdsSerializer(ad,many=False)
		response = {
			"msg": "Deleted Succesfully",
			"ok": True
		  }
		  
		return Response(response,status=status.HTTP_201_CREATED)
		
		
@api_view(['GET'])
def getAllPost(request):
	qs = ForumPost.objects.all()
	serializer = PostSerializer(qs,many=True)
	return Response(serializer.data)
	


@api_view(['GET'])
def getPost(request, id):
	qs = ForumPost.objects.get(pk = id)
	qs.views += 1 
	serializer = PostSerializer(qs,many=False)
	return Response(serializer.data)
	
@api_view(['GET'])
def getMyPost(request):
	qs = ForumPost.objects.filter(user = request.user)
	serializer = PostSerializer(qs,many=True)
	return Response(serializer.data)

@login_required()
@api_view(['POST'])
def create_post(request):
	response = {}
	if request.method == 'POST':
		data = request.data
		post = ForumPost.objects.create(
			user = request.user,
			title = data["title"],
			body = data["body"],
			image = data.get('image', None)
		)
		post.save()
		
		serializer = PostSerializer(post, many=False)
		response =	{ 
			"msg": "Posted",
			"ok": True,
			"post": serializer.data
		 
		 }
		 
		return Response(response, status=status.HTTP_201_CREATED)
		
		
		
@api_view(['GET'])
def getComments(request, id):
	qs = Comment.objects.filter(post = id)
	serializer = CommentSerializer(qs, many=True)
	return Response(serializer.data)
	

@login_required()
@api_view(['POST'])
def newComment(request, id):
	if request.method ==	'POST':
		data = request.data
		post = ForumPost.objects.get(pk = id)
		comment = Comment.objects.create(
			post = post,
			user = request.user,
			comment = data['comment']
		)
		comment.save()
		serializer = CommentSerializer(comment,many=False)
		response = {
			"msg": "Posted",
			"ok":True,
			"comment": serializer.data
		}
		
		return Response(response,status=status.HTTP_201_CREATED)
	


@api_view(['GET'])
def getAllArtisan(request):
	qs = Artisan.objects.all()
	serializer = ArtisanSerializer(qs,many=True)
	return Response(serializer.data)
	

@api_view(['GET'])
def getArtisan(request, id):
	qs = Artisan.objects.get(pk = id)
	serializer = ArrisanSerializer(qs,many=False)
	return Response(serializer.data)


@login_required()
@api_view(['POST'])
def newArtisan(request):
	if request.method == 'POST':
		data = request.data
		links = request.data['links']
		link = links.split(",")
		images = data.getlist('image')
		artisan = Artisan.objects.create(
			user = request.user,
			job = data['job'],
			about = data['about'],
			address = data['address'],
			facebook = link[0],
			github = link[1]
		)
		artisan.save()
		for img in images:
			im = GalleryImage.objects.create(
				artisan = artisan,
				image = img
			)
			im.save()
		user = MyUser.objects.get(email = request.user.email)
		user.is_artisan = True
		user.save()
		response = {
			'msg': 'Created Succesfully',
		}
		
		return Response(response, status=status.HTTP_201_CREATED)
		

@login_required()
@api_view(['GET'])
def likeArtisan(request, id):
	artisan = Artisan.objects.get(pk = id)
	artisan.rating += 1
	artisan.save()
	response = {
		"msg": "Liked",
		"ok":True
	  }
	return Response(response)
	
	
	
@api_view(['GET'])
def search_view(request):
	query = request.query_params.get('q', None)
	ads = Ad.objects.filter(title__icontains = query) or Ad.objects.filter(categories__icontains = query)
	arts = Artisan.objects.filter(job__icontains = query)
	response = {}
	adres = []
	artres = []
	
	for ad in ads:
		serializer = AdsSerializer(ad, many=False)
		imgs = AdImage.objects.filter(ad = ad.id)
		adimgs = AdImageSerializer(imgs, many=True)

		data = {"ad": serializer.data, "images": adimgs.data}
		adres.append(data)
	
	for art in arts:
		serializer = ArtisanSerializer(art, many=False)
		imgs = GalleryImage.objects.filter(artisan = art.id)
		gal = GallerySerializer(imgs, many=True)

		data = {"art": serializer.data, "images": gal.data}
		artres.append(data)
		
	posts = ForumPost.objects.filter(title__icontains = query)
	serialize = PostSerializer(posts, many=True)
	response = {
		"ads": adres,
		"artisan": artres,
		"post": serialize.data
	}
	return Response(response)
	
	

def result():
    print(hi)
    pass