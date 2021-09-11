from django.db.models.fields import NullBooleanField
from django.db import models

# Create your models here.
class Album(models.Model):
    Album_title=models.CharField(max_length=100)
    Album_format=models.CharField(max_length=100)
    CopyRight_Date=models.DateField()
    def __str__(self):
        return f"{self.Album_title} ({self.Album_format})"

class Song(models.Model):
    Song_title=models.CharField(max_length=100)
    Song_album=models.ForeignKey(Album,on_delete=models.CASCADE,null=True) 
    Song_Author=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Song_title} "
        if(self.Album_title==NullBooleanField):
            return f"{self.song_title} with no album"
        else:
            return f"{self.song_title} has an album  {self.Song_album.Album_title} "