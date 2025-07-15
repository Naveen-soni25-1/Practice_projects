from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Pizza,Topping, Rating
from .forms import PizzaForm, ToppingForm

def index(request):
    """Home page for pizzeria_project"""
    return render(request, 'pizzas/index.html')

@login_required
def menu(request):
    """Show available pizzas"""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/menu.html', context)

@login_required
def pizza(request, pizza_id):
    """show specific pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    entries =  pizza.topping_set.all()
    rating = Rating(pizza)
    context = {'pizza':pizza, 'toppings':entries, 'rating':rating}
    return render(request, 'pizzas/description.html', context)

@login_required
def add_pizza(request):
    """Add Pizza to Menu"""
    if request.method != "POST":
        # display a blank form
        form = PizzaForm()
    else:
        # post data submitted
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:menu')
        
    context = {'form': form}
    return render(request, 'pizzas/add_pizza.html', context)

@login_required
def edit_pizza(request, pizza_id):
    """Edit Pizza in Menu"""
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if not request.user.is_superuser:
        return redirect('pizzas:menu')

    if request.method != "POST":
        # Show the form with existing data
        form = PizzaForm(instance=pizza)
    else:
        # Handle form submission
        form = PizzaForm(instance=pizza, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:menu')

    context = {'form': form}
    return render(request, 'pizzas/edit_pizza.html', context)


@login_required
def add_topping(request, pizza_id):
    """Add topping to Menu"""
    pizza = Pizza.objects.get(id=pizza_id)

    if not request.user.is_superuser:
        return redirect('pizzas:menu')
    
    if request.method != "POST":
        # display a blank form
        form = ToppingForm()
    else:
        # post data submitted
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)
        
    context = {'form': form, 'pizza':pizza}
    return render(request, 'pizzas/add_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    """Edit a topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza_id = topping.pizza.id 

    if not request.user.is_superuser:
        return redirect('pizzas:menu')
    
    if request.method != "POST":
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form': form, 'topping': topping}
    return render(request, 'pizzas/edit_topping.html', context)

@login_required
def delete_pizza(request, pizza_id):
    """Delete an Pizza"""
    pizza = Pizza.objects.get(id=pizza_id)

    if not request.user.is_superuser:
        return redirect('pizzas:menu')
    
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizzas:menu')

@login_required    
def delete_topping(request, topping_id):
    topping = get_object_or_404(Topping, id=topping_id)
    pizza_id = topping.pizza.id

    if not request.user.is_superuser:
        return redirect('pizzas:menu')
    
    if request.method == 'POST':
        topping.delete()
        return redirect('pizzas:pizza', pizza_id=pizza_id)
    return redirect('pizzas:pizza', pizza_id=pizza_id)
