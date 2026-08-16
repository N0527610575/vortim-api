"""
app.py — נקודת הכניסה של השרת.
כאן מגדירים את אפליקציית Flask ואת כל ה-routes.
פונקציות העזר לא נכתבות כאן — הן נמצאות ב-helpers.py ומיובאות לכאן.

בנה את הקובץ הזה לפי ההנחיות במסמכי docs/, שלב אחר שלב.
"""
from flask import  Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "{ status: server is running }"

if __name__ == "__main__":
    app.run()