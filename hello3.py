import bottle

# this is the handler for the default path of the web server

@bottle.route('/')
def home_page():
    return "Hello world!\n"

@bottle.route('/testpage')
def test_page():
    return "this is test pagesdcsd\n"

bottle.debug(True)

bottle.run(host='localhost', port=8080)
