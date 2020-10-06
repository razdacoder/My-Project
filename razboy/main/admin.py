from django.contrib import admin
from .models import Ad,AdImage,ForumPost,Comment,Artisan,GalleryImage,Contact,AdLike
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Ad)
admin.site.register(AdImage)
admin.site.register(ForumPost)
admin.site.register(Comment)
admin.site.register(Artisan)
admin.site.register(GalleryImage)
admin.site.register(Contact)
admin.site.register(AdLike)

admin.site.unregister(Group)

