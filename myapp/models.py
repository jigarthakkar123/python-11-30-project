from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")
	usertype=models.CharField(max_length=100,default="customer")

	def __str__(self):
		return self.fname+" "+self.lname

class Artist_Profile(models.Model):
	category=(
			('Painter','Painter'),
			('Singer','Singer'),
			('Dancer','Dancer'),
			('Comedian','Comedian'),
		)
	artist=models.ForeignKey(User,on_delete=models.CASCADE)
	artist_category=models.CharField(max_length=100,choices=category)
	artist_fees=models.PositiveIntegerField(default=1000)
	artist_desc=models.TextField()
	picture1=models.ImageField(upload_to="artist_pic/",default="default.png")
	picture2=models.ImageField(upload_to="artist_pic/",default="default.png")
	picture3=models.ImageField(upload_to="artist_pic/",default="default.png")

	def __str__(self):
		return self.artist.fname+" - "+self.artist_category

class Book_Artist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	artist=models.ForeignKey(Artist_Profile,on_delete=models.CASCADE)
	date=models.CharField(max_length=100)
	venue=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	event=models.CharField(max_length=100)
	crowd_strength=models.PositiveIntegerField()
	artist_confirmation=models.BooleanField(default=False)
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+" - "+self.artist.artist.fname