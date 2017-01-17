__author__ = 'nishank'

from .models import News
import json


def create_entry(*args, **kwargs):
    """
    Create news
    """
    return News.objects.create(**kwargs)


def create_entry_bulk(raw_json):
    """
    Create news in bulk
    """
    objects = []
    for json_obj in raw_json:
        objects.append(News(** json_obj))
    return News.objects.bulk_create(objects)

