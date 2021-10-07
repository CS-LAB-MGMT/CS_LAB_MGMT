from django.db import models

class AccountRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    mnumber = models.CharField(max_length=8)
    system_id = models.ForeignKey('Systems', on_delete=models.CASCADE)
    # One way of doing the request type.
    class RequestType(models.IntegerChoices):
        ADDUSER = 1
        DELETEUSER = 2
        MODIFYUSER = 3
    request_type = models.IntegerField(choices=RequestType.choices)

    request_datetime = models.DateTimeField()
