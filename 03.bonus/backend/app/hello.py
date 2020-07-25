from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_csp.csp import csp_header

BASE_DOMAIN = '@@BASE_DOMAIN@@'
FIRST_DOMAIN = f'@@FIRST_SUBDOMAIN@@.{BASE_DOMAIN}'
SECOND_DOMAIN = f'@@SECOND_SUBDOMAIN@@.{BASE_DOMAIN}'
CSP = {
    'default-src':f"'self' http://*.{BASE_DOMAIN} 'unsafe-inline'",
    'script-src': f"'self' 'unsafe-eval' 'unsafe-inline' http://*.{BASE_DOMAIN}", 
    'img-src': f"'self' https://*.{BASE_DOMAIN}",
    'object-src': "'none'",
    'media-src': f"'self' https://*.{BASE_DOMAIN}",
    'font-src': f"'self' https://*.{BASE_DOMAIN}",
    'connect-src': f"'self' https://*.{BASE_DOMAIN} 'unsafe-inline'",
    'frame-src': f"'self' http://*.{BASE_DOMAIN}", 
    'base-uri': f"'self' http://*.{BASE_DOMAIN}", 
    "block-all-mixed-content": ""
}

app = Flask(__name__, host_matching=True, static_host=FIRST_DOMAIN)
app.config['BASE_DOMAIN'] = BASE_DOMAIN
app.config['FIRST_DOMAIN'] = FIRST_DOMAIN
app.config['SECOND_DOMAIN'] = SECOND_DOMAIN

@app.before_request
def domain_check():
    # Invalid host redirect
    if request.headers.get('Host') not in [FIRST_DOMAIN, SECOND_DOMAIN]:
        return redirect(request.url_root)

@app.route('/', host=FIRST_DOMAIN, methods=['GET','POST'])
@csp_header(CSP)
def index():
    #request.environ['wsgi.input_terminated'] = True
    return render_template("index.html")

@app.route('/us/gifts', host=FIRST_DOMAIN, methods=['GET','POST'])
def us_gifts():
    #request.environ['wsgi.input_terminated'] = True
    return render_template("gifts.html")

@app.route('/i', host=SECOND_DOMAIN, methods=['GET','POST'])
def i():
    #request.environ['wsgi.input_terminated'] = True
    js_src = request.args.get('js_src')
    return render_template("i.html", js_src=js_src)

@app.route('/fb.js', host=SECOND_DOMAIN, methods=['GET','POST'])
def fbjs():
    ret = """
var real_world='http request smuggling attack scenario';
var author='zairo';
"""
    return ret

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True, threaded=True)
