from django.urls import path
from .views import index, contact,product, about, remot, video, productdetailView, videodetailView, remotdetailView

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name = 'contact'),
    path('product/', product, name = 'product' ),
    path('about/', about, name = 'about' ),
    path('remot/', remot, name = 'remot' ),
    path('product/<int:id>', productdetailView, name='productdetailView'),
    path('video/', video, name='video'),
    path('video/<int:id>', videodetailView, name='videodetailView'),
    path('remot/<int:id>', remotdetailView, name='remotdetailView'),
]
