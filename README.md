# Continuous delivery of Google App Enginge using Google cloud platform


<p>In continuous delivery, code changes in the underlying pipeline can immediately trigger changes and updates to a running application. Google app engine&nbsp; was used&nbsp;to build and deploy a web app. After, I tested the ability to make changes to the app file (main.py) and have these updates trigger and redploy an&nbsp; updated web app. The purpose of the web application is to allow users to input a symptom for a condition or disease they are interested in, and the application will give a diagnosis and return a list of possible causes.</p>

<p>Google&#39;s App Engine was used to build and deploy a web application using the key files:</p>

<ul>
	<li>main.py : primary Flask application&nbsp;</li>
	<li>app.yaml : &nbsp;specifies the python runtime</li>
	<li>requirements.txt : additional packages that need to be installed</li>
	<li>cleaned.csv : contains symptoms and diagnosis data. This was pulled from&nbsp;kaggle (<a href="https://www.kaggle.com/plarmuseau/sdsort" rel="nofollow">https://www.kaggle.com/plarmuseau/sdsort</a>).&nbsp;</li>
	<li>cloudbuild.yaml : builds the application</li>
</ul>

<p>To see a demo of this web app, view the demo mp4 video.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
