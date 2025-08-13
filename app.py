import os
import pickle

from flask import Flask, render_template, request, jsonify

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
        # methode avec curl
        if request.is_json:
            data = request.get_json()
            print(data)
            checking_type = data["checking type"]
            engine_power_class = data["engine_power_class"]
            paint_color = data["paint_color"]
            has_gps = data["has_gps"]
            rental_price_per_day = data["rental_price_per_day"]

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


    return render_template("formulaire", result= result, request=request)
if __name__ == "__main__":
    app.run(debug=True)