#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """ listing all collection items """
    cursor = mongo_collection
    if cursor:
        for document in cursor.find():
            return document
    return []
