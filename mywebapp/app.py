from flask import Flask, url_for

# The url_for() function is very useful for dynamically building a URL for a specific function. The function accepts the name
# of a function as first argument, and one or more keyword arguments, each corresponding to the variable part of URL.
# However, there is no need to put this here.

app = Flask(__name__)


# Create default route and return/display 'Hello World'
@app.route('/')
def hello_world():
    return "Hello World"


# Create admin route and return/display 'welcome to the admin page'
@app.route('/admin')
def admin_page():
    return "welcome to the admin page"


# Create guest route and return/display 'Hello <Name> as Guest'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


# When a user named admin navigates to localhost:5000/user/<name> in the browser, they are redirected to the
# admin_page.
# When a user NOT named admin navigates to localhost:5000/user/<name> in the browser, they are redirected to the
# hello_guest page.
@app.route('/user/<name>')
def redirect_admin(name):
    if name == "admin":
        return admin_page()
    else:
        return hello_guest(name)


if __name__ == '__main__':
    app.run()
