# Project Requirements

- [x] Use flask
- [ ] Using GET method
- [ ] Must use OpenAPI standard with JSON responses
- [ ] Able to search by title, amenities, price, location
- [ ] I can sort by price
- [ ] Must use JWT Token

# Breaking down the task

- [x] Able to retrieve data from database
- [x] Show a json reponse of your data

# Note

- Note: When opening a new terminal, or when you close the one you are running the development server on and want to rerun it, it is important to remember activating the virtual environment and setting the environment variables FLASK_ENV and FLASK_APP for the flask run command to work properly.

```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

- If you want to run both applications at the same time, you can pass a different port number to the -p argument, for example, to run another application on port 5001 use the following command:

```
 flask run -p 5001
```

With this you can have one application running on http://127.0.0.1:5000/ and another one on http://127.0.0.1:5001/ if you want to.

# What I learned

- Decorators has to be above trhe method that wqe want to target. "@app.route is a decorator that turns a regular Python function into a Flask view function, which converts the function’s return value into an HTTP response to be displayed by an HTTP client, such as a web browser. You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL."

- Whatever you give in the url, whether it is uppercase or lowercase, it'll convert it to lowercase and worek wioth it.

- '''.upper()''' will make all capital and '''.capitalize()''' will make the 1st character capital

# Problems and solution

- [x] Installing flask

```
python3 -m venv venv
source venv/bin/activate
pip install flask

```

https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
If facng problem doing the above, then read this: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

- [x] Ignoring venv subdirectories => 'venv/' in gitignore

# Helpful

- You use the escape() function you imported earlier to render the word string as text. This is important to avoid Cross Site Scripting (XSS) attacks. If the user submits malicious JavaScript instead of a word, escape() will it render as text and the browser will not run it, keeping your web application safe.

- abort() for error responses

- HTTP (Hypertext Transfer Protocol) is the primary means of communicating data on the web. HTTP implements a number of “methods,” which tell which direction data is moving and what should happen to it. The two most common are GET, which pulls data from a server, and POST, which pushes new data to a server.

- URL (Uniform Resource Locator) - An address for a resource on the web, such as https://programminghistorian.org/about. A URL consists of a protocol (http://), domain (programminghistorian.org), and optional path (/about). A URL describes the location of a specific resource, such as a web page. When reading about APIs, you may see the terms URL, request, URI, or endpoint used to describe adjacent ideas.

- JSON (JavaScript Object Notation) is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.

- REST (REpresentational State Transfer) is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs. While the API outlined in this lesson uses some REST principles, there is a great deal of disagreement around this term. For this reason, I do not describe the example APIs here as REST APIs, but instead as web or HTTP APIs.

  2022.01.12

- https://www.youtube.com/watch?v=k10ILjUyWuQ
- https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f
- https://www.tutorialspoint.com/flask/flask_http_methods.htm
- https://www.tutorialspoint.com/flask/flask_templates.htm
- https://www.google.com/search?channel=fs&client=ubuntu&q=take+data+from+database+and+show+it+as+JSON+Restful+OpenAPI+using+flask
- https://realpython.com/flask-connexion-rest-api/
