from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
from .models import Food, FoodType, FoodMaterial, Evaluation, Order, FoodFeature

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_food = Food.objects.all().count()
    #num_of_dumplings_eval = Evaluation.objects.filter(foodID__exact='dumplings').count()
    #num_foodType = FoodType.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        locals()#,'num_foodType':num_foodType},
     )

def evaluation(request):

    userID = request.POST.get('userID', '')
    foodID = request.POST.get('foodID', '')
    content = request.POST.get('content', '')
    if (userID != '' and foodID != '' and content != ''):
        try:
            u = User.objects.get(username=userID)
            f = Food.objects.get(foodName=foodID)

            Evaluation.objects.create(userID=u, foodID=f, grade=content)
            return render_to_response('index.html',locals())
        except:
            pass
    return render_to_response('evaluation_list.html',locals())

def order(request):
    userID = request.POST.get('userID', '')
    foodID = request.POST.get('foodID', '')
    date_time = request.POST.get('orderDate1', '')
    if (userID != '' and foodID != ''):
        try:
            u = User.objects.get(username=userID)
            f = Food.objects.get(foodName=foodID)

            Order.objects.create(foodID=f, orderDate=date_time, userID=u)
            return render_to_response('index.html',locals())
        except:
            pass
    return render_to_response('order_list.html',locals())

def register(request):
    userID = request.POST.get('userID', '')
    password = request.POST.get('password', '')
    if (userID != '' and password != ''):
        User.objects.create_user(username=userID, password=password)
        return render_to_response('index.html',locals())
    return render_to_response('register.html',locals())

def addFood(request):
    foodName = request.POST.get('foodName', '')
    price = request.POST.get('price', '')
    foodType = request.POST.get('FoodType', '')
    foodFeature = request.POST.get('FoodFeature', '')
    if (price != '' and foodName != '' and foodType != '' and foodFeature != ''): 
        try:
            t = FoodType.objects.get(typeName=foodType)
            f = FoodFeature.objects.get(FoodFeat=foodFeature)
            Food.objects.create(foodName=foodName, price=price, typeID=t, featID=f)
            return render_to_response('index.html',locals())
        except:
            pass
    return render_to_response('addFood.html',locals())

from django.views import generic

class FoodListView(generic.ListView):
    model = Food

class FoodTypeListView(generic.ListView):
    model = FoodType
    context_object_name = 'foodType_list'

class AAA(generic.ListView):
    model = Evaluation
    context_object_name = 'AAA'
    template_name = 'catalog/AAA.html'

def FoodDetail(request, pk):

    model = Food
    food  = model.objects.get(id=pk)
    return(render(request,'catalog/food_detail.html', locals()))
    # def FoodDetailView(generic.DetailView):
    # model = Food

class MaterialListView(generic.ListView):
    model = FoodMaterial
    context_object_name = 'material_list'


from django.contrib.auth.mixins import LoginRequiredMixin


# class LoanedFoodsByUserListView(LoginRequiredMixin,generic.ListView):
#     """
#     Generic class-based view listing books on loan to current user. 
#     """
#     model = Order
#     context_object_name = 'material_list'
#     template_name ='catalog/foodinstance_list_user.html'
    
#     # def get_queryset(self):
#     #     return Order.objects.filter(userID=self.request.user)


