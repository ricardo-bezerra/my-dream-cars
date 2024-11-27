from django.db import models


class Car(models.Model):

    def upload_image_customer(instance, filename):
        return f"{instance.id_customer}, {filename}"

    car_id = models.AutoField(primary_key=True, editable=False)
    brand = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    category = models.CharField(max_length=35)
    release_year = models.DateField()
    model_year = models.DateField()
    fuel = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    doors = models.IntegerField()
    quilometers = models.DecimalField(max_digits=10, decimal_places=2)
    state =  models.CharField(max_length=15)
    create_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to=upload_image_customer, blank=True, null=True)
