from django.db import models
from mine.models import Mine


# Create your models here.
class ProductBaseModel(models.Model):
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    kode_sine_kar = models.CharField(max_length=125)
    stone_name = models.CharField(max_length=125)
    # stone_type = models.CharField(max_length=125)
    # height = models.PositiveIntegerField()
    # width = models.PositiveIntegerField()
    # length = models.PositiveIntegerField()
    # level=models.CharField(max_length=125)
    created=models.DateField()
    added=models.DateField(auto_now_add=True)
    uniqu_id = models.CharField(max_length=255, blank=True, null=True)
    # shomareh_serail_qoleh= models.CharField(max_length=255)


class Internal_Product(models.Model):
    shomareh_serial_ghole=models.CharField(max_length=125)
    uniqu_id = models.CharField(max_length=255, blank=True, null=True)
    kode_darajebandi=models.CharField(max_length=125)
    line = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        kode_sine_kar = self.kode_sine_kar
        kode_darage_bandi = self.kode_darage_bandi
        shomareh_ghole = self.shomareh_serail_qoleh_dr_madan
        year = str(self.created)[3]
        month = str(self.created)[5:7]
        day = str(self.created)[8::]
        mine = self.mine
        self.uniqu_id = kode_sine_kar + kode_darage_bandi + '-' + shomareh_ghole + year + month + day + '-' + mine
        super(Internal_Product, self).save(*args, **kwargs)


class Exportal_Product(models.Model):
    class Exportal(models.Model):
        Approximate_weight = models.IntegerField()
        baskol_weight=models.IntegerField()
        kode_peleh = models.CharField(max_length=255)
        shomareh_serail_qoleh_dr_madan = models.CharField(max_length=255)
        kode_darz = models.CharField(max_length=255)
        kode_ghavareh = models.CharField(max_length=255)
        kode_rang = models.CharField(max_length=255)
        vazne_baskol = models.PositiveIntegerField()
        buyer = models.CharField(max_length=255)
        uniqu_id = models.CharField(max_length=255, blank=True, null=True)

        def save(self, *args, **kwargs):
            color = self.kode_rang
            year = str(self.created)
            month = str(self.created)
            goleh = self.shomareh_serail_qoleh_dr_madan
            darz = self.kode_darz
            ghavareh = self.kode_ghavareh
            self.uniqu_id = color + '-' + year[3] + month[5] + month[6] + goleh + '-' + darz + ghavareh
            super(Exportal_Product, self).save(*args, **kwargs)
