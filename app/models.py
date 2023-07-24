from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CityRegister(models.Model):
    city=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image/state')
    
    def __str__(self):
        return self.city

class Product(models.Model):
    city = models.ForeignKey(CityRegister, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images', null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    after_discount=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    long_dec = models.TextField()
    weight = models.CharField(max_length=100)
    product_availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.CharField(max_length=13)
    zipcode=models.CharField(max_length=6)
    state=models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.after_discount
    
class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity * self.product.after_discount



class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100, blank=True ,null=True)
    razorpay_payment_status=models.CharField(max_length=100, blank=True ,null=True)
    razorpay_payment_id=models.CharField(max_length=100, blank=True ,null=True)
    paid=models.BooleanField(default=False)
    def __str__(self):
        payment_status = "Paid" if self.paid else "Not Paid"
        return f"Payment - User: {self.user}, Amount: {self.amount}, Status: {payment_status}"
    

    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE , default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.after_discount
    
