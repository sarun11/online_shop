from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel
)

class HomePage(Page):
    intro = RichTextField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    
    subpage_types = [
        "store.StoreIndexPage",
    ]
