from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
)

from wagtail.images.edit_handlers import (
    ImageChooserPanel
)
from cart.forms import CartAddProductForm

# Create your models here.

class StoreIndexPage(Page):
    intro = RichTextField(
        null=True, 
        blank=True,
        help_text="Enter page title here")
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    subpage_types = [
        "store.CategoryIndexPage",
        "store.ProductIndexPage",
    ]
    
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context["products"] = Product.objects.all()  # later on, may be only featured products will be here
        return context
    
      
class CategoryIndexPage(Page):
    
    max_count = 1
    
    subpage_types = [
        "store.ProductCategory",
    ]


class ProductCategory(Page):
    
    name = models.CharField(max_length=250)
    
    description = RichTextField(
        null=True,
        blank=True,
        help_text="Description of the Category"
    )
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
    
    active = models.BooleanField(default=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
        FieldPanel('active')
    ]
      
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

class ProductIndexPage(Page):
    
    max_count = 1
    
    subpage_types = [
        "store.Product",
    ]
    

class Product(Page):
    
    sku = models.IntegerField(null=True)
    name = models.CharField(max_length=250)
    
    category = models.ForeignKey(
        "store.ProductCategory", 
        on_delete=models.PROTECT,
        related_name="products")
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
    
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(null=True, max_length=50)
    # mrp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inStock = models.BooleanField(default=True)
    note = RichTextField(
        null=True,
        blank=True,
        help_text='Add notes (if any)'
    )
    
    # TODO available_sizes, available_colors, unit_in_stock, size,
    # TODO discount_available, discount_percentage, ranking,
    
    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('name'),
        FieldPanel('category'),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('brand'),
        # FieldPanel('mrp'),
        FieldPanel('inStock'),
        FieldPanel('note')
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context["cart_add_product_form"] = CartAddProductForm  # later on, may be only featured products will be here
        return context
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



