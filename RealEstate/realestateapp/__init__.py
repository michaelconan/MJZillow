from flask import Flask, render_template, session, request
from realestateapp.realestate import get_zestimate, get_comps
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/About/')
def about():
    return render_template('about.html')

@app.route('/Analysis/', methods=['GET','POST'])
def analysis():
    if request.method == 'POST':
        address = request.form['address']
        zestimate, zpid = get_zestimate(" ".join([request.form['address'], request.form['city'], request.form['state']]), request.form['zip'])
        comp_z, comp_b = get_comps(zpid)
        return render_template('analysis.html', address = address, zest = zestimate, comp = comp_z)
    return render_template('analysis.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')