import uuid
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from myAuth.models import MyUser

# Create your models here.


class Ad(models.Model):
    cat = [
        ('phones', 'Phones and Tablets'),
        ('computers', 'Computers and Accessories'),
        ('cars', 'Cars'),
        ('home', 'Home and Kicthen'),
        ('babies', 'Kids and Toys'),
        ('electronic', 'Electronics'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=300)
    categories = models.CharField(max_length=300, choices=cat)
    location = models.CharField(max_length=100, default="Ilaro Ogun State")
    price = models.PositiveIntegerField()
    liked = models.ManyToManyField(
        MyUser, default=None, blank=True, related_name="liked")
    boosted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike")
)


class AdLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default="Like", max_length=10)

    def __str__(self):
        return str(self.ad.title)


class AdImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return str(self.ad.title)

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1200, 900))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super().save(*args, **kwargs)


class ForumPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=10000)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1200)
    on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class Artisan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default="Ilaro Ogun State")
    about = models.TextField(max_length=1500)
    job = models.CharField(max_length=60)
    rating = models.PositiveIntegerField(default=0, null=True)
    # facebook = models.URLField(max_length=50)
    # github = models.URLField(max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True)
    long = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.fullname


class GalleryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.artisan.user.fullname

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1200, 900))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super().save(*args, **kwargs)


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    message = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
