import os
from flask import Flask, render_template, request

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        DATABASE =os.path.join(app.instance_path, 'flaskr.sqlite'),
        )
    if test_config is None:
        app.config.from_pyfile('config', silent =True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #routes

#    @app.route("/")
#    def index():
#        return render_template('index.html')

#    @app.route('/home')
#   def home():
#        return render_template('home.html')

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    

    return app
