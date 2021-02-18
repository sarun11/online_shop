from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from store.models import ( 
    ProductCategory, 
    ProductSubCategory,
    ProductIndex,
    Mobile,
    Laptop,
    Book)


class ProductCategoryAdmin(ModelAdmin):
    model = ProductCategory
    menu_icon = "pilcrow"
    menu_label = "Product Category"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    # list_display = ("title")
    # list_filter = ('title')
    # search_fields = ('title')
    
    
class ProductSubCategoryAdmin(ModelAdmin):
    model = ProductSubCategory
    menu_icon = "pilcrow"
    menu_label = "Product Sub-Category"
    menu_order = 100    # 100 refers to first menu order and so on 
    list_per_page = 10
    # list_display = ("title")
    # list_filter = ('title')
    # search_fields = ('title')


class ProductIndexModelAdmin(ModelAdmin):
    model = ProductIndex
    menu_icon = "list-ol"
    menu_label = "Product Index"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    # list_display = ("title")
    # list_filter = ('title')
    # search_fields = ('title')
    
class MobileModelAdmin(ModelAdmin):
    model = Mobile
    menu_icon = "list-ol"
    menu_label = "Mobile"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    list_display = ("title",'price')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price', 'inStock')
    
class LaptopModelAdmin(ModelAdmin):
    model = Laptop
    menu_icon = "list-ol"
    menu_label = "Laptop"
    menu_order = 100    # 000 refers to first menu order and so on 
    list_per_page = 10
    list_display = ("title",'price')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price', 'inStock')
    
    
class ElectronicsAdminGroup(ModelAdminGroup):
    menu_label = "Electronics"
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (MobileModelAdmin, LaptopModelAdmin)

   
modeladmin_register(ProductCategoryAdmin)
modeladmin_register(ProductSubCategoryAdmin) 
modeladmin_register(ProductIndexModelAdmin)
modeladmin_register(ElectronicsAdminGroup)




    
    



