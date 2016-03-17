from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from app.menu.models import Product


class AddProductView(CreateView):
    model = Product
    fields = ["name", "category", "image", "price", "weight", "calorie", "tag",
              "about"]
    template_name = 'adm/menu/add_product_form.html'
    success_url = reverse_lazy("stuff:menu:new_product")

class ListProductsView(ListView):
    template_name = 'adm/menu/view_products.html'
    model = Product
    context_object_name = "products"
