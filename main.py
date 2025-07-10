import os
import pickle

from flask import Flask, render_template, request

app = Flask(__name__)


with open("golden svc for car_location", "rb") as fr:
    model = pickle.load(fr)

@app.route("/", methods=["GET", "POST"])
def route_url():
    dict_result =  {
        0 : "Location non risque",
        1 : "Location a risque"
    }
    result= None
    if request.method == "POST":
        checking_type = int(request.form["checking type"])
        engine_power_class = int(request.form["engine_power_class"])
        paint_color = int(request.form["paint_color"])
        has_gps = int(request.form["has_gps"])
        rental_price_per_day = int(request.form["rental_price_per_day"])
        result_ = model.predict([[checking_type, engine_power_class , paint_color , has_gps, rental_price_per_day]])[0]
        result = dict_result[result_]


    return render_template("hello.html", result= result, request=request)
if __name__ == "__main__":
    app.run(debug=True)


