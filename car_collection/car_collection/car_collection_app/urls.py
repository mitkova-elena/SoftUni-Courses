from django.urls import path, include

from car_collection.car_collection_app.views import index, catalogue, car_create, car_details, car_edit, car_delete, \
    profile_details, profile_edit, profile_delete, profile_create

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit/', car_edit, name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
       ])),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
        path('create/', profile_create, name='profile create'),
    ]))
)
