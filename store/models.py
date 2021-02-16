from django.db import models
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

class StoreIndexPage(Page):
    intro = RichTextField(
        null=True, 
        blank=True,
        help_text="Enter page title here")
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    subpage_types = [
        "store.ProductIndexPage",
    ]
    
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context["products"] = Product.objects.all()  # later on, may be only featured products will be here
        return context
    
class ProductIndexPage(Page):
    
    # max_count = 1
    
    parent_page_types = [
        "store.StoreIndexPage"
    ]
    
    subpage_types = [
        "store.Book",    #Change this
    ]
    

class Product(Page):
    
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
        "store.ProductIndexPage",
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

