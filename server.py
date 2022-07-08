from flask import Flask
from about import me
from data import mock_data
import json

app= Flask ('server')
# print("hello from server")




@app.get("/")
def home():
    return "hello from server"

@app.get("/test")
def test():
    return "test"



@app.get("/about")
def about():
    return "this is the bookstore"




###################################################################################
#################### API ENDPOINTS =PRODUCTS ###################################
###################################################################################


@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def aboutMe():
    # return me["first"] + " " +me["last"]
    # return f
    return json.dumps(me) #parse dicitonary into json string



#get api products, return mock data in json string
@app.get("/api/products")
def aboutProducts():
    # return me["first"] + " " +me["last"]
    # return f
    return json.dumps(mock_data) #parse dicitonary into json string

# @app.post("/api/products")
@app.get("/api/products/<id>")
def get_product_by_id(id):
    # return "id is : " + id
    # for user in mock_data:
    #     if user["id"]== id:
    #         thing= json.dumps(user)
    # return thing
    for prod in mock_data:
        if str(prod["id"])==id:
            return json.dumps(prod)


    return "not found"


app.run(debug=True)