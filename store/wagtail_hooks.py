from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    # ModelAdminGroup,
    modeladmin_register
)

from store.models import Product




class ProductModelAdmin(ModelAdmin):
    model = Product
    menu_icon = "list-ol"
    menu_label = "Products"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    list_display = ("title",'price')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price', 'inStock')
    
    
modeladmin_register(ProductModelAdmin)



    
    



