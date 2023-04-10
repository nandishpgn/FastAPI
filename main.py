
#==================================================================================================
#==============FastAPI======================================================
#Fastapi is a modern, fast(High performance) ASGI( asynchronous server gateway inteface) framwork
#for bulding restful api's with python

######=====Features =========
#asynchronous way of programming
#very high performance
# FAst to code
#great editor support
# fastapi comes with bult in support for data validation, authentication, documentation 

######## ========concepts we are going to deal in fastapi==========
#creating end points and running it locally
#Handling request parameters
# 1)path parameters
# 2)Query parameters
# 3)The rewuest body
# 4)form data and file uploads
# 5)Headers and request obj

#=======customizing the response====
#Raising HTTP errors
#building custom response
# path opertation parameters
# the response bady 



#structuring bigger projects with multiuple routes

#Communicating with sql database====using sqlalchemy
#Creating table
#making insertion queries
#connecting to database
#making select queries
#making update and delete queries

#=====Adding custom data validation====with pydantic
#Applying validation at field level
#Applying validation at object level
#Applying validation before pydantic parsing

#===Authentication and authorization=====
#===generating tokens========== 


#======Handling request parameters===========

#======Path parameters====
#in fastapi , such a path string is given as a parameter to the operation decorator.

# from fastapi import FastAPI

# app=FastAPI()
# @app.get("/")
# async def index():
#     return{"message":"Hello World"}

# here ("/") is the path, get is the operation#// @app.get("/") is the path operation decorator

# async keword in the defnition tells fastapi that it is to be run asynchronously
#i.e without blocking the current thread of execution 

# from fastapi import FastAPI

# app=FastAPI()
# # @app.get("/")
# # async def index():
# #     return{"Message":"Hello world"}
# @app.get("/hello/{name}")
# async def hello(name):
#     return{"name":name}

# ========route can have multiple paramters============
# from fastapi import FastAPI

# app=FastAPI()
# @app.get("/users/{name}/{age}")
# async def hello(name,age):
#     print(name+age)    ///// by default it will consider string
#     return{"name":name,"age":age}

# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/hello/{name}/{age}")
# async def data(name:str, age:int):
#     return{"name":name, "age":age}


#========Limiting values using enum========
# from fastapi import FastAPI
# from enum import Enum

# app=FastAPI()

# class UserType(str, Enum):#limiting value to class parameters
#     STANDARD="STANDARD"
#     ADMIN="ADMIN"

# @app.get("users/{type}/{id}")
# async def get_user(type:UserType, id:int):
#     return{"type":type, "id":id}    


#======multiple inheritance ========

# from enum import Enum
# from fastapi import FastAPI


# class CarTypeName(str, Enum):
#     tesla = "Tesla"
#     volvo = "Volvo"
#     fiat  = "Fiat"

# class CarPrice(str, Enum):
#     Tesla_price="30 lac"
#     Volvo_price="40 lac"
#     Fiat_price="10 lac"

# app = FastAPI()


# @app.get("/car/{car_type}/{car_price}")
# async def get_car(car_type: CarTypeName, car_price:CarPrice):
#     # CarTypeName.tesla
#     # if car_type == CarTypeName.tesla:
#     #     print("in a Tesla")
#     return {'car_type': car_type, 'car_price':car_price}

#======Advanced Validation==========

# from fastapi import FastAPI, Path
# from enum import Enum

# app= FastAPI()

# @app.get("/users/{id}")
# async def get_user(id:int= Path(..., ge=1)):
#     return{"id":id}


# from fastapi import FastAPI, Path
# from enum import Enum

# app=FastAPI()

# @app.get("/licence-plates/{licence}")
# async def get_licence_plate(licence:str =Path(..., min_length=9, max_length=9)):
#     return {'licence':licence}

#//////////////////doubt======
# from fastapi import FastAPI,Path
# from enum import Enum

# app=FastAPI()

