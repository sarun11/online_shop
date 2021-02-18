from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel
)

from store.models import ProductCategory, ProductSubCategory

class HomePage(Page):
    intro = RichTextField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    subpage_types = [
        "store.ProductCategory",
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        # sub_categories = self.objects.descendant_of(ProductCategory) 
        sub_categories = ProductSubCategory.objects.all()
        context["sub_categories"] = sub_categories # later on, may be only featured products will be here
        return context
    
    
