from django.db import models

# Create your models here.
class Topic(models.Model):
    sno=models.IntegerField()
    topic_name=models.CharField(max_length=25, primary_key=True)
    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    player_ID=models.IntegerField(primary_key=True)
    player_name=models.CharField(max_length=30)
    Email=models.EmailField(default='mm1437799@gmail.com')
    def __str__(self):
        return self.player_name

class About(models.Model):
    player_name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    Jersey_No=models.IntegerField(primary_key=True)
    country=models.CharField(max_length=25)
    date=models.DateField(default='2021-11-22')
    def __str__(self):
        return self.country
