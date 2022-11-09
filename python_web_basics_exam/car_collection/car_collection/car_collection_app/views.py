from django.shortcuts import render, redirect

from car_collection.car_collection_app.additional_functionality.functions import get_profile, get_full_name
from car_collection.car_collection_app.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm
from car_collection.car_collection_app.models import ProfileModel, CarModel


def index(request):
    profiles = get_profile()
    context = {
        'profiles': profiles,
    }
    return render(request, 'core/index.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(catalogue)
    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'car/car-create.html', context)


def catalogue(request):
    cars = CarModel.objects.get_queryset()
    cars_num = len(cars)
    context = {
        'cars': cars,
        'cars_num': cars_num,
    }
    return render(request, "core/catalogue.html", context)


def car_details(request, pk):
    car = CarModel.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'car/car-delete.html', context)


def profile_details(request):
    profile = get_profile()
    total_price = []
    full_name = get_full_name()

    context = {
        'profile': profile,
        'total_price': total_price,
        'full_name': full_name,
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')
