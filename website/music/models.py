from django.db import models

# Create your models here.
#has primarykey
class Album(models.Model):
	artist=models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	genre=models.CharField(max_length=100)
	album_logo=models.CharField(max_length=1000)
	
	#make method such that when data base is seen , it show show complete details. no generic one say object(1) etc.
	
	def __str__(self):
	 return self.album_title+'-'+self.artist

class Song(models.Model):
	album=models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=1000)
	
