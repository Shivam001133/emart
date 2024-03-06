from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
from .models import Product
from haystack.query import SearchQuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from haystack.backends.whoosh_backend import WhooshEngine



def home(request):
    product_info = request.GET.get("product_info")
    print("************", product_info)
    if product_info:
        queryset = SearchQuerySet().filter(content=product_info).exclude(content="adfadf").models(Product)

    else:
        queryset = Product.objects.all()
    if queryset:
        paginator = Paginator(queryset, 4)
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = paginator.page(paginator.num_pages)
    return render(request, 'emart/list.html', {"context": page_obj})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'emart/detail.html'
