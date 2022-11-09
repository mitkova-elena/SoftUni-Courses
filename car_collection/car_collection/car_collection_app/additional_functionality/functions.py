from car_collection.car_collection_app.models import ProfileModel


def get_profile():
    try:
        profiles = ProfileModel.objects.get()
        return profiles
    except ProfileModel.DoesNotExist as ex:
        return None


def get_full_name():
    profile = get_profile()
    if profile.first_name is not None:
        first_name = profile.first_name
    else:
        first_name = ''
    if profile.last_name is not None:
        last_name = f' {profile.last_name}'
    else:
        last_name = ''

    last_name = f'{first_name}{last_name}'

    return last_name



