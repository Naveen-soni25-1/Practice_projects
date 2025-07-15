from django.contrib import admin
from .models import Pizza, Topping, Rating

class ToppingsInline(admin.TabularInline):
    model = Topping
    extra = 1

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_vegetarian', 'created_at')
    search_fields = ['name']
    list_filter = ['is_vegetarian']
    inlines = [ToppingsInline]

@admin.register(Topping)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pizza', 'quantity', 'is_spicy', 'date_added')
    list_filter = ['is_spicy']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'stars', 'comment', 'rated_at')