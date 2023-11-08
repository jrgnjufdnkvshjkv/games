from django.http import Http404
from django.shortcuts import render
from .models import Product, Contact, Remot, Video, Comment
# Create your views here.

def product(request):
    video = Video.objects.all
    remot = Remot.objects.all
    comments = Comment.objects.all
    context = {
        'video':video,
        'remot':remot,
         'comments':comments
    }
    return render(request, "product.html", context=context)



def videodetailView(requests, id):
   try:
         video = Video.objects.get(id=id)
         context = {
           "video": video
            }
   except video.DoesNotExist:
        raise Http404("No video found")
   return render(requests, "videodetail.html", context=context)


def remotdetailView(requests, id):
   try:
         remot = Remot.objects.get(id=id)
         context = {
           "remot": remot
            }
   except remot.DoesNotExist:
        raise Http404("No remot found")
   return render(requests, "remotdetail.html", context=context)


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "index.html", context=context)

def contact(request):
    contact = Contact.objects.all()
    context = {
        'contacts': contact
    }
    return render(request, "contact.html", context=context)

def about(request):
    return render(request, "about.html", context={})

def remot(request):
      remot = Remot.objects.all
      context = {
          'remot': remot
      }
      return render(request, "remot.html", context=context)

def video(request):
    video = Video.objects.all
    context = {
        'video': video
    }
    return render(request, "video.html", context=context)

def productdetailView(requests, id):
   try:
         product = Product.objects.get(id=id)
         context = {
           "product": product
        }
   except product.DoesNotExist:
        raise Http404("No product found")
   return render(requests, "product_detail.html", context=context)

