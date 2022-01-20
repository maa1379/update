from django.db import models



# Create your models here.
class Mine(models.Model):
    name = models.CharField(max_length=255)
    stone_type = models.CharField(max_length=255)
    discovery_license_number = models.CharField(max_length=255)
    operating_license_number = models.CharField(max_length=255)
    minimum_operating_tonnage = models.PositiveBigIntegerField()
    government_law = models.PositiveIntegerField()
    issue_date = models.DateField()
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
