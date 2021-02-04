#!/usr/bin/env python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """ Top Students """
    mongo_collection.find().sort("averageScore",pymongo.ASCENDING)
