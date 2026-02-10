from django.db import models



class Home(models.Model):
    title = models.CharField(max_length=100)
    city = models.ForeignKey("City", on_delete=models.CASCADE,related_name="city")

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title



class City(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name




class ImageHome(models.Model):
    image = models.ImageField(upload_to='images/')
    home = models.ForeignKey("Home", on_delete=models.CASCADE,related_name="home")

    def __str__(self):
        return self.home.title

    def __repr__(self):
        return self.home.title
