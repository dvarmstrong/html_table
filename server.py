from flask import Flask, render_template 

app = Flask(__name__)


@app.route('/')
def my_table():
    users = [
        {'first_name' : 'Micheal', 'last_name' : 'Choi', 'Birthday':'1-19-1981'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'Birthday': '12-8-1972'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'Birthday': '7-4-1963'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'Birthday': '2-14-1990'},
        {'first_name' : 'Bill', 'last_name' : 'Wilkin', 'Birthday': '3-25-1989'},
        {'first_name' : 'Mel', 'last_name' : 'B', 'Birthday': '5-2-1970'},
        {'first_name' : 'Adrien', 'last_name' : 'Nibb', 'Birthday': '4-15-1992'},
        {'first_name' : 'Dimitri', 'last_name' : 'Armstrong', 'Birthday': '7-13-1979'}
    ]


    return render_template('index.html', user=users)






if __name__=="__main__":
    app.run(debug=True)