from uuid import uuid4
from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    verified_email = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=False)
    deadline = models.DateField(null=False)
    signed = models.BooleanField(default=False)
    created_at = models.DateField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id, self.name, self.email, self.verified_email, self.password, self.deadline, \
            self.signed, self.created_at, self.update_at

    class Meta:
        db_table = 'user'
