from django.contrib.gis.geoip2 import GeoIP2

def validate_dni(dni):
    """
    Validates DNI/NIE/NIF
    :param dni:
    :return: B
    """
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
            and tabla[int(dni) % 23] == dig_control
    return False


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def get_form_errors(form):
    return ' '.join([', '.join(errors) for field, errors in form.errors.items()])


def get_user_geo_info_by_ip(request):
    """
    Get location information about the user, using GeoIP2 module
    :param request:
    :return:
    """
    ip_info = request.session.get('ip_info')

    if not ip_info:
        try:
            ip = get_client_ip(request)  # '94.8.123.17'
            g = GeoIP2()
            lat, lng = g.lat_lon(ip)
            address = g.city(ip)
        except Exception:
            lat = None
            lng = None
            address = None

        ip_info = {
            'lat': lat,
            'lng': lng,
            'address': address
        }

        request.session['ip_info'] = ip_info

    return ip_info
