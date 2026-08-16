"""
app.py — נקודת הכניסה של השרת.
כאן מגדירים את אפליקציית Flask ואת כל ה-routes.
פונקציות העזר לא נכתבות כאן — הן נמצאות ב-helpers.py ומיובאות לכאן.

בנה את הקובץ הזה לפי ההנחיות במסמכי docs/, שלב אחר שלב.
"""






from flask import Flask, jsonify
from helpers import (
    get_all_parshiot,
    load_vortim_for_parsha,
    load_single_vort
)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def home():
    return jsonify({"status": "server is running"})


@app.get("/parshiot")
def get_parshiot():
    parshiot_list = get_all_parshiot()
    return jsonify(parshiot_list), 200


@app.get("/parshiot/<parsha>/vortim")
def get_vortim_for_parsha(parsha):
    vortim = load_vortim_for_parsha(parsha)
    if vortim is None:
        return jsonify({"error": f"Parsha '{parsha}' not found"}), 404
    return jsonify(vortim), 200


@app.get("/parshiot/<parsha>/vortim/<vort_id>")
def get_single_vort(parsha, vort_id):
    vort = load_single_vort(parsha, vort_id)
    if vort is None:
        return jsonify({"error": f"Vort '{vort_id}' not found in parsha '{parsha}'"}), 404
    return jsonify(vort), 200


@app.get("/current")
def get_current_parsha():
    return jsonify({"current_parsha": "bereshit"}), 200


if __name__ == "__main__":
    app.run(debug=True)