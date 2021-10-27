# RestApi-Using-Python-MongoDB-and-Docker

<p align="center">
   <a href="https://restfulapi.net/">
  <img alt="RestApiImage" src="https://turzo.org/wp-content/uploads/2021/04/rest_api_development_python_flask-768x576.jpg" width="900">
  </a>
 
</p>






<center>

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/tutorial/index.html)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/docs)

</center>


This task is all about of two of the most important concepts of software engineering ([API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) and [Containerization](https://www.docker.com/101-tutorial))
---

**The goal of this task is to allow the user to interact with a database of products using APIs which are available on localhost via Docker**

---

# Tech Stack

  - [**Python-3**](https://docs.python.org/3/tutorial/index.html)
  - [**Flask**](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [**PyMongo**](https://docs.mongodb.com/drivers/pymongo/)
  - [**Postman**](https://www.postman.com/)
  - [**Docker**](https://docs.docker.com/)

# Documentation

### *Deploy the project on Docker*
 * Open the cmd or terminal.
 * Docker must be running in the background.
 * Run : __docker-compose build__
 * Run : __docker-compose up__
 * Test the APIs with __http://localhost:5000/mongodb__ by Postman 
---
### *Run by MongoDB on Docker*
 * Open the cmd or terminal.
 * Docker must be running in the background.
 * Run : __docker pull mongo__
 * Run : __docker create -it --name MongoContainer -p 5000:27017 mongo__
 * Run : __docker start MongoContainer__
 * Access MongoDB database and collections MongoDB Campass by   __mongodb://localhost:27017/__
 * Test the APIs with __http://localhost:5000/mongodb__ by Postman
---
### *CRUD Operation on Api Methods*
| Method  | Fuction | Description |
| ------------- | ------------- | ------------- |
| GET  | fetch  | Getting all data from collection, for specific need of data filter keyword is used and for calculating number of records count keyword is used |
| POST  | insert  | Insertion of data in collection, can put one or more depending on the data|
| PUT  | put  | Updates data in collection, uses Filter keyword for previous data and DataToBeUpdated keyword for changed data  |
| Delete  | remove | Deletes data from collection, filter used for remove specific records  |
| COPY  | discountedP | Show number of products which are on discounted price  |
| PATCH  | uniqueBrands | Show unique brands from collection |
| VIEW  | highofferprice | Show number of products which are in high offer price (greater than 300) |
| LOCK  | highdiscount | Show number of products which are in high discount (greater than 30%) |
| UNLINK  | drop | Drops collection  |
| LINK  | insertdata | Insert default collection data in collection  |
----

### *Accessing APIs*
  Follow below steps to access APIs on localhost:
- Open Postman
- Mention __http://localhost:5000/mongodb__ in URL
- Choose any Api method like GET, POST, PUT, DELETE, ETC...
- Go to ****Body**** then ****Raw**** then select ****Json****
- Type Json code according to particular method
- Press on ****Send****
---
### *Using above APIs to fetch, insert, update, remove products and many more...*

**-->  GET Method:** Fetching all data

 ``` 
  {
  "database": "ProductDB",
  "collection": "PDB"
  }
  ```
  Database and Collection of project 	:point_up_2:


  ![GET-Fetch](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Fetch.PNG)
  
  **-->  GET Method + Filter :** Show records, where brand name is equal to outwell
  ```
  {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": 
    {
    "brand_name": "outwell"
    }
  }
  ```
  ![GET-Fetch-Filter](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Fetch-Filter.PNG)
  
  
  **-->  GET Method + Filter + Count :** Show number of records whose brand name is equal to outwell
  ```
   {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": {
    "brand_name": "outwell"
  }
  "count":""
  }
  ```
   ![GET-Fetch-Filter-Count](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Fetch-Filter-Count.PNG)
  
**-->  POST Method:** Insertion of data

  ```
  {
  "database": "ProductDB",
  "collection": "PDB",
  "Document": {
    "name": "Alexa", 
    "brand_name": "Amazon", 
    "regular_price_value": 4999.0, 
    "offer_price_value": 1999.0, 
    "currency": "INR", 
    "classification_l1": "Teen & youngsters", 
    "classification_l2": "Electronic & Tech", 
    "classification_l3": "", 
    "classification_l4": "", 
    "image_url": "https://images.unsplash.com/photo-1543512214-318c7553f230?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80"
  }
  }
  ```
   ![POST-Insert](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/POST-Insert.PNG)
  
**-->  PUT Method:**  Updates already exist data, uses Filter keyword for previous data and DataToBeUpdated keyword for changed data
 
 ```
 {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": {
    "brand_name": "Amazon"
  },
  "DataToBeUpdated": {
    "name": "Alexa", 
    "brand_name": "Google", 
    "regular_price_value": 6999, 
    "offer_price_value": 4999,
    "currency": "INR", 
    "classification_l1": "youngsters", 
    "classification_l2": "Tech", 
    "classification_l3": "", 
    "classification_l4": "", 
    "image_url": "https://images.unsplash.com/photo-1543512214-318c7553f230?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80"
  }
  }
  ```
  ![PUT-put](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/PUT-put.PNG)
  
**-->  DELETE Method:**  Deletion of data, filter used for remove specific records

  ```
   {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": {
    "name": "Alexa"
  }
  }
  ```
  ![DELETE-remove](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/DELETE-remove.PNG)


 **-->  COPY Method:** Show number of products which are on discounted price


  ```
   {
  "database": "ProductDB",
  "collection": "PDB",
  }
  ```
 ![COPY-Count-Discounted-Products](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/COPY-Count-Discounted-Products.PNG)
  
  This solution to this task could be achieved by **GET Method** too 
  ```
  {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": {
    "$expr":{"$gt":["$regular_price_value", "$offer_price_value"]}
  },
  "count":""
  }
  ```
   ![GET-Count-Discounted-Products](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Count-Discounted-Products.PNG)

  
**-->  PATCH Method:** Show unique brands from collection , distinct   keyword takes a field as input and returns the unique records in that field.
 

   ```
   {
  "database": "ProductDB",
  "collection": "PDB",
  "Distinct": "brand_name"
  }
  ```
  ![PATCH-Distinct](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/PATCH-Distinct.PNG)
 

  
**-->  VIEW Method:**   Show number of products which are in high offer price (greater than 300) 

  ```
   {
  "database": "ProductDB",
  "collection": "PDB"
  }
  ```
  ![VIEW-Count-High-Offer-Price](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/VIEW-Count-High-Offer-Price.PNG)
  
 This solution to this task could be achieved by **GET Method** too
  ```
  {
  "database": "ProductDB",
  "collection": "PDB",
  "Filter": {
    'offer_price_value' : {'$gt' : 300 }}
  },
  "count":""
  }
  ```
 ![GET-Count-High-Offer-Price](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Count-High-Offer-Price.PNG)

**-->  LOCK Method:** Show number of products which are in high discount (greater than 30%)

  ```
   {
  "database": "ProductDB",
  "collection": "PDB"
  }
  ```
   ![LOCK-Count-High-Discount](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/LOCK-Count-High-Discount.PNG)

  This solution to this task could be achieved by **GET Method** too
  ```
  {
"database": "ProductDB",
  "collection": "PDB",
"Filter": {
  "$expr":{"$gt":[{"$subtract":["$regular_price_value","$offer_price_value"]},{"$multiply":[0.3,"$regular_price_value"]}]}
},
"count":""
}
  ```
 ![GET-Count-High-Discount](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/GET-Count-High-Discount.PNG)

**-->  UNLINK Method:**  Drop collection
   
   ```
   {
  "database": "ProductDB",
  "collection": "PDB"
  }
  ```
 ![Drop_UNLINK](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/UNLINK-Drop.PNG)

**-->  LINK Method:** Insert data in collection.

   ```
   {
  "database": "ProductDB",
  "collection": "PDB"
  }
  ```
 ![Import_LINK](https://github.com/tusharmaheshwari12/RestApi-Using-Python-MongoDB-and-Docker/blob/main/Assignment-Tushar/Screenshots/LINK-Import.PNG)
