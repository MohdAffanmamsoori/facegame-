from os import name
from django.contrib.auth import forms
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Userearns12
from home.models import Contactus
from home.models import add_bank_details_user 

from django.contrib.auth.forms import UserCreationForm
from home.models import Users
from django.contrib.auth import views as auth_views 



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from home.forms import ContactForm

import stripe

import razorpay


stripe.api_key = 'sk_test_51HOpHBLMQYyNXTCHKvZHx2tfrW8rfHwqxGN6JV7b5b7yUa4oEJGsHyzhqtGTFMoNOciXb0G5dF3yNbSCfpSBRgdy00bHLvNFUN'



# from home.forms import UserDetailsForm
# from . models import UserProfile




# from django.contrib.auth.views import views as auth_views

# Create your views here.

from django.http import HttpResponse, request, response


def index(request):

    # websi = 'Alhamdulillah Allah Huakbar'

    data = { "amount": 200000 ,"currency": "INR", "receipt": "order_rcptid_11" }
    payment_order = client.order.create(data=data)
    payment_order_id=payment_order['id']

    context={
        'amount':'amount','api_key':key_id , 'order_id':payment_order_id


    }

    return render(request, 'index.html',context)

@login_required(login_url='loginuser.html')

def contact(request):
    
 if request.user.is_authenticated:
    user=request.user
    print(user)
    form=ContactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        cont=form.save(commit=False)
        cont.mainuse=user
        cont.save()
        print(cont)
        return redirect('contact.html')
    return render(request, 'contact.html',context={'form':form})




    

    # if request.method == 'POST':
    #     print('Alhamdulillah')
    #     name = request.POST['Name']
    #     email = request.POST['Email']
    #     phone = request.POST['Phone']
    #     problem = request.POST['Problem']
    #     contact = Contactus(Name=name, Email=email, Phone=phone, Problem=problem)
    #     contact=request.user
    #     contact.save()
    #     messages.success(request, 'Profile details updated.')

    # return render(request, 'contact.html')

@csrf_exempt
def signupuser(request):
    if request.user.is_authenticated:
        return redirect('maindashboard')
    else:    


      if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # paypal=request.POST['userpay']

        if User.objects.filter(email=email).exists():
    
            messages.info(request,'Email Already Exists')
            return redirect('/signupuser/')
        else:

         myuser = User.objects.create_user(username,email,password)
         myuser.save()
         messages.success(request, 'Accounts Created Successfully.')
         return redirect('loginuser')
        

    return render(request, 'signupuser.html')


def loginuser(request):
   if request.user.is_authenticated:
        return redirect('maindashboard')
   else:    


    if request.method == 'POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')

        user = authenticate(request, username=username,
                            password=password)

        if user is not None:
            login(request, user)
            # messages.success(request,username +    'has been successfully Logged in')
            return redirect('/maindashboard')

            
        
        
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('loginuser.html')

         
    return render(request, 'loginuser.html')


def logoutuser(request):
    logout(request)
    messages.success(request, "SuccessFully Logged Out")
    return redirect('/')

       
       
@login_required(login_url='loginuser.html')
@csrf_exempt

def maindashboard(request):
    messages.success( request ,'has been Logged in Successfully')       
    return render(request,'maindashboard.html')
@login_required(login_url='loginuser.html')
def userearn(request):
  if request.user.is_authenticated:
    users=request.user  

    uservids=Userearns12.objects.filter(user=users)
    for item in uservids :
        print(item.video)
    
    return render(request ,'earnings.html', {'uservids': uservids})  

@login_required(login_url='loginuser.html')
def add_bank(request):
    if request.user.is_authenticated:
     users=request.user  
    #  add_bank_details=add_bank_details_user.objects.filter(user=users)
    #  add_bank_details=add_bank_details_user.objects.filter(user=users)
     add_bank_details=add_bank_details_user.objects.filter(user=users)
     
     
     if request.method=='POST':
        acc_number=request.POST['AccountNumber']
        acc_name=request.POST['AccountName']
        swift_code=request.POST['swiftcode']
        profile_name=request.POST['profilename']
        profile_url=request.POST['profileurl']
        add_bank_details=add_bank_details_user(acc_number=acc_number,acc_name=acc_name,swift_code=swift_code,profile_name=profile_name,profile_url=profile_url)

        
        
        add_bank_details.user=request.user
        add_bank_details.save()

    
        print('Alhamdulillah')
       
        messages.success(request,'Bank details added successfully')
     return render(request,'bankdetailsuser.html',{'add_bank_details': add_bank_details} )
    # ,{'add_bank_details': add_bank_details})


key_id='rzp_test_iDUw672ZJMnMXj'
key_secret='D6S2f5TTADJ3NNdS6pBzc2sR'


client = razorpay.Client(auth=(key_id, key_secret))
def Subsuser(request):
 

 data = { "amount": 200000 ,"currency": "INR", "receipt": "order_rcptid_11" }
 payment_order = client.order.create(data=data)
 payment_order_id=payment_order['id']

 context={
     'amount':'amount','api_key':key_id , 'order_id':payment_order_id
 

 }

 if request.method=='POST':
     return redirect('subscribe/pay')

 print(context)

#  payment_id = request.POST.get('razorpay_payment_id', '')
#  order_id = request.POST.get('payment_order_id','')
#  signature = request.POST.get('razorpay_signature','')
#  params_dict = { #     'payment_order_id': payment_order_id, 
#     'razorpay_payment_id': payment_id,
#     'razorpay_signature': signature
#     }

#  result = client.utility.verify_payment_signature(params_dict)
 return render(request,'paymentsubsuser.html',context)

   
   




# def article_create(request):
#     if request.method=='POST':
#         form=forms.CreateArticle(request.POST,request.FILES)
#         if form.is_valid():
#            instance= form.save(commit=False)
#            instance.author=request.user
#            instance.save()
#     return render(request,'bankdetailsuser.html')




# def UserDetailsView(request):
#     #f = 0
#     if request.method == 'POST':
#         f = UserDetailsForm(request.POST, instance = request.user)
#         if f.is_valid():
#             f.save()
#     else:
#         f = UserDetailsForm(request.POST , instance = request.user)

#     print( "UserDetails objects: "), (UserProfile.objects.all()) 

#     return render(request,'forms.html', 
#                               { 'form': f}, 
#                               context_instance=RequestContext(request))    


        