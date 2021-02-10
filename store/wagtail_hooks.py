from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    # ModelAdminGroup,
    modeladmin_register
)

from store.models import CategoryPage, ProductPage


class CategoryModelAdmin(ModelAdmin):
    model = CategoryPage
    menu_icon = "list-ul"
    menu_label = "Categories"
    menu_order = 100    # 000 refers to first menu order and so on
    list_per_page = 10
    list_display = ("title",)
    list_filter = ('title',)
    search_fields = ('title', 'active')


class ProductModelAdmin(ModelAdmin):
    model = ProductPage
    menu_icon = "list-ol"
    menu_label = "Products"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    list_display = ("title", 'category', 'price')
    list_filter = ('title', 'category', 'price')
    search_fields = ('title', 'category', 'price', 'inStock')
    
    
modeladmin_register(CategoryModelAdmin)
modeladmin_register(ProductModelAdmin)

    
    



