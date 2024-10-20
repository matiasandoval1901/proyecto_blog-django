from django.urls import path
import apps.contacto.views as view

app_name = 'apps.contacto'

urlpatterns = [
    path('contacto/', view.ContactoUsario.as_view(), name='contacto'),
]
