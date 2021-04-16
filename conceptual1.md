### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python has mutable and imutable data types. JavaScript does not.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

Use: get(key,def_val)  

- What is a unit test?

Different units of source code are put under different tests to see if they work.

- What is an integration test?

Testing with an integrated software to test the whole system of code.

- What is the role of web application framework, like Flask?

It provides you with tools, mechanics and libraries that will help to to more efficiantly build your application.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  One is a serch queery, the other are the actual results.

- How do you collect data from a URL placeholder parameter using Flask?
from flask import request

@app.route('/landingpage')
def landing_page():
    id = request.args['id']
    ...

- How do you collect data from the query string using Flask?
@app.route('/data')
def data():

- How do you collect data from the body of the request using Flask?
 request. get_data() 

- What is a cookie and what kinds of things are they commonly used for?

Data that tracks your preferences, behavior, and identifying information on a website.

- What is the session object in Flask?

An object used to track the session data.

- What does Flask's `jsonify()` do?
Returns a response object with the application/json mimetype set.
