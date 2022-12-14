from django.db import models

class habib(models.Model):
    NAMA = models.CharField(max_length=50)
    NPM = models.CharField(max_length=20)

    def __str__(self):
        return "{}. {}".format(self.id,self.NAMA)

class tahu(models.Model):
    judul = models.ForeignKey(habib, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True)


    def __str__(self):
        return "{}".format(self.judul)

