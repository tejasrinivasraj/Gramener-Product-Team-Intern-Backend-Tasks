from flask import Flask, render_template, request, flash
from forms import DetailsForm
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def main():
    form = DetailsForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('main.html', form = form)
        else:
            try:
                 name = request.form['name']
                 age = request.form['Age']
                 gender = request.form['Gender']
    
                 with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO students (name,age,gender) VALUES (?,?,?)",(name,age,gender))                    
                    con.commit()
                    msg = "Record successfully added"
            except:
                con.rollback()
                msg = "error in insert operation"
              
            finally:
                con = sql.connect("database.db")
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("select * from students")
               
                rows = cur.fetchall();
                return render_template("success.html",rows = rows)
                con.close()
    elif request.method == 'GET':
        return render_template('main.html', form = form)
@app.route('/data')
def display():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from students")
   
    rows = cur.fetchall();
    return render_template("success.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