# @app.get("/licence/")
# async def get_licence(licence:str=Path(..., min_length=10, max_length=10)):
#     return{'licence':licence}
# #@app.get("/usn")
# async def get_usn(usn:int=Path(..., ge=0,le=11)):
#     return{"usn":usn}


#========Query parameters=========

#when we declare a function parameter that are not part of the path parameters, they are 
#automatically interpreted as "Query" parameter
#"Query" is the set of key value pairs

# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/users")
# async def get_user(page:int, size:int):
#     return{"page":page, "size":size}


# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/users")
# async def get_user(page:int=1, size:int=10):
#     return{"page":page, "size":size}

# from enum import Enum
# from fastapi import FastAPI

# class UserFormat(str,Enum):
#     SHORT="short"
#     FULL="full"

# app=FastAPI()
# @app.get("/users")
# async def get_user(format:UserFormat):
#     return{"format":format}    


#====Advanced validation for query parms=====

# from fastapi import FastAPI, Query

# app=FastAPI()

# @app.get("/users")
# async def get_user(page:int=Query(1,gt=0),size:int=Query(10,le=100)):
#     return{"page":page, "size":size}


#========The request body=====
#the body is the part of http request that contains raw data, representing documents,forms
#or files 
#in restapi it is usually encoded in json & used to create structured obj in database.

# from fastapi import FastAPI,Body

# app=FastAPI()

# @app.get("/users")
# async def Create_user(name:str=Body(...), age:int=Body(...)):
#     return{"name":name, "age":age}

#=====Pydantic models=======
#Pydantic a is python library for data validation and is based on classes and type hints
 

# from fastapi import FastAPI
# from pydantic import BaseModel

# class User(BaseModel):#
#     name:str
#     age:int

# app=FastAPI()
# @app.post("/users")
# async def create_user(user:User):
#     return user    

#=====Multiple objects=====
#======================================doubt=========// during mul classes we should not use curly braces

# from fastapi import FastAPI
# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# class Company(BaseModel):
#     company_name: str

# app=FastAPI()
# @app.post("/users")
# async def create_user(user:User, company_name:Company):
#     return user, company_name        


#==add singular body values with the body function======


# from fastapi import FastAPI, Body
# from pydantic import BaseModel

# class User(BaseModel):
#     name:str
#     age:int

# app=FastAPI()
# @app.post("/users")
# def create_user(user:User , id:int=Body(..., ge=1, le=10)):
#     return {"user":user, "id":id}



#======Form data & File uploads=======/////////////////=============
#pip install python-multipart
#=======Form Data=======
#Form is a class that inherits directly from body. To declare form bodies you need to use
#Form explicitly
#because without it the parameter would be interpreted as query parameter or body parameter  

# from fastapi import FastAPI, Form

# app=FastAPI()

# @app.post("/users")
# async def create_user(name:str =Form(...), age:int=Form(...)):
#     return name,age


# from fastapi import FastAPI, Form
# app=FastAPI()

# @app.post("/login/")
# async def login(username:str=Form(...), password:str=Form(...)):
#     return{"username":username}

#=====File uploads======
#uploading file is a common requirement for web application wheather that is image or documents
#fastapi provides a parameter fun File that enables this


# from fastapi import FastAPI, File

# app=FastAPI()

# @app.post('/files')
# async def upload_files(file:bytes=File(...)):
#     return{"file_size":len(file)}

#===UploadFile=====(doubt:File function allocates memory in--)
#it has several advantages oveer bytes, it uses a spooled file:(spooling is a system functons
#that saves data in a database file for later processing or printing ) 
#afile stored in memory up to a max size limit it will be stored in disk.


# from fastapi import FastAPI, UploadFile, File

# app= FastAPI()

# @app.post("/files")
# async def Upload_file(file:UploadFile=File(...)):
#     return{"file_name":file.filename, "content_type":file.content_type}

#=====Uploading multiple files===


# from fastapi import FastAPI, File, UploadFile

