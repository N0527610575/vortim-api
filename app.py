"""
app.py — נקודת הכניסה של השרת.
כאן מגדירים את אפליקציית Flask ואת כל ה-routes.
פונקציות העזר לא נכתבות כאן — הן נמצאות ב-helpers.py ומיובאות לכאן.

בנה את הקובץ הזה לפי ההנחיות במסמכי docs/, שלב אחר שלב.
"""



from flask import Flask, jsonify, abort



app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False


@app.route("/")
def home():
    return jsonify({
        "status": "server is running"
    })


@app.get("/parshiot")
def get_parshiot():
    parshiot_list = "get_all_parshiot()"
    return jsonify({
        "parshiot": parshiot_list
    })


@app.get("/parshiot/<parsha>/vortim")
def vortim_for_parasha(parsha):
    vortim = "get_vortim_by_parsha(parsha)"
    if vortim is None:
        return jsonify({"error": f"Parsha '{parsha}' not found"}), 404

    return jsonify({
        "parsha": parsha,
        "vortim": vortim
    })


@app.get("/parshiot/<parsha>/vortim/<vort_id>")
def get_single_vort(parsha, vort_id):
    vort = "get_vort_by_id(parsha, vort_id)"
    if vort is None:
        return jsonify({"error": f"Vort with id '{vort_id}' not found in parsha '{parsha}'"}), 404

    return jsonify({
        "parsha": parsha,
        "vort_id": vort_id,
        "vort": vort
    })


if __name__ == "__main__":
    app.run(debug=True)