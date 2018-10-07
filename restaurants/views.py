from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    restaurants = [
        {"name":"burgerKing","food":"Checken Royal"},
        {"name":"PizzaHut","food":"Pepperone"},
        {"name":"Macdonalds","food":"Potato"},
        ]

    context = {
        "my_list": restaurants,
            }

    return render(request, 'list.html', context)


def restaurant_detail(request):
    
    context = {
    'my_object': {"name":"burgerKing","food":"Checken Royal"},
    }
    return render(request, 'detail.html', context)
