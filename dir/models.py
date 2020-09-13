from django.db import models


class Tournament (models.Model):
    tournament_name = models.CharField(max_length=250)
    lang = models.CharField(max_length=2, choices=[('bn', 'Bangla'), ('en', 'English')])
    format = models.CharField(max_length=3, choices=[('ap', 'AP'), ('bp', 'BP'), ('3v3', '3v3')])
    date = models.DateField()

    def year(self):
        return self.year

    def __str__(self):
        return self.tournament_name


class Category(models.Model):
    category_text = models.CharField(max_length=50)
    alt_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text


class Motion (models.Model):
    motion_text = models.CharField(max_length=1000)
    info_slide = models.CharField(max_length=9000, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.round + '  -  ' + self.motion_text

