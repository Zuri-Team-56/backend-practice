from django.db import models


class Testimonial(models.Model):
    
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    testimonial = models.TextField(max_length=5000)
    date = models.DateField()

    def __str__(self):
        return "{}".format(self.testimonial)
        