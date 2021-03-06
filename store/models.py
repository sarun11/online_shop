from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator 
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
)

from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.images.edit_handlers import (
    ImageChooserPanel
)

from modelcluster.fields import (
    ParentalKey,
)

from wagtail.snippets.models import register_snippet
from cart.forms import CartAddProductForm

# Create your models here.

class ProductCategoryIndex(Page):
     
    max_count = 1
    
    subpage_types = [
        "store.ProductCategory"
    ]
    
    
class ProductCategory(Page):
    
    # Example: Electronic Devices
    # Example: Watches and Accessories
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
        
    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
    ]
    
    parent_page_types = [
        "home.HomePage"
    ]
    
    subpage_types = [
        "store.ProductSubCategory"
    ]
       
class ProductSubCategory(Page):
    
    # Example: Mobiles, Laptops
    # Example: Sunglasses, Eyeglasses
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
        
    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
    ]
    
    parent_page_types = [
        "store.ProductCategory"
    ]
    
    subpage_types = [
        "store.ProductIndex"
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)            
        context["brands"] =self.get_children()  # later on, may be only featured products will be here
        return context
    
class ProductIndex(Page):
    
    # Example: Samsung Mobiles, Apple iPhones, Mi/Redmi Phones
    # Example: Gaming Laptops, Macbooks
    # Example: Men's Sunglasses, Women's Sunglasses
    # Example: Men's Eyeglasses, Women's Eyeglasses
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
        
    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
    ]
    
    parent_page_types = [
        "store.ProductSubCategory"
    ]
    
    subpage_types = [
        "store.Book",    # Change this
        "store.Mobile", 
        "store.Laptop", 
    ]
    

class Product(Page):
    
    # Inherit this class to form individual products
    
    sku = models.IntegerField(null=True)
    name = models.CharField(max_length=250)
    
    image = models.ForeignKey(
        "wagtailimages.Image", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+")
    
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(null=True, max_length=50)  # This will be a Snippet (foreign key)
    # mrp = models.DecimalField(max_digits=10, decimal_places=2, de fault=0)
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
    
    subpage_types = []
    

class Mobile(Product):
    
    template = 'store/product.html'
    
    MEMORY_CHOICES = [
        ('2GB', '2GB'),
        ('3GB', '3GB'),
        ('4GB', '4GB'),
        ('6GB', '6GB'),
        ('8GB', '8GB'),
        ('12GB', '12GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'),   
    ]
    
    STORAGE_CHOICES = [
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
        ('128GB', '128GB'), 
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1TB', '1TB'),
    ]
    
    COLOR_CHOICES = [
        ('Grey', 'Grey'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Light Blue', 'Light Blue'),
    ]
    
    color = models.CharField(max_length=25, choices=COLOR_CHOICES, default='Black')
    memory = models.CharField(max_length=5, choices=MEMORY_CHOICES, default='4GB')
    storage = models.CharField(max_length=5, choices=STORAGE_CHOICES, default='32GB')
    
    stock = models.PositiveIntegerField()
    
    content_panels = Product.content_panels + [
        FieldPanel('color'),
        FieldPanel('memory'),
        FieldPanel('storage'),
        FieldPanel('stock'),
        
    ]
    
    parent_page_types = [
        "store.ProductIndex",
    ]
    
    subpage_types = []
    

class Laptop(Product):
    template = 'store/product.html'
    
    MEMORY_CHOICES = [
        ('2GB', '2GB'),
        ('3GB', '3GB'),
        ('4GB', '4GB'),
        ('6GB', '6GB'),
        ('8GB', '8GB'),
        ('12GB', '12GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'), 
        ('64GB', '64GB'),
        ('128GB', '128GB'),
        ('256GB', '256GB'),  
    ]
    
    SSD_STORAGE_CHOICES = [
        ('None', 'None'),
        ('128GB', '128GB'), 
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1TB', '1TB'),
        ('2TB', '2TB'),
        ('4TB', '4TB'),
    ]
    
    COLOR_CHOICES = [
        ('Grey', 'Grey'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Light Blue', 'Light Blue'),
    ]
    
    color = models.CharField(max_length=25, choices=COLOR_CHOICES, default='Black')
    memory = models.CharField(max_length=5, choices=MEMORY_CHOICES, default='4GB')
    hasSSD = models.BooleanField(default=False)
    ssd_storage = models.CharField(max_length=5, choices=SSD_STORAGE_CHOICES, default='None')
    
    stock = models.PositiveIntegerField()
    
    content_panels = Product.content_panels + [
        FieldPanel('color'),
        FieldPanel('memory'),
        FieldPanel('hasSSD'),
        FieldPanel('ssd_storage'),
        FieldPanel('stock'),
        
    ]
    
    parent_page_types = [
        "store.ProductIndex",
    ]
    
    subpage_types = []
    
    
class Book(Product):
    
    template = 'store/product.html'
    
    content_panels = Product.content_panels + [
        InlinePanel(
            "authors",
            heading="Authors",
            help_text="Select one or more authors"
        ),
    ]
    
    parent_page_types = [
        "store.ProductIndex",
    ]
    
    subpage_types = []


class BookAuthor(Orderable, models.Model):
    book = ParentalKey(
        "store.Book",
        null=True,
        on_delete=models.CASCADE,
        related_name="authors",
    )
    
    author = models.ForeignKey(
        "store.Person",
        null=True,
        on_delete=models.SET_NULL,
        related_name="books_authored"
    )
    
    class Meta(Orderable.Meta):
        verbose_name = "author"
        verbose_name_plural = "authors"
    
    panels = [
        SnippetChooserPanel("author")
    ]
    
    
@register_snippet
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name')
    ]
    
    def __str__(self):
        return " ".join([self.first_name, self.last_name])


