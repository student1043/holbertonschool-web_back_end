#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    connection = client.logs.nginx
    totalips = {}
    iters = 0
    storedips = list(connection.find())
    numofcollections = len(list(connection.find()))
    print(numofcollections, "logs")
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in method:
        print("\tmethod", i + ":", len(list(connection.find({"method": i}))))

    print(len(list(connection.find({"method": "GET", "path": "/status"}))),
          "status check")

    print("IPs:")
    for myips in storedips:
        if myips.get("ip") in totalips:
            totalips[myips.get("ip")] += 1
        else:
            totalips[myips.get("ip")] = 1
    while iters < 10:
        maximum = max(totalips, key=totalips.get)
        print("\t" + maximum + ":", totalips[maximum])
        del totalips[maximum]
        iters += 1
