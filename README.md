# Flask based REST API application 

This is a game-based application for riddles.Its purpose is to provide a riddles for an outdoor entertainment for a group of people. The target of the game is to find the answer of all questions.   


\*\* This repo contains only the Server-side part!  
\*\*The client for this project can be found [here](https://github.com/a-angeliev/Trivia-client)

## Install and run the app

  	pip install -r requirements.txt

## Routes
Routes that require an authentication

	"/riddles"
	"/riddles/<int:id_>"
	"/riddles/<int:id_>/events"
	"/event"
   	"/admin"
   	"/riddles/public"

Routes that do not require an authentication

	"/login"
	"/register"
	"/riddles/public"

 
# REST API

The REST API to the example app is described below.

## Register

### Request

`POST /register`

    curl -i -H 'Accept: application/json' -d '{"email": "test@test123.com","password": "12345a!"}'http://127.0.0.1:5000/register'


### Response

  
    Status: 201 OK
    Content-Type: application/json
    
    [{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5LCJleHAiOjE2NTAwNTQxNzh9.lGKagYwC2MROuFx-Ouh5NH2pMxRx
    _K89rTuxax3NiT8"}]

## LogIn

### Request

`POST /login`

    curl -i -H 'Accept: application/json' -d '{"email": "test@test123.com","password": "12345a!"}'http://127.0.0.1:5000/login'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5LCJleHAiOjE2NTAwNTQxNzh9.lGKagYwC2MROuFx-Ouh5NH2pMxR
    x_K89rTuxax3NiT8"}]
    
    
 ## Create a riddle

### Request

`POST /riddles`

    curl -i -H '{Accept: application/json, token: "token"}' -d '{"email": "test@test123.com","password": "12345a!"}'http://127.0.0.1:5000/riddles'


### Response

  
    Status: 201 OK
    Content-Type: application/json
    
    [{"title": "second riddle", "description": "this is the first riddle for our project", "id": 4,
    "questions": "question 1@question2@question 3", "discount": 0.0, "status": "available", "price": 10.0, "number_of_questions": 3,
    "answers": "answer 1@ Answer2@Answer 3"}]
    
    
  ## Get info about all riddles

### Request

`GET /riddles`

    curl -i -H '{Accept: application/json, token: "token"}' 'http://127.0.0.1:5000/riddles'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"title": "second riddle", "description": "this is the first riddle for our project", "id": 4,
    "questions": "question 1@question2@question 3", "discount": 0.0, "status": "available", "price": 10.0, "number_of_questions": 3,
    "answers": "answer 1@ Answer2@Answer 3"}]
    
    
  ## Update riddle by id

### Request

`PUT /riddles/<id>`

    curl -i -H '{Accept: application/json, token: "token"}' -d '{
    "title": "second riddle",
    "description": "this is the first riddle for our project",
    "price": 1500,
    "questions": "question 1@question2@question 3",
    "answers": "answer 1@ Answer2@Answer 3",
    "number_of_questions": 3}"'http://127.0.0.1:5000/riddles/1'


### Response

  
    Status: 201 OK
    Content-Type: application/json
    
    [{"title": "second riddle","description": "this is the first riddle for our project","price": 1500,
    "questions": "question 1@question2@question 3","answers": "answer 1@ Answer2@Answer 3",
    "number_of_questions": 3}]
    
    
   ## Find riddle by id

### Request

`GET /riddles/<id>`

    curl -i -H '{Accept: application/json, token: "token"}' 'http://127.0.0.1:5000/riddles/1'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"title": "second riddle","description": "this is the first riddle for our project","price": 1500,
    "questions": "question 1@question2@question 3","answers": "answer 1@ Answer2@Answer 3",
    "number_of_questions": 3}]
    
    
   ## Create event
   
### Request

`POST /riddles/<id>/event`

    curl -i -H '{Accept: application/json, token: "token"}' 'http://127.0.0.1:5000/riddles/1/event'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"url": "http://127.0.0.1:5000/event?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE4LCJleHAiOjE2NTAwMzA0
    OTV9.0CclxW8niLiGK--MFiz7rIznRV_puUhMK_QptS_MHrQ"}]
    
    
  ## Progres event
   
### Request

`GET /event?token=<token>`

    curl -i -H '{Accept: application/json, token: "token"}' 'http://127.0.0.1:5000/event?token=<token>'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"massage": f"You should start the riddle. Once the riddle start there is no money refunds anymore. Wind is <5 km/h. Weather 
    is good for riddles."}]
    
  ## Progres event
   
### Request

`POST /event?token=<token>`

    curl -i -H '{Accept: application/json, token: "token"}' -d '{'answer':'answer1'}' 'http://127.0.0.1:5000/event?token=<token>'


### Response

  
    Status: 200 OK
    Content-Type: application/json
    
    [{"question 2": f"question 2"}]
    
    
    
   ## Create admin
   
### Request

`POST /admin`

    curl -i -H '{Accept: application/json, token: "token"}' -d '{'email':'test@test.com'}' 'http://127.0.0.1:5000/admin'


### Response

  
    Status: 200 OK
    Content-Type: application/json


    
