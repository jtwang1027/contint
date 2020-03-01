## Continuous delivery of Flask application using Google App engine

In continuous delivery, code changes in the underlying pipeline can immediately trigger changes and updates to a running application. Google app engine  was used to build and deploy a web app. After, I tested the ability to make changes to the app file (main.py) and have these updates trigger and redploy an  updated web app. The purpose of the web application is to allow users to input a symptom for a condition or disease they are interested in, and the application will give a diagnosis and return a list of possible causes.

Google's App Engine was used to build and deploy a web application using the key files:

-*main.py* : primary Flask application   
-*app.yaml* :  specifies the python runtime  
-*requirements.txt* : additional packages that need to be installed  
-*cleaned.csv* : contains symptoms and diagnosis data. This was pulled from kaggle. [(link)](https://www.kaggle.com/plarmuseau/sdsort)  
-*cloudbuild.yaml* : builds the application  

To see a demo of this web app, view the demo mp4 video.[(link)](https://github.com/jtwang1027/contint)  
<img width="762" alt="search" src="https://user-images.githubusercontent.com/46359281/75284908-a1aec680-57e3-11ea-8053-a1640e6482f9.png">
<img width="744" alt="diagnosis" src="https://user-images.githubusercontent.com/46359281/75284881-98bdf500-57e3-11ea-87ae-1a97c7b0b89b.png">
<img width="706" alt="gcp_trigger" src="https://user-images.githubusercontent.com/46359281/75284851-8cd23300-57e3-11ea-9d24-4b5685b5849b.png">