# app=FastAPI()
# @app.post('/files')
# async def Upload_multiple_Files(files:list[UploadFile]=File(...)):
#     return[
      
#         {"file_name":file.filename, "content_type":file.content_type}
#           for file in files
#     ]



# from fastapi import FastAPI, File, UploadFile

# app=FastAPI()
# @app.post('/files')
# async def Upload_multiple_Files(files:list[UploadFile]=File(...)):
#     return files


#====Headers=========
#beside the url and the body, another major part of HTTP request are the Headers, they contain
#all sort of meta data that can be useful when handling requests.

# from fastapi import FastAPI, Header

# app=FastAPI()

# @app.get("/")
# async def get_headers(hello:str=Header(...)):
#     return{'Hello':hello}


# from fastapi import FastAPI,Header

# app=FastAPI()
# @app.get("/")
# async def get_header(user_agent:str=Header(...)):
#     return{"user_agent":user_agent}

#====The Request Object======
#suppose we need to access a raw request object with all of the data associated with it,
#by using request object

# from fastapi import FastAPI, Request

# app=FastAPI()

# @app.get("/")
# async def get_request(request:Request):
#     return{"path":request.url.path}


#//doubt

# from fastapi import FastAPI,Request, File, UploadFile

# app=FastAPI()
# @app.post("/")
# async def get_request(request:Request, file:UploadFile=File(...)):
#     return{"file":file,
#         "path":request.url.path}



#=====Customizing the response===
#if we want to customize the response a bit further;for instance, by changing status code

# from fastapi import FastAPI, status
# from pydantic import BaseModel

# class Post(BaseModel):
#     title:str

# app=FastAPI()
# @app.get("/post", status_code=status.HTTP_201_CREATED)
# async def create_post(post:Post):
#     return post


#===Dummy database==//// error
# from fastapi import FastAPI, status
# from pydantic import BaseModel

# class Post(BaseModel):
#     title:str
#     nb_views:int

# posts = {
#     1:Post(title="hello", nb_views=100)
#     }

# app=FastAPI()


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(id:int):
#     posts.pop

#=====Response parameters=====
#it is used for custon headers=

# from fastapi import FastAPI, Response

# app=FastAPI()
# @app.get("/")
# async def custom_header(response:Response):
#     response.headers["Custom-Header"]="Custom-Header-Value"
#     return{"Hello":'World'}


# from fastapi import FastAPI, Response, status
# from pydantic import BaseModel

# class Post(BaseModel):
#     title:str
#     nb_views:int

# posts = {
# 1:Post(title="Hello", nb_views=100)
# #3:Post(title="World", nb_views=100)
# }

# app=FastAPI()

# app.put("/posts/{id}")
# async def Update(id:int, post:Post, response:Response):
#     response.status_code=status.HTTP_201_CREATED
#     post[id]=post
#     return posts[id]

# from typing import List, Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []


# @app.post("/items/")
# async def create_item(item: Item)-> Item:
#     return Item


# @app.get("/items/")
# async def read_items()->List[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


#====== Raising HTTP Errors===========
#When calling a rest api, Quite frequently, you might find that things dont go very well;
#we might come across the wrong paramters, invalid payloads,or obj that don't exist anymore
#Errors happen for a lot of reasons,
#thats why it's critical to detect them and raise a clear and unambiguous error msg

# from fastapi import FastAPI, Body, status, HTTPException

# app=FastAPI()

# @app.post("/password")
# async def check_pass(password:str=Body(...), password_confirm:str=Body(...)):
#     if password != password_confirm:
#         raise HTTPException(
#             status.HTTP_400_BAD_REQUEST,
#             detail="password don't match"
#         )
#     return{"message":"password match"}



# from fastapi import FastAPI ,Body, HTTPException,status

