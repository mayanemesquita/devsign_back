from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    class LanguageEnum(models.TextChoices):
        PORTUGESE = "pt-br", _("Português")
        ENGLISH = "en-us", _("Inglês")
        SPANISH = "es-es", _("Espanhol")

    company_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    timezone = models.CharField(max_length=50, default="-03:00")
    language = models.CharField(max_length=5, choices=LanguageEnum.choices, default=LanguageEnum.PORTUGESE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    guest_user = models.ManyToManyField('User', blank=True, related_name="guest_user")
    associated_document = models.ManyToManyField('Document', blank=True, related_name="associated_document")

    def __str__(self):
        return '__all__'

    class Meta:
        db_table = 'company'
        ordering = ['name']
