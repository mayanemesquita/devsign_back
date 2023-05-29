from uuid import uuid4

from django.db import models


class Document(models.Model):
    document_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    deleted = models.BooleanField(default=False)
    deadline = models.DateField(null=False)
    signed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '__all__'

    class Meta:
        db_table = 'document'
        ordering = ['-created_at']
