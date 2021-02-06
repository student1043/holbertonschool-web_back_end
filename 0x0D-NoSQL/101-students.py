#!/usr/bin/env python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """ Top Students """
    studentlist = list(mongo_collection.find())
    students = []
    for student in studentlist:
        mystudent = {"name": student.get("name"), "_id": student.get("_id"), "averageScore": 0}
        total = 0
        for myscore in student.get("topics"):
            total += myscore.get("score")
        mystudent["averageScore"] = total / len(student.get("topics"))
        students.append(mystudent)
    sorted(students, key = lambda i: i['averageScore'], reverse = True)
    return students
