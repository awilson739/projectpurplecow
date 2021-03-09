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

# Features to Add
1. Database for persistence
1. Update the item that matches the `id`
1. Logging


