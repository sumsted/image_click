import os
from bottle import run, get, post, request, template, static_file, route


@get('/')
def get_index():
    return template('index', images=[])


@get('/images')
def get_image():
    return {'images': []}


@post('/image')
def post_message():
    return {'status': 'SUCCESS'}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
