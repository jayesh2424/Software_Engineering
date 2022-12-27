from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def greeting():
    # Get Input birthday date and today's date
    name = request.args.get('name')
    dateToday = request.args.get('date')
    birthdate = request.args.get('birthday')
    
    # Convert the dates to datetime objects
    dateToday = datetime.strptime(dateToday, '%Y-%m-%d')
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    
    # Check if it is the user's birthday
    #use '.strftime' to take the time out of the date comparison
    if dateToday.strftime('%m-%d') == birthdate.strftime('%m-%d'):
        return '<h1>Happy Birthday Dear {name}!</h1>'
    else:
        return "<h1>This is a simple Web-Server</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)
