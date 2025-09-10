import os
import pickle

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


with open("golden GB for car_location", "rb") as fr:
    model = pickle.load(fr)

@app.route("/", methods=["GET", "POST"])
def route_url():
    dict_result =  {
        0 : "Location non risque",
        1 : "Location a risque"
    }
    result= None
    if request.method == "POST":
        # methode avec curl
        if request.is_json:
            data = request.get_json()
            print(data)
            mileage = data["mileage"]
            engine_power_class = data["engine_power_class"]
            automatic_car_num = data["automatic_car_num"]
            has_gps = data["has_gps"]
            has_getaround_connect_num = data["has_getaround_connect_num"]
            has_air_conditioning_num = data["has_air_conditioning_num"]
            has_speed_regulator_num = data["has_speed_regulator_num"]
            car_type_num = data["car_type_num"]

        else:
            # methode avec formulaire

            checking_type = int(request.form["checking type"])
            engine_power_class = int(request.form["engine_power_class"])
            paint_color = int(request.form["paint_color"])
            has_gps = int(request.form["has_gps"])
            rental_price_per_day = int(request.form["rental_price_per_day"])
        result_ = model.predict([[checking_type, engine_power_class , paint_color , has_gps, rental_price_per_day]])[0]
        result = dict_result[result_]
        if request.is_json:
            return jsonify({"resultat de prediction": result})


    return render_template("formulaire.html", result= result, request=request)
@app.route("/docs", methods=["GET", "POST"])
def documentation_url():
    return render_template("documentation.html", request=request)
if __name__ == "__main__":
    app.run(debug=True)