from flask import Flask, flash, render_template, request, url_for, redirect
import pandas as pd
app = Flask(__name__)

data=pd.read_csv(r'C:\Users\jwang\Documents\DUKE\Courses\cloud_computing-ece590L\project1\cleaned.csv')

@app.route('/', methods=['GET', 'POST']) #get/post generates a request object
def search():
    #post: page generated after data is submitted;
    #you can use .form.get method to variables submitted
    #get: what u see when u access URL directly by typing
    if request.method=="POST":
        symp= request.form.get('symptom') #based on name=
        symp=symp.lower() #lower case
        diag= data.diagnose[data.symptom.str.contains(symp)].unique()

        if len(diag)==0: #no matches found
            return '<h1>Matches not found. Please try again. </h1>'
        else:
            #diag='\n'.join(diag)
            #return (print('\n'.join(diag)))
            return '<h1>The possible diagnoses are:</h1> {}'.format(','.join(diag))


    return '''<form method="POST">
                  Symptom: <input type="text" name="symptom"><br>
        
                  <input type="submit" value="Submit"><br>
              </form>'''
#def diagnose():


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)

