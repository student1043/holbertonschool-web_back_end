#!/usr/bin/env python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """ Top Students """
    studentlist = list(mongo_collection.find())
    students = []
    total = 0
    for student in studentlist:
        mystudent = {"name": student.get("name"), "_id": student.get("_id"), "averageScore": 0}
        for myscore in student.get("topics"):
            total += myscore.get("score")
        mystudent["averageScore"] = total