# app=FastAPI()
# @app.post("/password")
# async def check_pass(passwod:str=Body(...), password_conf:str=Body(...)):
#     if passwod != password_conf:
#         raise HTTPException(
#             status.HTTP_400_BAD_REQUEST,
#             detail={
#             "msg":"password don't match",
#             "hints":[
#             "check tha caps lock on your keboard",
#             "Try to make the password visible by clicking on the eye icon to check your typing"
#             ],
#             },
#         )
#     return{"msg":"password match"}


#===Building custom response=========
#===types==

#HTML response
#plain text response
#redirect response
#streaming response
#file response

#====HTML response====

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.get("/items/", response_class=HTMLResponse)
# async def read_items():
#     return """
#     <html>
#         <head>
#             <title>html response</title>
#         </head>
#         <body>
#             <h1>HTML resonse!</h1>
#         </body>
#     </html>
#     """

#====Plain text response===
# from fastapi import FastAPI
# from fastapi.responses import PlainTextResponse

# app=FastAPI()
# @app.get("/plain_text_response", response_class=PlainTextResponse)
# async def get_response():
#     return "hello world!"

#====making redirection====

# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse


# app=FastAPI()
# @app.get("/redirect",response_class=RedirectResponse)
# async def redirect():
#     return RedirectResponse("/some_thing")

# @app.get("/some_thing")
# async def redirect():
#     return "nandish"



# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# app = FastAPI()


# @app.get("/fastapi", response_class=RedirectResponse)
# async def redirect_fastapi():
#     return "https://fastapi.tiangolo.com"


#=====Managing models and their field types with pydantic
#defining models and their field types with pydantic
#creating models variation with class inheritace
#adding custom data validation with pydantic
#working with pydantic object


# from pydantic import BaseModel
# from enum import Enum
# from typing import List
# from pydantic import BaseModel, ValidationError
# from datetime import date

# class Gender(str,Enum):
#     MALE="male"
#     FEMALE="female"
#     NON_BINARY="non_binary"
    

# class Person(BaseModel):
#     first_name:str
#     last_name:str
#     gender:Gender
#     birthdate:date    
#     interests:List[str]

# try:

#     Person(
#         first_name="nandish",
#         last_name="P",
#         gender="male",
#         birthdate="1998-10-10",
#         interests=["travel", "sports"]
#     )  

# except ValidationError as e:
#     print(str(e))

# names=[
#     "nandish",
#     "madhu",
#     "rajesh",
#     "devu"
# ]
# #var={len(names) for name in names}
# for name in names:
#     length={name:len(name)}
#     print(length , end=" ")
# #length={name:len(name)for name in names}
# print(length)


#===============================================================================

#======Pydantic validation ===========

                  
# from pydantic import BaseModel, Field

# class Blog(BaseModel):
#     title: str = Field(...,min_length=5)
#     is_active: bool

# value= Blog(title="hicgb ",is_active=True)
# print(value)



# Defining models and field types with pydantic



# from datetime import date
# from enum import Enum
# from typing import List

# from pydantic import BaseModel, ValidationError
# from enum import Enum

# class Gender(str, Enum):
#     Male="male"
#     Female="female"
#     Non_binary="Non_binary"

# class Person(BaseModel):
#     first_name:str
#     last_name:str
#     gender:Gender
#     birthdate:date
#     intersers:List[str]

# try:
#     Person(
#         first_name="Nandish",
#         last_name="P",
#         gender="male",
#         birthdate="1998-11-22",
#         intersers=["safdas","sdfzcv"]
#     )
# except ValidationError as e:
#     print(str(e))    


# from datetime import date
# from enum import Enum
# from typing import List
# from pydantic import BaseModel, ValidationError

# class Gender(str,Enum):
#     male='male'
#     female="female"
#     others="others"

# class Person(BaseModel):
#     fname:str
#     lname:str
#     birthdate:date
#     gender:Gender
#     intersts:list[str]
# # for invalid bith date
# try:
#     Person(
#         fname="nandish",
#         lname="P",
#         gender="male",
#         birthdate="1998-22-11",
#         intersts=["sadfas","sadas"]
#     )        
# except ValidationError as e:
#     print(str(e))    



