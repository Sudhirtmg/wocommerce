from django.shortcuts import render,get_object_or_404,redirect
from core.models import *
from django.db.models import Avg,Count
from taggit.models import Tag
from core.forms import ProductReviewForm
from django.http import JsonResponse
from django.contrib import messages
from cart.cart import Cart

# Create your views here.
def index(rq):
    # product=Product.objects.all().order_by('-id')
    product=Product.objects.filter(product_status='published',feature=True)

    context={
        'product':product,
    }
    return render(rq,'index.html',context)

def Product_List_View(rq):
    product=Product.objects.filter(product_status='published')
    context={
        'product':product
    }
    
    return render(rq,'core/product_list.html',context)
def Category_List_View(rq):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(rq,'core/category_list.html',context)
def Product_Category_List(rq,cid):
    category=Category.objects.get(cid=cid)
    product=Product.objects.filter(product_status='published',category=category)
    context={
        'category':category,
       'product':product

    }
    return render(rq,'core/product_category_list.html',context)
def ProductDetail(rq,pid):
    product=Product.objects.get(pid=pid)
    products=Product.objects.filter(category=product.category).exclude(pid=pid)
    p_image=product.p_image.all()
    reviews=ProductReview.objects.filter(product=product).order_by('-date')
    review_form=ProductReviewForm()
    context={
        'product':product,
        'p_image':p_image,
        'products':products,
        'review_form':review_form,
        'reviews':reviews,
    }
    return render(rq,'core/product-detail.html',context)
def product_tag(rq,slug_tag=None):
    product=Product.objects.filter(product_status='published',feature=True)
    tag=None
    if slug_tag:
        tag=get_object_or_404(Tag,slug=slug_tag)
        product=product.filter(tags__in=[tag])
    context={
        'product':product,
        'tag':tag
    }
    return render(rq,'core/tag.html',context)
def review(rq,pid):
    product=Product.objects.get(pk=pid)
    user=rq.user
    review=ProductReview.objects.create(
        user=user,
        product=product,
        review=rq.POST['review'],
        rating=rq.POST['rating'],
    )
    context={
        'user':user.username,
        'review':rq.POST['review'],
        'rating':rq.POST['rating'],
    }
    average_review=ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    return JsonResponse(
        {
            'bool':True,
            'context':context,
            'average_review':average_review,
        }
    )
# def search(rq):
#     titles=rq.GET.get('t')
#     min_price = rq.GET.get('min_price')
#     max_price = rq.GET.get('max_price')

#     name=Product.objects.filter(tags__name__icontains=titles).order_by('-date')
#     name=Product.objects.filter(description__icontains=titles).order_by('-date')
#     name=Product.objects.filter(price__icontains=titles).order_by('-date')

#     context={
#         'titles':titles,

#         'name':name,
#     }

#     return render(rq,'core/search.html',context)
def search(request):
    title = request.GET.get('t')
    description=request.GET.get('d')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Start with all products
    products = Product.objects.all()

    # Filter by title
    if title:
        products = products.filter(title__icontains=title)
    if description:
        products = products.filter(description__icontains=description)


    # Filter by price range
    if min_price and max_price:
        products = products.filter(price__range=(min_price, max_price))

    # Order the results by date
    products = products.order_by('-date')

    context = {
        'title': title,
        'min_price': min_price,
        'max_price': max_price,
        'products': products,
        'description':description,
    }

    return render(request, 'core/search.html', context)

# def add_to_cart(rq):
#     cart_product={}
#     cart_product[str(rq.GET['id'])]={
#         'quantity':rq.GET['quantity'],
#         'title':rq.GET['title'],
#         'price':rq.GET['price'],
#         'image':rq.GET['image'],
#         'pid':rq.GET['pid'],

#     }
#     if 'cart_data_obj' in rq.session:
#         if str(rq.GET['id']) in rq.session:
#             cart_data=rq.session['cart_data_obj']
#             cart_data[str(rq.GET['id'])]['quantity']=int(cart_product[str(rq.GET['id'])])
#             cart_data.update(cart_data)
#             rq.session['cart_data_obj']=cart_data
#         else:
#             cart_data=rq.session['cart_data_obj']
#             cart_data.update(cart_product)
#             rq.session['cart_data_obj']=cart_data
#     else:
#         rq.session['cart_data_obj']=cart_product
#     return JsonResponse({
#         'data':rq.session['cart_data_obj'],
#         'totalcartitem':len(rq.session['cart_data_obj'])
#     })
# def add_to_cart(rq):
#     product_cart={}
#     product_cart[str(rq.GET['id'])]={
#         'quantity':rq.GET['quantity'],
#         'title':rq.GET['title'],
#         'price':rq.GET['price'],
#         'image':rq.GET['image'],
#         'pid':rq.GET['pid'],
#     }
#     if 'cart_data_obj' in rq.session:
#         if str(rq.GET['id']) in rq.session:
#             cart_data=rq.session['cart_data_obj']
#             cart_data[str(rq.GET['id'])]['quantity']=int(product_cart[str(rq.GET['id'])])
#             cart_data.update(cart_data)
#             rq.session['cart_data_obj']=cart_data
#         else:
#             cart_data=rq.session['cart_data_obj']
#             cart_data.update(product_cart)
#             rq.session['cart_data_obj']=cart_data
#     else:
#         rq.session['cart_data_obj']=product_cart
#     return JsonResponse({
#         'data':rq.session['cart_data_obj'],
#         'totalcartitem':len(rq.session['cart_data_obj'])
#     })
# def cart_view(request):
#     cart_total_amount = 0
#     if 'cart_data_obj' in request.session:
#         for p_id, item in request.session['cart_data_obj'].items():
#             cart_total_amount += int(item['quantity']) * float(item['price'])
#         return render(request, "core/cart.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
#     else:
#         messages.warning(request, "Your cart is empty")
#         return redirect("index")
            
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'core/cart.html')

    









