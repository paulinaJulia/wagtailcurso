from email.mime import image
from django.db import models
from wagtail.core.models import Page

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.models import TranslatableMixin

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from streams import blocks
class MarketPage(Page):

    titulo = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Titulo da Página"
    )

    subtitle = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Subtítulo da Página"
    )

    image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+',
        verbose_name="Imagem"
    )

    content_panels = Page.content_panels + [
        FieldPanel("titulo"),
        FieldPanel("subtitle"),
        ImageChooserPanel("image"),
    ]
    
   
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["frag"] = MarketFragmento
        return context
        
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Página mark"
        verbose_name_plural = "Páginas Mark"

        

class MarketFragmento(TranslatableMixin, models.Model):


    texto = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Titulo" 
    )

    email = models.CharField(
        max_length=255,
        null=True,
        blank=True, 
        verbose_name="E-mail"
    )

    icon = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+',
        verbose_name="Icone"
    )

    content = StreamField(
            [
                ("title_and_text", blocks.TitleAndTextBlock()),
                ("full_richtext", blocks.RichtextBlock()),
                ("cards", blocks.CardBlock()),
                ("button", blocks.ButtonBlock()), 
                
            ],
            null=True,
            blank=True,
        )
    content_panels = Page.content_panels + [
       
                
                FieldPanel("texto"),
                FieldPanel("email"),
                ImageChooserPanel("icon"),
                StreamFieldPanel("content"),  
    ]

    
    def __str__(self):
        return self.texto

    class Meta:  # noqa
        verbose_name = "Proveedor - Market Assets"
        verbose_name_plural = "Proveedores - Market Assets"
        unique_together = ('translation_key', 'locale')
register_snippet(MarketFragmento)
