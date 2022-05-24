Search engine - capstone project.
Working branch is the cosim branch.

A limited search engine that works on a local dataset (Wikipedia articles)

**Important to Have Installed**
1) Postgresql
2) Nodejs
3) Flask

Using Windows:
1) Go to the server folder directory -> run command "nodemon index" 
2) Go to the server folder directory -> run command "set FLASK_RUN_PORT=8000" -> run command "python app.py" or "flask run"
3) Go to the client folder directory -> run command "npm install" -> run command "npm start"

Assuming node already installed
Using Mac:
1) client folder -> npm start
2) server folder -> npx nodemon index
3) server folder -> export FLASK_RUN_PORT=8000 FLASK_ENV=development FLASK_APP=app.py -> flask run

Possible errors during installation
Flask only reliably imported packages correctly when installed via conda vs pip
