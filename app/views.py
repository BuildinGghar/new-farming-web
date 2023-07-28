from . models import *
from django.shortcuts import render, get_object_or_404, redirect 
from django.views import View
from django.contrib import messages
from .forms import *
from django.http import JsonResponse
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.



def home(request, city_name=None):
    cities = CityRegister.objects.all()
    product = Product.objects.all()
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    context = {
        'city': cities,
        'product':product,
        'totalitem':totalitem,
        'wishitem':wishitem
    }
    return render(request, 'app/index.html', context)

def product(request, city_name=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    cities = CityRegister.objects.all()
    product = Product.objects.filter(city__city=city_name) if city_name else Product.objects.all()
    context = {
        'city': cities,
        'product':product,
        'totalitem':totalitem,
        'wishitem':wishitem
    }
    return render(request, 'app/product.html', context)

@login_required
def product_details(request,id, city_name=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    cities = CityRegister.objects.all()
    related_product = Product.objects.filter(city__city=city_name) if city_name else Product.objects.all()
    product=get_object_or_404(Product, id=id)
    wishlist=Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
    products = Product.objects.filter(city__city=city_name) if city_name else Product.objects.all()
    context={
        'city':cities,
        'product':product,
        'related_product':related_product,
        'totalitem':totalitem,
        'wishlist':wishlist,
        'wishitem':wishitem,
        'products':products
    }
    return render(request, 'app/product_details.html', context)

def about(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    cities = CityRegister.objects.all()
    context = {
        'city': cities,
        'totalitem':totalitem,
        'wishitem':wishitem
    }
    return render(request, 'app/about.html', context)

def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    
    cities = CityRegister.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Save the data to the database using the ContactMessage model
            contact_message = ContactMessage(name=name, email=email, phone_number=phone_number, message=message)
            contact_message.save()

            # Add a success message
            messages.success(request, 'Your message was successfully sent We will contact you soon.')

            # Redirect to the same page after successful form submission
            return redirect('/')
    else:
        form = ContactForm()

    context = {
        'city': cities,
        'totalitem': totalitem,
        'wishitem': wishitem,
        'form': form,
    }
    return render(request, 'app/contact.html', context)


class CustomerRegistrationView(View):
    def get(self, request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        form=CustomerRegistrationForm()
        return render(request, 'app/CustomerRegistration.html', locals())
    
    def post(self, request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/CustomerRegistration.html', locals())
    
    
from django.shortcuts import render, redirect
from django.contrib import messages

class ProfileView(View):
    def get(self, request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        if form.is_valid():
            # Create a new Customer instance and populate it with form data
            customer = form.save(commit=False)
            customer.user = request.user  # Set the user for the customer
            
            # Save the customer instance to the database
            customer.save()
            
            messages.success(request, 'Profile updated successfully.')
            return redirect('address')
        
        messages.error(request, 'There was an error in the form submission.')
        return render(request, 'app/profile.html', {'form': form})


def address_view(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    addresses = Customer.objects.filter(user=request.user)
    context={
        'addresses': addresses,
        'totalitem':totalitem,
        'wishitem':wishitem
    }
    return render(request, 'app/address.html', context)


class updateAddress(View):
    def get(self, request, pk):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        addresses = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=addresses)
        context={
            'addresses':addresses,
            'form':form,
            'totalitem':totalitem,
            'wishitem':wishitem
        }
        return render(request, 'app/update_address.html',context)
    def post(self, request, pk):
        customer = Customer.objects.get(pk=pk)  # Fetch the existing customer instance
        form = CustomerProfileForm(request.POST, instance=customer)  # Bind the form to the existing instance
    
        if form.is_valid():
            form.save()  # Save the updated form data to the customer instance

            messages.success(request, 'Updated successfully.')
            return redirect('address')

        messages.error(request, 'There was an error in the form submission.')
        return render(request, 'app/update_address.html', {'form': form})

def delete_address(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    messages.success(request, 'Address deleted successfully.')
    return redirect('address')



def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")

def show_cart(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.total_cost
        amount=amount + value
    totalamount=amount + 40
    return render(request, 'app/addtocart.html', locals())

def show_wishlist(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    user=request.user
    cart=Wishlist.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.total_cost
        amount=amount + value
    totalamount=amount + 40
    return render(request, 'app/wishlist.html', locals())

from django.http import JsonResponse
from django.db.models import Q
from .models import Cart

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()  # Corrected the typo here, it should be c.save() instead of c.save
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.total_cost
            amount += value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
            
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        # Ensure the quantity doesn't go below 1
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.total_cost
            amount += value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.total_cost
            amount += value
        totalamount = amount + 40
        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    
    
def plus_wishlist(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user=request.user
        Wishlist(user=user, product=product).save()
        data={
            'message':"Wishlist Added Successfully",
        }
        return JsonResponse(data)
    
from django.http import JsonResponse

def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        user = request.user
        # Assuming 'Wishlist' is a model representing the user's wishlist
        # Ensure you have the correct import statement for the Wishlist model
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': "Wishlist Remove Successfully",
        }
        return JsonResponse(data)

    
import razorpay 
from django.conf import settings
   
import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views import View

class checkout(View):
    def get(self, request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=0
        if request.user.is_authenticated:
            wishitem=len(Wishlist.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart = Cart.objects.filter(user=user)
        famount = 0
        for p in cart:
            value = p.total_cost
            famount += value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRECT))
        data = {'amount': razoramount, "currency": "INR", "receipt": "order_rcptid_11"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        # {'id': 'order_MGNG4yAXiprRoH', 'entity': 'order', 'amount': 16400, 'amount_paid': 0, 'amount_due': 16400, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1689925656}
        order_id=payment_response['id']
        order_status=payment_response['status']
        if order_status == 'created':
            payment=Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
                
            )
            payment.save()
        return render(request, 'app/checkout.html', locals())


from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils import timezone
from .models import OrderPlacedCOD, Cart, Customer, OrderPlaced

from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from app.models import Cart, OrderPlaced, Customer, OrderPlacedCOD

class CODCheckout(View):
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        totalamount = 0
        for p in cart:
            totalamount += p.total_cost
        totalamount += 40

        add = Customer.objects.filter(user=user)

        return render(request, 'app/checkout.html', {'cart': cart, 'add': add, 'totalamount': totalamount})

    def post(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        totalamount = 0
        for p in cart:
            totalamount += p.total_cost
        totalamount += 40

        add = Customer.objects.filter(user=user)

        # Process the COD order and save it to the database
        if cart.exists():
            cart_item = cart.first()
            product = cart_item.product

            # Get the most recent OrderPlaced instance for the current user
            try:
                your_order_instance = OrderPlaced.objects.filter(user=request.user).latest('order_date')
            except OrderPlaced.DoesNotExist:
                # Handle the case where no OrderPlaced instance is found for the current user
                your_order_instance = None

            if your_order_instance:
                your_product_instance = product
                your_customer_instance = your_order_instance.customer

                # Create the OrderPlacedCOD instance and save it to the database
                order = OrderPlacedCOD(
                    user=user,  # Set the user field to the current user
                    order=your_order_instance,
                    product=your_product_instance,
                    quantity=1,  # Set the quantity as needed
                    customer=your_customer_instance,
                    order_date=timezone.now(),
                    status='Pending',  # You can set the initial status as 'Pending' or any other value
                    total_amount=totalamount,
                )
                order.save()

                # Show a success message to the user
                messages.success(request, 'COD order placed successfully.')

                # After processing the order, delete the cart items for the current user
                cart.delete()

        # Redirect the user back to the checkout page
        return redirect('orderscod')


def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')

    user = request.user

    # Check if the user is authenticated
    if not user.is_authenticated:
        return redirect('login')  # Redirect to the login page for anonymous users

    try:
        customer = Customer.objects.get(id=cust_id)
        payment = Payment.objects.get(razorpay_order_id=order_id)

        # Check if the payment is already marked as paid
        if not payment.paid:
            payment.paid = True
            payment.razorpay_payment_id = payment_id
            payment.save()

            # Assuming you have a Cart model, you can clear the cart after successful payment
            cart = Cart.objects.filter(user=user)
            for c in cart:
                OrderPlaced.objects.create(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment)
                c.delete()

        return redirect("orders")

    except Customer.DoesNotExist:
        # Handle the case when the customer does not exist
        return redirect("error_page")  # Redirect to a custom error page

    except Payment.DoesNotExist:
        # Handle the case when the payment does not exist
        return redirect("error_page")  # Redirect to a custom error page


def orders(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    order_placed=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())



from django.shortcuts import render
from .models import OrderPlacedCOD

def orderscod(request):
    totalitem = len(Cart.objects.filter(user=request.user)) if request.user.is_authenticated else 0
    wishitem = len(Wishlist.objects.filter(user=request.user)) if request.user.is_authenticated else 0

    # Get the associated Customer instance for the current user
    customer = request.user.customer if hasattr(request.user, 'customer') else None
    print("Customer:", customer)  # Debug statement

    # Fetch OrderPlacedCOD instances related to the current customer
    order_placed = OrderPlacedCOD.objects.filter(user=request.user)
    print("Orders:", order_placed)  # Debug statement
    return render(request, 'app/orderscod.html', {'order_placed': order_placed, 'totalitem': totalitem, 'wishitem': wishitem})




# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import Product

def search_results(request):
    cities = CityRegister.objects.all()
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    wishitem=0
    if request.user.is_authenticated:
        wishitem=len(Wishlist.objects.filter(user=request.user))
    search_query = request.GET.get('q')
    if search_query:
        # Filter the queryset based on the search term
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(city__city__icontains=search_query) |
            Q(price__icontains=search_query) |
            Q(after_discount__icontains=search_query) |
           
            Q(long_dec__icontains=search_query) |
            Q(weight__icontains=search_query) 
            
        )
    else:
        products = Product.objects.all()
    
    context = {
        'products': products, 
        'search_query': search_query,
        'totalitem':totalitem,
        'wishitem':wishitem,
        'city': cities,
        
        }
    return render(request, 'app/search_results.html', context)
