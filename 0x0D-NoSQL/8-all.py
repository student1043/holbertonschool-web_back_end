#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """ listing all collection items """
    cursor = (list(mongo_collection.find({})))
    for document in cursor.find():
        return document
