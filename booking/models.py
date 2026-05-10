from django.db import models

class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    room_number = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.guest_name