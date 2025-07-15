from django.db import models
from django.utils import timezone


class Pizza(models.Model):
    """A class representing a pizza."""
    name = models.CharField(max_length=200, default="Custom Pizza")
    description = models.TextField(blank=True, default="No description provided.")
    is_vegetarian = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=199.99)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Topping(models.Model): 
    """A class representing a topping for a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Cheese")
    quantity = models.CharField(max_length=50, help_text="e.g., 2 slices, 50g, 1 tbsp", default="50g")
    is_spicy = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        spicy = "🌶" if self.is_spicy else ""
        return f"{self.name} ({self.quantity}) {spicy}"


class Rating(models.Model):
    """A class to store customer ratings for pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="ratings")
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    comment = models.TextField(blank=True, default="No comment.")
    rated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.pizza.name} - {self.stars}⭐"
