#! /usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']

@app.route('/')
def index():

    teacher = {
        'name': 'Jack',
        'email': 'dongqian3@qq.com'
    }

    course = {
        'name': 'Python Basic',
        'teacher': teacher,
        'user_count': 5348,
        'price': 199.0,
        'lab': None,
        'is_private': False,
        'is_member_course': True,
        'tags': ['python','big data','linux']
    }
    #return 'Hello Dongqian!'
    return render_template('index.html', course=course)

if __name__ == '__main__':
    app.run()