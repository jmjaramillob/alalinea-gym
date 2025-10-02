from django.db import models


# Datos del personal
class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    bio = models.TextField()
    photo = models.ImageField(upload_to='media/staff_photos/')

    def __str__(self):
        return self.name


# Planes de pago
class PaymentPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


# Clientes del gimnasio
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='client_photos/')
 
# Registro de pagos de mensualidad
class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.name} - {self.plan.name}'

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
