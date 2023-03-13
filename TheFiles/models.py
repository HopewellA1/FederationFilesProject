from django.db import models
from django.contrib.auth.models import User

class Federation(models.Model):
    FedId = models.AutoField(primary_key=True,blank=False,null=False,auto_created=True)
    superID = models.IntegerField(default=0, blank=True, null=True)
    FederationName = models.TextField(max_length=100)
    
  
    OfficialLetterhead = models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    Constitution = models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    last_AGM_Minutes  = models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    Annual_Financial_Statement = models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    SARS_Tax_Clearance = models.CharField(max_length=3, default="Yes")
    Tax_Clearance_Copy =  models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    Child_Protection_Policies = models.CharField(max_length=3, default='Yes')
    Child_Protection_Copy =  models.FileField(upload_to='TheFiles/files',blank=True, null=True)
    
    #id_OfficialLetterhead
    #id_Constitution
    #id_last_AGM_Minutes
    #

