import json

from django.forms import model_to_dict
from django.http import QueryDict

from apps.cinema.models import Hall, Site


""" in this module just contain static functions 
    which help us to do some manipulations 
    with Hall and Site objects """


def get_hall_dict(hall: Hall) -> dict:
    hall_dict = model_to_dict(hall)
    hall_dict.update({'sites': get_sites_list(hall)})
    return hall_dict


def get_sites_list(hall_obj: Hall) -> list:
    return [model_to_dict(site)
            for site in Site.objects.filter(hall=hall_obj)]


# updating utils


def parse_update_response(data: dict) -> [list, dict]:
    print(data)
    sites_json_list = (data.get('new_sites') + ',').split('},')[0: -1: 1]
    site_list = [json.loads(site + '}') for site in sites_json_list]
    hall_dict = {
        'is_vip': json.loads(data.get('is_vip')),
        'number': json.loads(data.get('number')),
    }
    print(site_list, len(site_list))
    return site_list, hall_dict


def update_sites(hall_obj: Hall, sites_list: list):
    Site.objects.filter(hall=hall_obj).delete()
    # print(sites_list)
    for site_dict in sites_list:
        del site_dict['id']
        Site.objects.create(**site_dict)


def update_hall(hall: Hall, data: QueryDict):

    new_sites_list, new_hall = parse_update_response(data)
    print(new_sites_list)
    [site.update({'hall': hall}) for site in new_sites_list]
    sites_list = get_sites_list(hall)

    if sites_list != new_sites_list:
        update_sites(hall, new_sites_list)
    if hall.is_vip != new_hall.get('is_vip'):
        hall.is_vip = not hall.is_vip
    if hall.number != new_hall.get('number'):
        hall.number = new_hall.get('number')

    hall.rows_amount = len(new_sites_list)
    hall.sites_amount = len(new_sites_list[0])
    hall.save()


def gen_price_scheme():
    pass











