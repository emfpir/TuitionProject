from flask import Flask
from controllers import site_controller
from flask_cors import CORS
from datetime import date, timedelta, datetime

app = Flask(__name__)
CORS(app)
site_controller.route(app)


if __name__ == '__main__':
    # print(date.today().strftime("%Y-%m-%d"))
    # print(date.today())
    # endDate = date.today()+timedelta(days=5)
    # print(endDate)
    # dateNow = str(date.today().strftime("%Y-%m-%d"))
    # beginDate = datetime.strptime(dateNow, "%Y-%m-%d")
    # print((beginDate+timedelta(days=5)))
    app.run(debug=True)




