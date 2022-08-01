# encoding=utf-8
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from flask import redirect
from flask import make_response
from flask import flash
from flask_script import Manager

from api.app import create_app
from autoapp import app


@app.errorhandler(403)
def not_found(error):
    if getattr(request, 'is_xhr', True):
        return make_response(jsonify(message=error.description), 403)
    flash(u"您的权限不够", "error")
    if request.referrer is not None:
        return redirect(request.referrer)
    else:
        return redirect(url_for("dashboard.index"))


@app.errorhandler(404)
def not_found(error):
    if getattr(request, 'is_xhr', True):
        return make_response(jsonify(message=error.description), 404)
    print('error')
    print(error)
    a = request
    return make_response(jsonify(message=error.description), 404)


@app.errorhandler(400)
def server_error(error):
    if getattr(request, 'is_xhr', True):
        return make_response(jsonify(message=error.description), 400)
    flash(error.description, "error")
    if request.referrer is not None:
        return redirect(request.referrer)
    else:
        return redirect(url_for("home.index"))


@app.errorhandler(500)
def server_error(error):
    if getattr(request, 'is_xhr', True):
        return make_response(jsonify(message=error.description), 500)
    return render_template("500.html", error=error.message), 500


manager = Manager(app)

app = create_app()

if __name__ == '__main__':
    manager.run()
