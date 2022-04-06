from unicodedata import name
from django.db import models

# Create your models here.
class HighPriority(models.Model):
    Sector = models.CharField(max_length=120,verbose_name='Sector')
    NoOfScheme = models.CharField(max_length=120,verbose_name='No Of Scheme')
    NoOfUnit = models.CharField(max_length=120,verbose_name='No Of Unit')
    NoOfBeneficiary = models.CharField(max_length=120,name='NoOfBeneficiary')
    SanctionAmount = models.CharField(max_length=120,name='SanctionAmount')
    ReleasedAmount = models.CharField(max_length=120,name='ReleaseAmount')
    SpentAmount = models.CharField(max_length=120,verbose_name='SpentAmount')
    YetToStart = models.CharField(max_length=120,verbose_name='Yet To Start')
    Ongoing = models.CharField(max_length=120,verbose_name='On Going')
    Completed = models.CharField(max_length=120,verbose_name='completed')
    Scraped = models.CharField(max_length=120,verbose_name='Scraped')
    Remarks = models.CharField(max_length=120,verbose_name='Remarks')

    def __str__(self):
        return f"{self.Sector}"

class LowPriority(models.Model):
    Sector = models.CharField(max_length=120,verbose_name='sectior')
    NoOfScheme = models.CharField(max_length=120,verbose_name='No Of Scheme')
    NoOfUnit = models.CharField(max_length=120,verbose_name='No Of Unit')
    NoOfBeneficiary = models.CharField(max_length=120,name='NoOfBeneficiary')
    SanctionAmount = models.CharField(max_length=120,name='SanctionAmount')
    ReleasedAmount = models.CharField(max_length=120,name='ReleasedAmount')
    SpentAmount = models.CharField(max_length=120,verbose_name='SpentAmount')
    YetToStart = models.CharField(max_length=120,verbose_name='Yet To Start')
    Ongoing = models.CharField(max_length=120,verbose_name='On Going')
    Completed = models.CharField(max_length=120,verbose_name='completed')
    Scraped = models.CharField(max_length=120,verbose_name='Scraped')
    Remarks = models.CharField(max_length=120,verbose_name='Remarks')

    def __str__(self):
        return f"{self.Sector}"