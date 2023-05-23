from uuid import uuid4

from django.db import models


class Document(models.Model):
    document_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    deleted = models.BooleanField(default=False)
    deadline = models.DateField(null=False)
    signed = models.BooleanField(default=False)
    created_at = models.DateField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_id, self.name, self.deleted, self.deadline, self.signed, self.created_at, self.update_at

    class Meta:
        db_table = 'document'
