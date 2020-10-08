from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


def ads_view(request):
    qs = Ad.objects.all()
    data = []

    for ad in qs:
        imgs = AdImage.objects.filter(ad=ad.id)
        ads = {"ad": ad, "images": imgs}
        data.append(ads)
        paginator = Paginator(data, 4)
        page = request.GET.get('page')
        allads = paginator.get_page(page)
    context = {
        "data": allads,
    }
    # print(ads['ad']['title'])

    return render(request, 'ads/allads.html', context)


def ads_details_view(request, id):
    ad = get_object_or_404(Ad, id=id)
    imgs = AdImage.objects.filter(ad=ad.id)

    context = {
        "ad": ad,
        "images": imgs
    }

    return render(request, 'ads/adsDetails.html', context)


@login_required(login_url="login")
def ads_like_view(request, pk):
    ad = get_object_or_404(Ad, id=request.POST.get('ad_id'))
    ad.liked.add(request.user)
    return HttpResponseRedirect(reverse('ads_details', args=[str(pk)]))


@login_required(login_url="login")
def create_ad_view(request):
    if request.method == "GET":
        return render(request, "ads/newAd.html")
    else:
        data = request.POST
        cat = data.get("select")
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")
        location = data.get("location")
        boost = data.get("boosted")
        image1 = request.FILES['post-images1']
        image2 = request.FILES['post-images2']
        image3 = request.FILES['post-images3']
        image4 = request.FILES['post-images4']
        image5 = request.FILES['post-images5']
        images = [image1, image2, image3, image4, image5]
        print(images)
        if boost == "on":
            boosted = True
        else:
            boosted = False
        ad = Ad.objects.create(
            title=title,
            description=description,
            categories=cat,
            location=location,
            price=price,
            boosted=boosted,
            user=request.user
        )
        for img in images:
            im = AdImage.objects.create(
                ad=ad,
                image=img
            )
            im.save()
        ad.save()

        # return HttpResponseRedirect("ads_details", args=[str(ad.id)])
        return redirect("home")


def artisan_view(request):
    if request.user.is_authenticated == True:
        qs = Artisan.objects.exclude(user=request.user)
    else:
        qs = Artisan.objects.all()

    data = []

    for art in qs:
        imgs = GalleryImage.objects.filter(artisan=art.id)
        artisans = {"art": art, "images": imgs}
        data.append(artisans)
        paginator = Paginator(data, 4)
        page = request.GET.get('page')
        allart = paginator.get_page(page)
    context = {
        "data": allart,
    }
    # print(ads['ad']['title'])

    return render(request, 'artisan/allart.html', context)


def artisan_detail_view(request, id):
    artisan = get_object_or_404(Artisan, id=id)
    images = GalleryImage.objects.filter(artisan=artisan.id)
    context = {
        "artisan": artisan,
        "images": images
    }
    return render(request, "artisan/artDetails.html", context)
