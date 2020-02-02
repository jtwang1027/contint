from flask import Flask #, flash, render_template, request, url_for, redirect
import pandas as pd


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

data=pd.read_csv(r'cleaned.csv') #loads symptom-diagnosis data

@app.route('/', methods=['GET', 'POST']) #get/post generates a request object
def search():
    #post: page generated after data is submitted;
    #you can use .form.get method to retrieve submitted variables
    #get: what you see when you access URL directly by typing
    if request.method=="POST":
        symp= request.form.get('symptom') #based on name=
        symp=symp.lower() #lower case
        diag= data.diagnose[data.symptom.str.contains(symp)].unique()

        if len(diag)==0: #no matches found
            return '<h1>Matches not found. Please try again. </h1>'
        else:

            return '<h1>The possible diagnoses are:</h1> {}'.format(','.join(diag))


    return '''<form method="POST">
                  Symptom: <input type="text" name="symptom"><br>
        
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
