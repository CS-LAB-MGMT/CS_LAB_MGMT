from django.db import models
# Django models for the entire system. Should likely be moved elsewhere. For now, it is important to note that CASCADE on_delete will
# likely not be a permanent choice here. This is temporary and should not be hard to fix.
class Systems(models.Model):
    #system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural = "Systems"

class Students(models.Model):
    mnumber = models.CharField(max_length=8, primary_key=True)

    class Meta:
        verbose_name_plural = "Students"

class Scripts(models.Model):
    script_id = models.AutoField(primary_key=True)
    system_name = models.ForeignKey('Systems', on_delete=models.CASCADE) # May be okay to CASCADE, we'll see what Bryan wants and how it behaves.
    class ScriptType(models.IntegerChoices):
        ADDUSER = 1
        DELETEUSER = 2
        MODIFYUSER = 3
        RESETPASSWORD = 4
    script_type = models.IntegerField(choices=ScriptType.choices)
    script_string = models.TextField()

    class Meta:
        verbose_name_plural = "Scripts"

class AccountRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    mnumber = models.ForeignKey('Students', on_delete=models.CASCADE)
    system_name = models.ForeignKey('Systems', on_delete=models.CASCADE)
    reason = models.CharField(max_length=150, default='')
    # One way of doing the request type.
    class RequestType(models.IntegerChoices):
        ADDUSER = 1
        DELETEUSER = 2
        MODIFYUSER = 3
        RESETPASSWORD = 4
    request_type = models.IntegerField(choices=RequestType.choices)

    request_datetime = models.DateTimeField(auto_now_add=True)
    class RequestStatus(models.IntegerChoices):
        INCOMPLETE = 1
        HOLD = 2
        NOSCRIPT = 3
        COMPLETE = 4
    request_status = models.IntegerField(choices=RequestStatus.choices)
    class YesNo(models.IntegerChoices):
        NO = 0
        YES = 1
    request_complete = models.IntegerField(choices=YesNo.choices)

    class Meta:
        verbose_name_plural = "Account Requests"
