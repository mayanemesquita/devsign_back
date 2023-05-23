from uuid import uuid4
from django.db import models


class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    timezone = models.CharField(max_length=50, default="-03:00")
    language = models.CharField(max_length=2, default="pt")
    created_at = models.DateField(auto_created=True)
    created_by = models.DateField(max_length=36)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_id, self.name, self.timezone, self.language, self.created_at, self.created_by, \
            self.update_at

    class Meta:
        db_table = 'company'
