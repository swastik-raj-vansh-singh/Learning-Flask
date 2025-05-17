## Here we are learing the flask from scratch 

## -- There are two imprting things 

## 1. web server gateway interface (WSGI)
it is the standard gateway between pyhton app and the server

as web server cann't run the python code directly do we need WSGI

visualization 
                            protocol WSGI
    web server  <---------------------------------------------> web app
    (azure app)                                                  (flask framework)



## 2. JINGA 2:
--web teplate enginne

visualization:

    web template  <------------------------------ Data Source
    (web pages)                                                (sql db , csv sheet,mongo db)
    
it create dynamic we pages 


## Installing the flask 

-- pip install flask 


## Basic Skeleton:

from flask import Flask 
app = Flask("__name__")

if __name__ == "__main__:
    app.run()

## now you are good to go 
