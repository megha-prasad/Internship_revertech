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
    
#The url_for() function is used to build a URL to the specific function dynamically. The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

# This function is useful in the sense that we can avoid hard-coding the URLs into the templates by dynamically building them using this function.

from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
if __name__ =='__main__':  
    app.run(debug = True)  
    
# HTTP is the hypertext transfer protocol which is considered as the foundation of the data transfer in the world wide web. All web frameworks including flask need to provide several HTTP methods for data communication.

# 1	GET	It is the most common method which can be used to send data in the unencrypted form to the server.
# 2	HEAD	It is similar to the GET but used without the response body.
# 3	POST	It is used to send the form data to the server. The server does not cache the data transmitted using the post method.
# 4	PUT	It is used to replace all the current representation of the target resource with the uploaded content.
# 5	DELETE	It is used to delete all the current representation of the target resource specified in the URL.
# We can specify which HTTP method to be used to handle the requests in the route() function of the Flask class. By default, the requests are handled by the GET() method.

# post example
login.html

<html>  
   <body>  
      <form action = "http://localhost:5000/login" method = "post">  
         <table>  
        <tr><td>Name</td>  
        <td><input type ="text" name ="uname"></td></tr>  
        <tr><td>Password</td>  
        <td><input type ="password" name ="pass"></td></tr>  
        <tr><td><input type = "submit"></td></tr>  
    </table>  
      </form>  
   </body>  
</html>  
Now, Enter the following code into the script named post_example.py.

# post_example.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  

# get eg
# login.html
<html>  
   <body>  
      <form action = "http://localhost:5000/login" method = "get">  
         <table>  
        <tr><td>Name</td>  
        <td><input type ="text" name ="uname"></td></tr>  
        <tr><td>Password</td>  
        <td><input type ="password" name ="pass"></td></tr>  
        <tr><td><input type = "submit"></td></tr>  
    </table>  
      </form>  
   </body>  
</html>  
Now, create the following python script as get_example.py.

# get_example.py

from flask import *  
app = Flask(__name__)  
  
  
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
    
The data is obtained by using the following line of code.

# uname = request.args.get('uname')  
# Here, the args is a dictionary object which contains the list of pairs of form parameter and its corresponding value.

# Flask facilitates us to render the external HTML file instead of hardcoding the HTML in the view function. Here, we can take advantage of the jinja2 template engine on which the flask is based.

# Flask provides us the render_template() function which can be used to render the external HTML file to be returned as the response from the view function.

# To render an HTML file from the view function, let's first create an HTML file named as message.html.

# message.html

<html>  
<head>  
<title>Message</title>  
</head>  
<body>  
<h1>hi, welcome to the website </h1>  
</body>  
</html>  
# script.py

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('message.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
# Here, we must create the folder templates inside the application directory and save the HTML templates referenced in the flask script in that directory.

# In our case, the path of our script file script.py is E:\flask whereas the path of the HTML template is E:\flask\templates.

# Application Directory
# script.py
# templates
# message.html

# Delimiters
# Jinga 2 template engine provides some delimiters which can be used in the HTML to make it capable of dynamic data representation. The template system provides some HTML syntax which are placeholders for variables and expressions that are replaced by their actual values when the template is rendered.

# The jinga2 template engine provides the following delimiters to escape from the HTML.

# {% ... %} for statements
# {{ ... }} for expressions to print to the template output
# {# ... #} for the comments that are not included in the template output
# # ... ## for line statements

# message.html

<html>  
<head>  
<title>Message</title>  
</head>  
<body>  
<h1>hi, {{ name }}</h1>  
</body>  
</html>  

# script.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/user/<uname>')  
def message(uname):  
      return render_template('message.html',name=uname)  
if __name__ == '__main__':  
   app.run(debug = True)  
    
# Due to the fact that HTML is a mark-up language and purely used for the designing purpose, sometimes, in the web applications, we may need to execute the statements for the general-purpose computations. For this purpose, Flask facilitates us the delimiter {%...%} which can be used to embed the simple python statements into the HTML.

# script.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/table/<int:num>')  
def table(num):  
      return render_template('print-table.html',n=num)  
if __name__ == '__main__':  
   app.run(debug = True)  
# print-table.py

<html>  
<head>  
<title>print table</title>  
</head>  
<body>  
<h2> printing table of {{n}}</h2>  
{% for i  in range(1,11): %}  
    <h3>{{n}} X {{i}} = {{n * i}} </h3>  
{% endfor %}  
</body>  
</html>  

# Referring Static files in HTML
# The static files such as CSS or JavaScript file enhance the display of an HTML web page. A web server is configured to serve such files from the static folder in the package or the next to the module. The static files are available at the path /static of the application.

# Example
# In the following example, the flask script returns the HTML file, i.e., message.html which is styled using the stylesheet style.css. The flask template system finds the static CSS file under static/css directory. Hence the style.css is saved at the specified path.

# script.py

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('message.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
# message.html

<html>  
<head>  
    <title>Message</title>  
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">  
</head>  
   
<body>  
    <h1>hi, welcome to the website</h1>  
</body>  
</html>  
# style.css

body {  
  background-color: powderblue;  
}  
h1 {  
  color: blue;  
}  
p {  
  color: red;  
}  

