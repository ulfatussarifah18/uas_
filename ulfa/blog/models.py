from django.db import models

class hoby(models.Model):
    Makanan = models.CharField(max_length=50)
    Minuman = models.CharField(max_length=50)
    warna = models.CharField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.Makanan)
