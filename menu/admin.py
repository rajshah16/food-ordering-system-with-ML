from django.contrib import admin
from .models import Product
from .models import Customer
from .models import Order
from .models import OrderItem
from .models import Productbf
from .models import Productbev
from .models import Productchp
from .models import Productsoup
from .models import Productdessert
from .models import OrderItembf
from .models import OrderItembev
from .models import OrderItemchp
from .models import OrderItemsoup
from .models import OrderItemdessert


# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItembf)
admin.site.register(OrderItembev)
admin.site.register(OrderItemchp)
admin.site.register(OrderItemsoup)
admin.site.register(OrderItemdessert)
admin.site.register(Productbf)
admin.site.register(Productbev)
admin.site.register(Productchp)
admin.site.register(Productsoup)
admin.site.register(Productdessert)