# from pydantic import BaseModel, ValidationError

# class Address(BaseModel):
#     street:str
#     postal_code:str
#     city:str
#     country:str

# class Person(BaseModel):
#     fname:str
#     lanme:str
#     address:Address

# try:
#     Person(
#         fname="nandish",
#         lanme="P",
#         address={
#         "street":"dsnfvsjdk",
#         "postal_code":"dsfvsdsdf",
#         "city":"sdcassc",
#         "country":"sdfcsdfc"
#         }
#     )        
# except ValidationError as e:
#     print(str(e))



# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int):
#     results = {"item_id": item_id}
#     return results


#=====Optional fields and defaut values====

# from typing import Optional
# from pydantic import BaseModel

# class UserProfile(BaseModel):
#     name:str
#     location:Optional[str]
#     is_available:bool=True

# user=UserProfile(name="namdish")
# print(user)

      
#====Field validation========

# from pydantic import BaseModel, Field, ValidationError
# from typing import Optional

# class Person(BaseModel):
#     fname:str=Field(..., min_length=3)
#     lname:str=Field(..., min_length=2)
#     age:Optional[int]

# data=Person(
#     fname="nandish",
#     lname="pcv",
#     age=24

# )    
# print(data)

#===Vlaidating Email and URls with pydantic types====

##pip install email-validator

# from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

# class Person(BaseModel):
#     emai:EmailStr
#     website:HttpUrl

# try:
#     Person(
#         emai="nandi@gamil.com",
#         website="https://www.w3schools.com/python/python_conditions.asp"
#     )
# except ValidationError as e:
#     print(str(e))    

      
#====Applying validation at field level=====

# from datetime import date
# from pydantic import BaseModel, validator

# class Person(BaseModel):
#     fname:str
#     lname:str
#     dob:date

#     @validator("dob")
#     def valid_dob(cls, v:date):
#         delta=date.today() -v
#         age=delta.days/365

#         if age> 120:
#             raise ValueError("Too Old")
#         return v
    
# data=Person(
#     fname="sdasd",
#     lname="cfxz",
#     dob="2000-01-01"
# )
# print(data)


#====Object level==========


# from pydantic import BaseModel, root_validator

# class CreateUser(BaseModel):
#     email : str
#     password :str 
#     confirm_password :str 

#     @root_validator()
#     def verify_password_match(cls,values):
#         password = values.get("password")
#         confirm_password = values.get("confirm_password")

#         if password==confirm_password:
#             raise ValueError("password match")
        
#         elif  password!= confirm_password:
#             print()
#             raise ValueError("the two password did not match")
       
#         else:
#              return values
        
# user=CreateUser(email="ping@fastapitutorial.com",password="1234",confirm_password="1234")
# print(user)



#=====Converting object to dict=========


# from pydantic import BaseModel
# from datetime import date

# class Person(BaseModel):
#     fname:str
#     lname:str
#     dob:date
#     interests:list[str]
#     address:str
               
# data=Person(
#     fname="nandish",
#     lname="p",
#     dob="1998-11-22",
#     interests=["travelling", "Sports","Swimming"],
#     address="cta"
# )
# print(data)

# person_dict=data.dict()
# print(person_dict)
# print(person_dict["fname"])
# print(person_dict["address"], person_dict["lname"])

# person_include=data.dict(include={"dob"})
# print(person_include)

# person_exclude=data.dict(exclude={"fname", "lname"})
# print(person_exclude)


#====Dependency injection====

# from fastapi import FastAPI, HTTPException, status, Depends

# development_db = ["DB for Development"]

# def get_db_session():
#     return development_db 

# app = FastAPI()


# @app.post("/add-item/")
# def add_item(item:str, db = Depends(get_db_session)):
#     db.append(item)
#     print(db)
#     #return db
#     return {"message":f"added item {item}"}


#=====Path dependency======

# from fastapi import FastAPI, Depends, HTTPException, status
# from typing import Optional

# app=FastAPI()

