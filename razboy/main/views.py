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
