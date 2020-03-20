from flask import render_template

from AppInit import app, csrf


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404

#
# @app.errorhandler(500)
# def error():
#     return render_template('500.html'), 500
#
#
# @csrf.error_handler
# def csrf_error(reason):
#     render_template('csrf_error.html', reason=reason), 400
