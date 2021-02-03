#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ insert school """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
