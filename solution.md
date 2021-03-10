# Project Purple Cow

# Installation
`pip3 install requirements.txt`
`python3 app.py`

It currently runs on port `3000` however that can be changed by modifying the `config` file. 

## Docker
`docker build -t project-purple-cow .`
`docker run --name project-purple-cow -p 3000:3000 project-purple-cow`

# What does this app do?
Currently, it will add/delete/list items by id and name.
Add item:  
`curl -H "Content-Type: application/json" -d {"id":"1","name":"something"} 127.0.0.1:3000/item`  
List items:  
`curl 127.0.0.1:3000/item`  
Delete Item:  
`curl -H "Content-Type: application/json" -X DELETE -d {"id":"1"} 127.0.0.1:3000/item`  
# Features to Add
1. Database for persistence
1. Update the item that matches the `id`
1. Delete Multiple items
1. Add Multiple items
1. Logging


