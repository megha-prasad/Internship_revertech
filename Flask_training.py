# Flask is a web framework that provides libraries to build lightweight web applications in python. It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO).
# Flask is a web framework that provides libraries to build lightweight web applications in python. It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO). It is based on WSGI toolkit and jinja2 template engine. Flask is considered as a micro framework.
# WSGI- It is an acronym for web server gateway interface which is a standard for python web application development. It is considered as the specification for the universal interface between the web server and web application.
# Jinja2 is a web template engine which combines a template with a certain data source to render the dynamic web pages.

from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  
  
if __name__ =='__main__':  
    app.run(debug = True)  

# To build the python web application, we need to import the Flask module. An object of the Flask class is considered as the WSGI application.

# We need to pass the name of the current module, i.e. __name__ as the argument into the Flask constructor.

# The route() function of the Flask class defines the URL mapping of the associated function. The syntax is given below.

# app.route(rule, options)  
# It accepts the following parameters.

# rule: It represents the URL binding with the function.
# options: It represents the list of parameters to be associated with the rule object

# As we can see here, the / URL is bound to the main function which is responsible for returning the server response. It can return a string to be printed on the browser's window or we can use the HTML template to return the HTML file as a response from the server.

# Finally, the run method of the Flask class is used to run the flask application on the local development server.

# The syntax is given below.

app.run(host, port, debug, options)

# 1	host	The default hostname is 127.0.0.1, i.e. localhost.
# 2	port	The port number to which the server is listening to. The default port number is 5000.
# 3	debug	The default is false. It provides debug information if it is set to true.
# 4	options	It contains the information to be forwarded to the server.

# Flask facilitates us to add the variable part to the URL by using the section. We can reuse the variable by adding that as a parameter into the view function.
from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<name>')  
def home(name):  
    return "hello,"+name;  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
# The converter can also be used in the URL to map the specified variable to the particular data type. For example, we can provide the integers or float like age or salary respectively.
# The following converters are used to convert the default string type to the associated data type.

# string: default
# int: used to convert the string to the integer
# float: used to convert the string to the float.
# path: It can accept the slashes given in the URL.

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<int:age>')  
def home(age):  
    return "Age = %d"%age;  
  
if __name__ =="__main__":  
    app.run(debug = True) 
    
# add_url_rule(<url rule>, <endpoint>, <view function>)  
# This function is mainly used in the case if the view function is not given and we need to connect a view function to an endpoint externally by using this function.

from flask import Flask  
app = Flask(__name__)  
  
def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
# 
