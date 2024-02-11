from flask import Flask, jsonify, request, abort 
from flasgger import Swagger, swag_from
# import sys
# sys.path.append('../../')
# from search_jobs import Scrape_Place
# from ...


app = Flask(__name__)

swagger = Swagger(app)
swag = {"swag": True,
        "tags": ["demo"],
        "responses": {200: {"description": "Success request"},
                      400: {"description": "Validation error"}}}


@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 


@app.route('/api/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)

@app.route('/api/job/<string:jobId>', methods=['POST, GET'], **swag)
def job(jobId):
    """Example endpoint returning jobId
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Job Description
        in: path
        type: string
        required: true
        default: all
    definitions:
      Job Description:
        type: string
    responses:
      200:
        description: A jobId
        schema:
          $ref: '#/definitions/Job Description'
        examples:
          results: ''
    """
    error = None
    if request.mehod != 'POST':
        app.logger.error('An error occurred')
        # abort(404)
    if request.method == 'POST':
        app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.debug('A value for debugging')
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return jsonify('result', jsonify(jobId))

@app.route('/api/jobs/<string:jobId>')
def jobs(jobId):
    """Example endpoint returning jobId
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Job Description
        in: path
        type: string
        required: true
        default: all
    definitions:
      Job Description:
        type: string
    responses:
      200:
        description: A jobId
        schema:
          $ref: '#/definitions/Job Description'
        examples:
          results: ''
    """
    error = None
    if request.mehod != 'POST':
        app.logger.error('An error occurred')
        # abort(404)
    if request.method == 'POST':
        app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.debug('A value for debugging')
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return jsonify('result', jsonify(jobId))

if __name__ == "__main__": app.run(debug=True)
