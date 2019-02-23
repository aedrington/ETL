from flask import Flask, request, render_template
import pymysql

db = pymysql.connect("localhost", "username", "password", "database")

app = Flask(__name__)
def TablePull(pull):
	cursor = db.cursor()
    
	cursor.execute(pull)
    results = cursor.fetchall()
	return results


@app.route('/')
def PullDatabase():
	
    jobsTable=TablePull("SELECT * from ETLProject.jobs LIMIT 5")
	abbTable=TablePull("SELECT * from ETLProject.abbreviations LIMIT 5")
	popTable = TablePull("SELECT * from ETLProject.abbreviations LIMIT 5")
	statesTable=TablePull("SELECT * from ETLProject.states LIMIT 5")
	FinalTable =TablePull("SELECT * from ETLProject.Final")
	
	return render_template('index.html', results=results)

if __name__ == '__main__':
	app.run(debug=True)