# def secret_header(secret_header:Optional[str]):

#     if secret_header!= "secret_value":
#         raise HTTPException(status.HTTP_403_FORBIDDEN)

# @app.get("/protected-route", dependencies=[Depends(secret_header)])
# async def protected_route():
#     return{"Hello":"World"}

#=====Function dependency========

 
# from fastapi import Depends, FastAPI

# app = FastAPI()

# async def properties(offset: int = 0, limit: int = 100):
#     return {"offset": offset, "limit": limit}

# @app.get("/books/")
# async def get_books(params: dict = Depends(properties)):
#     return params

# @app.get("/authors/")
# async def get_authors(params: dict = Depends(properties)):
#     return params



#==========Communicating with sql database using sqlalchemy======

#========Authentication============


# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.params import Depends
# from fastapi.security import APIKeyHeader

# API_TOKEN = "SECRET_API_TOKEN"


# app = FastAPI()


# api_key_header = APIKeyHeader(name="Token")


# @app.get("/protected-route")
# async def protected_route(token: str = Depends(api_key_header)):
#     if token != API_TOKEN:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return {"hello": "world"}


# async def api_token(token: str = Depends(APIKeyHeader(name="Token"))):
#     if token != API_TOKEN:
#      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

# @app.get("/protected-route", dependencies=[Depends(api_token)])
# async def protected_route():
#     return {"hello": "world"}





# from fastapi import FastAPI

# app = FastAPI()

# # sample data
# books = [
#     {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
# ]

# @app.get("/books")
# async def read_books(sort_by: str = None):
#     if sort_by:
#         # sort the books by the specified key
#         books_sorted = sorted(books, key=lambda x: x[sort_by])
#         return books_sorted
#     return books




from fastapi import FastAPI, File, UploadFile
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Response

app = FastAPI()

# Create a SQLAlchemy engine to connect to the database
engine = create_engine("sqlite:///./example.db")

# Create a session factory to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a model to represent uploaded files
class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content_type = Column(String)
    contents = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Read the contents of the uploaded file
    contents = await file.read()

    # Create a new database session
    db = SessionLocal()

    # Create a new UploadedFile object to represent the uploaded file
    uploaded_file = UploadedFile(filename=file.filename, content_type=file.content_type, contents=contents)

    # Add the new UploadedFile object to the session
    db.add(uploaded_file)

    # Commit the changes to the database
    db.commit()

    # Close the database session
    db.close()

    # Return a response indicating success
    return {"message": "File uploaded successfully"}
# from fastapi import FastAPI
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# app = FastAPI()

# # Create a SQLAlchemy engine to connect to the database
# engine = create_engine("sqlite:///./example.db")

# # Create a session factory to create database sessions
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create a base class for declarative models
# Base = declarative_base()

# # Define a model to represent uploaded files
# class UploadedFile(Base):
#     __tablename__ = "uploaded_files"

#     id = Column(Integer, primary_key=True, index=True)
#     filename = Column(String)
#     content_type = Column(String)
#     contents = Column(String)

# # Create the database tables
# Base.metadata.create_all(bind=engine)

@app.get("/file/{file_id}")
async def read_file(file_id: int):
    # Create a new database session
    db = SessionLocal()

    # Query the database for the uploaded file with the given ID
    uploaded_file = db.query(UploadedFile).filter(UploadedFile.id == file_id).first()

    # Close the database session
    db.close()

    # If the file was not found, return a 404 response
    if not uploaded_file:
        return {"message": "File not found"}

    # Otherwise, return a response with the file contents and content type
    return Response(content=uploaded_file.contents, media_type=uploaded_file.content_type, headers={"Content-Disposition": f"attachment; filename={uploaded_file.filename}"})
























































# from fastapi import FastAPI
# from fastapi.responses import FileResponse

# some_file_path = "Nandish P(Resume).pdf"
# app = FastAPI()


# @app.get("/")
# async def main():
#     return FileResponse(some_file_path)