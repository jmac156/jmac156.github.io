## Peter Cler - Portfolio 

Hi, My name is Peter Cler and I am recent Computer Science Graduate of Southern New Hampshire University. In my time In school, I learned a great many things that improved my understanding of technology and the world. In this Portfolio, I am showing a few of the improvements that have made to my Skills as a Software Developer. I hope that you enjoy your time here. 

My Regards,
Peter

### Informal Code Review. 

This is a simple display of some of the technology that was in the pieces of my project before. It is styled as a Video Code Review.

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=YZ__MTsMdoc&feature=youtu.be" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

[Link to video on youtube](https://youtu.be/YZ__MTsMdoc)

### HTML/CSS/Javascript Front End

The First piece of the project is a web interface for entering Reviews. There is a simple page to enter a review in a Form. 

You can see the Site at http://www.geocities.ws/petercler/index.html.

You can read the report on this part of the project at this [link](https://tinyurl.com/ya26qbmu).

### Restful API

The Second Piece of the Project is a restful web API that allows for calls to a database through the internet.

'''
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
'''

You can read the enhancement report at this [link](https://tinyurl.com/y82qhqfd)

## MongoDB Database

The Third Peice of the Project centers on the MongoDB database that actually stores the reviews data. 

You can read the enhancement report [here](https://tinyurl.com/y765kogt)

## Self Assessment

Lastly, I have made an introspective review of my time in school in this [Self-Assessment](https://tinyurl.com/yaxkqpce)
