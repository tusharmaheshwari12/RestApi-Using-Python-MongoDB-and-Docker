#Packages Importing 
from flask import Flask, request, json, Response
from pymongo import MongoClient, collection
import json
import logging as log


#Flask Intialization
app = Flask(__name__)       


#Import collection
def collectionbuild(): 
    #c = MongoClient("mongodb://localhost:27017/")        #for server is hosted locally
    c = MongoClient('mongodb://mongo:27017/')             #for docker-compose
    db = c["ProductDB"]                               
    coll = db["PDB"]                                  

    #Data import from json file
    with open('Greendeck SE Assignment Task 1.json') as f:
        d = json.load(f)
    coll.insert_many(d)



class RestApi:

    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        #self.c = MongoClient("mongodb://localhost:27017/")         #for server is hosted locally
        self.c = MongoClient('mongodb://mongo:27017/')              #for docker-compose

        #info of database and collection from user 
        database = data['database']                         
        collection = data['collection']
        cursor = self.c[database]
        self.collection = cursor[collection]
        self.data = data
    
    #fetch method : getting data from collection
    def fetch(self):
        log.info('Fetching All Data')
        if 'Filter' in str(self.data):                        
            filter = self.data['Filter']                      
            doc = self.collection.find(filter)                
        else:
            doc = self.collection.find()                    
        if 'count' in str(self.data):                       
            o=doc.count()
        else:
            o = [{item: data[item] for item in data if item != '_id'} for data in doc]
        return o

    
    #insert method : put data in collection
    def insert(self, data):
        log.info('Data Insertion')
        new_doc = data['Document']                        
        response = self.collection.insert_one(new_doc)    
        o = {'Status': ' Inserted Successfully',
                  'Document_ID': str(response.inserted_id)}
        return o

    #put method: updates data from collection 
    def put(self):
        log.info('Data Updation')
        filter = self.data['Filter']                                     
        ud = {"$set": self.data['DataToBeUpdated']}           
        response = self.collection.update_many(filter, ud)   
        o = {'Status': 'Updated Successfully' 
        if response.modified_count > 0 
        else "No Changes"}
        return o

    
    #remove method: delete data from collection
    def remove(self, data):
        log.info('Data Deletion')                                       
        filter = data['Filter']                                          
        response = self.collection.delete_many(filter)
        o = {'Status': 'Deleted Successfully'
        if response.deleted_count > 0 
        else "Not found"}
        return o

    #discountedP method: Show number of products which are on discounted price
    def discountedP(self):
        log.info('Calculating number of products which are on discounted price')
        doc = self.collection.find({'$expr':{'$gt':['$regular_price_value','$offer_price_value']}}).count()      
        return doc


    #uniqueBrands method: show unique brands
    def uniqueBrands(self):
        log.info('Collecting unique brands')
        filter = self.data['Distinct']                                    
        doc = self.collection.distinct(filter)                      
        return doc

    
    #highofferprice method: show number of products which are in high offer price (greater than 300)
    def highofferprice(self):
        log.info('Discovering products whose offer price greater than 300')
        doc = self.collection.find({'offer_price_value' : {'$gt' : 300 }}).count()                              
        return doc

    
    #highdiscount method: shows number of products which are in high discount (greater than 30%)
    def highdiscount(self):
        log.info('Discovering products whose discount greater than 30%')
        doc = self.collection.find({'$expr':{'$gt':[{'$subtract':['$regular_price_value','$offer_price_value']},{'$multiply':[0.3,'$regular_price_value']}]}}).count()
        return doc

    def drop(self):
        self.collection.drop()                                                 #Dropping the Collection
        o = "Status:  Successfully Dropped"
        return o
    
    def insertdata(self):
        with open('Greendeck SE Assignment Task 1.json') as f:                 #Importing data in collection
            fd = json.load(f)
        self.collection.insert_many(fd)    
        o = 'Status: Imported Successfully'
        return o

#Endpoints

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "Yep"}),                     
                    status=200,
                    mimetype='application/json')

#Endpoint for fetch method
@app.route('/mongodb', methods=['GET'])                                 
def mongo_fetch():
    data = request.json                                                                             
    if data is None or data == {}:                                                                   
        return Response(response=json.dumps({"Error": "Query is invalid"}),                         
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                          
    response = o1.fetch()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for insert method
@app.route('/mongodb', methods=['POST'])
def mongo_insert():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Query is invalid"}),
                        status=400,
                        mimetype='application/json')
    o1 = RestApi(data)
    response = o1.insert(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for put method
@app.route('/mongodb', methods=['PUT'])
def mongo_put():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Query is invalid"}),
                        status=400,
                        mimetype='application/json')
    o1 = RestApi(data)
    response = o1.put()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for remove method
@app.route('/mongodb', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Query is invalid"}),
                        status=400,
                        mimetype='application/json')
    o1 = RestApi(data)
    response = o1.remove(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


#Endpoint for discountedP method
@app.route('/mongodb', methods=['COPY'])
def mongo_discount():
    data = request.json                                                         
    if data is None or data == {}:                                              
        return Response(response=json.dumps({"Error": "Query is invalid"}),     
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                           
    response = o1.discountedP()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for uniqueBrand method
@app.route('/mongodb', methods=['PATCH'])
def mongo_distinct():
    data = request.json
    if data is None or data == {} or 'Distinct' not in data:
        return Response(response=json.dumps({"Error": "Query is invalid"}),
                        status=400,
                        mimetype='application/json')
    o1 = RestApi(data)
    response = o1.uniqueBrands()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


#Endpoint for highofferprice method
@app.route('/mongodb', methods=['VIEW'])
def mongo_highoffer():
    data = request.json                                                                              
    if data is None or data == {}:                                                                   
        return Response(response=json.dumps({"Error": "Query is invalid"}),     
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                           
    response = o1.highofferprice()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for highdiscount method
@app.route('/mongodb', methods=['LOCK'])
def mongo_highdiscount():
    data = request.json                                                                             
    if data is None or data == {}:                                                                  
        return Response(response=json.dumps({"Error": "Query is invalid"}),      
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                           
    response = o1.highdiscount()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for drop method
@app.route('/mongodb', methods=['UNLINK'])                                 
def mongo_drop():
    data = request.json                                                                             
    if data is None or data == {}:                                               
        return Response(response=json.dumps({"Error": "Query is invalid"}),     
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                            
    response = o1.drop()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#Endpoint for insertdata method
@app.route('/mongodb', methods=['LINK'])                                 
def mongo_insertdata():
    data = request.json                                                         
    if data is None or data == {}:                                              
        return Response(response=json.dumps({"Error": "Query is invalid"}),     
                        status=400,                                                                  
                        mimetype='application/json')
    o1 = RestApi(data)                                                                            
    response = o1.insertdata()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
    collectionbuild()                                
    app.run(debug=True, port=5000, host='0.0.0.0')  #Taking port and host
