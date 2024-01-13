from core.models import  *

def default(rq):
    categories=Category.objects.all()
    vendors=Vendor.objects.all()
    return {
        'categories':categories,
        'vendors':vendors
    }