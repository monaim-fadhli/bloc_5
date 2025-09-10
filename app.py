import os
import pickle

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


with open("golden GB for car_location", "rb") as fr:
    model = pickle.load(fr)

@app.route("/", methods=["GET", "POST"])
def route_url():

    result= None
    if request.method == "POST":
        # methode avec curl
        if request.is_json:
            data = request.get_json()
            print(data)
            mileage = data["mileage"]
            engine_power = data["engine_power"]
            has_gps_num = data["has_gps_num"]
            automatic_car_num = data["automatic_car_num"]
            has_getaround_connect_num = data["has_getaround_connect_num"]
            has_air_conditioning_num = data["has_air_conditioning_num"]
            has_speed_regulator_num = data["has_speed_regulator_num"]
            car_type_num = data["car_type_num"]

        else:
            # methode avec formulaire

            mileage = int(request.form["mileage"])
            engine_power = int(request.form["engine_power"])
            has_gps_num = int(request.form["has_gps_num"])
            automatic_car_num = int(request.form["automatic_car_num"])
            has_getaround_connect_num = int(request.form["has_getaround_connect_num"])
            has_air_conditioning_num = int(request.form["has_air_conditioning_num"])
            has_speed_regulator_num = int(request.form["has_speed_regulator_num"])
            car_type_num = int(request.form["car_type_num"])
        result = round(model.predict([[mileage, engine_power , has_gps_num , automatic_car_num, has_getaround_connect_num, has_air_conditioning_num, has_speed_regulator_num, car_type_num]])[0],2)

        if request.is_json:
            return jsonify({"resultat de prediction (euros)": result})


    return render_template("formulaire.html", result= result, request=request)
@app.route("/docs", methods=["GET", "POST"])
def documentation_url():
    return render_template("documentation.html", request=request)
if __name__ == "__main__":
    app.run(debug=True)