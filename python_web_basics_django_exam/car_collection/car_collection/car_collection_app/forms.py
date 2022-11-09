from django import forms

from car_collection.car_collection_app.models import ProfileModel, CarModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'email', 'age', 'password']
        # exclude = ['first_name', 'last_name', 'profile_picture']

    password = forms.CharField(
        widget=forms.PasswordInput,
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CreateCarForm(CarBaseForm):
    pass


class EditCarForm(CarBaseForm):
    pass


class DeleteCarForm(CarBaseForm):
    pass
