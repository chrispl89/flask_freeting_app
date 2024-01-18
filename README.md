## Flask App with Flash Messages

This is a simple Flask web application that greets the user. It utilizes the Flask web framework and includes flash messages for user interactions. Below is a breakdown of the code and the libraries used:

### Libraries Used:

1. **Flask:**
   - Flask is a micro web framework for Python. It is easy to use and does not have rigid dependencies, making it a popular choice for building web applications. In this code, Flask is used to define routes and render HTML templates.

2. **render_template:**
   - The `render_template` function from Flask is used to render HTML templates. It enables the use of HTML files to structure the views of the application.

3. **request:**
   - The `request` object from Flask is used to handle incoming HTTP requests. In this code, it is utilized to access form data submitted by the user.

4. **flash:**
   - Flash messages are used to display temporary messages to the user. The `flash` function from Flask is employed to store messages that can be retrieved and displayed in the HTML templates.


### Setup and Run:

Before running the code, ensure that you have Flask installed. You can install it using:


pip install Flask


To run the application, set the Flask environment variables and execute the script:


set FLASK_APP=app_name.py

set FLASK_ENV=development

flask run


Visit [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello) in your web browser to interact with the application.

Feel free to customize and expand upon this code for your specific use case.
