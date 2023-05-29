from uuid import uuid4

from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    verified_email = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=False)
    password_reset_at = models.DateTimeField(null=True)
    original_company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    company_associated = models.ManyToManyField('Company', blank=True, related_name='user_company')
    associated_document = models.ManyToManyField('Document', blank=True, related_name="user_document")
    created_at = models.DateField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '__all__'

    class Meta:
        db_table = 'user'
        ordering = ['-update_at']
