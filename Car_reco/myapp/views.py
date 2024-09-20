from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from .models import Car

def car_recommendation(request):
    if request.method == 'GET':
        # Example input from questionnaire (in a real scenario, this would come from user input)
        min_price = float(request.GET.get('min_price', 500000))
        max_price = float(request.GET.get('max_price', 3300000))
        min_seating = int(request.GET.get('min_seating', 4))
        min_mileage = float(request.GET.get('min_mileage', 15))
        transmission = request.GET.get('transmission', 'Automatic')  # New input for transmission

        # Query to filter cars based on the user's preferences
        cars = Car.objects.filter(
            price__gte=min_price,
            price__lte=max_price,
            seating_capacity__gte=min_seating,
            mileage__gte=min_mileage,
            transmission__iexact=transmission  # Added transmission filter
        ).order_by('price')

        # Prepare the data to return as JSON
        car_list = [{
            'id': car.id,
            'brand': car.brand,
            'company': car.company,
            'type': car.type,
            'price': car.price,
            'mileage': car.mileage,
            'seating_capacity': car.seating_capacity,
            'image_url': car.image_url,
            'car': car.car,
            'transmission': car.transmission,
            'fuel_type': car.fuel_type
        } for car in cars]

        return JsonResponse(car_list, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)




def questionnaire(request):
    return render(request, 'questionnaire.html')

