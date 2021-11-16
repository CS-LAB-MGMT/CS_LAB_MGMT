from django.db import models
# Django models for the entire system. Should likely be moved elsewhere. For now, it is important to note that CASCADE on_delete will
# likely not be a permanent choice here. This is temporary and should not be hard to fix.

#Represents Systems table in database
class Systems(models.Model):
    system_name = models.CharField(max_length=30, primary_key=True)
    group_name = models.CharField(max_length=30,default='')
    class YesNo(models.IntegerChoices):
        NO = 0
        YES = 1
    system_active = models.IntegerField(choices=YesNo.choices, default=1)
    def __str__(self):
       return '%s'  % (self.pk)

    #Affects how systems is displayed on admin page
    class Meta:
        verbose_name_plural = "Systems"


#Represents Students table in database
class Students(models.Model):
    pipeline_id = models.CharField(max_length=6 ,primary_key=True)

    def __str__(self):
       return '%s'  % (self.pk)

    # Affects how students is displayed on admin page
    class Meta:
        verbose_name_plural = "Students"

class RequestType(models.Model):
    request_type = models.CharField(max_length=30 ,primary_key=True)

    def __str__(self):
       return '%s'  % (self.pk)

    

#Represents scripts table in database
class Scripts(models.Model):
    script_id = models.AutoField(primary_key=True)
    system_name = models.ForeignKey('Systems',on_delete=models.CASCADE) # May be okay to CASCADE, we'll see what Bryan wants and how it behaves.
    
    script_type = models.ForeignKey('RequestType',on_delete=models.CASCADE)
    script_string = models.TextField()


    def __str__(self):
        return '%s %s %s' % (self.system_name, self.script_type, self.script_string)

    # Affects how scripts is displayed on admin page
    class Meta:
        verbose_name_plural = "Scripts"
#Represents AccountRequests table in database
class AccountRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    pipeline_id = models.ForeignKey('Students', on_delete=models.CASCADE)
    system_name = models.ForeignKey('Systems', on_delete=models.CASCADE)
    reason = models.CharField(max_length=150, default='')
    # One way of doing the request type.
    # class RequestType(models.IntegerChoices):
    #     ADDUSER = 1
    #     DELETEUSER = 2
    #     MODIFYUSER = 3
    #     RESETPASSWORD = 4
    request_type = models.ForeignKey('RequestType', on_delete=models.CASCADE)

    request_datetime = models.DateTimeField(auto_now_add=True)
    class RequestStatus(models.IntegerChoices):
        INCOMPLETE = 1
        HOLD = 2
        NOSCRIPT = 3
        COMPLETE = 4
    request_status = models.IntegerField(choices=RequestStatus.choices, default=1)
    class YesNo(models.IntegerChoices):
        NO = 0
        YES = 1
    request_complete = models.IntegerField(choices=YesNo.choices, default=0)

    unique_request = models.UniqueConstraint(fields=['pipeline_id','system_name','request_type'],
                                            name='unique_request')
    def __str__(self):
        return '%s %s %s %s'  % (self.system_name, self.reason, self.request_type, self.request_status)

    class Meta:
        verbose_name_plural = "Account Requests"


#Send a message to general


