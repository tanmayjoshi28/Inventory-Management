from django.db import models


class inventory(models.Model):
    inv_class = models.CharField(max_length=50)
    total = models.IntegerField(default=0)

    def __str__(self):
        return ' class = {}'.format(self.inv_class)


class Item(models.Model):
    item = models.ForeignKey(inventory, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    total_no = models.IntegerField()
    choices = (('Available', 'Available'),
              ('Need Restocking', 'Need Restocking'),
              ('SOLD', 'SOLD'))

    status = models.CharField(max_length=50, choices=choices, default='Available')

    def __str__(self):
        return '[ name - {}]    [ price - {}]   [ status - {}]'.format(self.item_name, self.item_price, self.status)

