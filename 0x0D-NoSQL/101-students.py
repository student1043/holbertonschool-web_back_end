#!/usr/bin/env python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """ Top Students """
    studentlist = list(mongo_collection.find())
    students = []
    for i in studentlist:
        print(i)
