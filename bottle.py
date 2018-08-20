#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort
import datetime
from pymongo import MongoClient #standard imports including bottle and pymongo

@route('/create', method='POST')
def create_document():
    uname=request.query.get('uname')
	stars=request.query.get('stars')#pull in the data via request
	date=request.query.get('date')
	review=request.query.get('review')
    try:
        connection = MongoClient('localhost', 27017) 
        db = connection['games']
        collection = db['reviews']#define connection to local database that the bottle server is on
        result=collection.insert({"Username": uname, "Stars": stars, "Date": date, "Review": review})
    except (NameError, IOError, TypeError) as e:#error check
        abort(404, 'This happened > {}'.format(e))
    return result

@route('/read', method='GET')
def read_document():
    try:
        connection = MongoClient('localhost', 27017) 
        db = connection['games']
        collection = db['reviews']#define connection and db collection to connect to
        result=collection.find_one()#return random review for a read request
    except (NameError, IOError, TypeError) as e:#error handling
        abort(404, 'This happened > {}'.format(e))

    if not result:
        abort(404, 'Something Went Wrong...')
    return json.loads(json.dumps(result, indent=4, default=json_util.default))# send back a json formated review

 
  
if __name__ == '__main__': #declare instance of request
    run(host='localhost', port=8080)#run the server and point to the proper port.