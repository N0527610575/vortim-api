"""
helpers.py — כל פונקציות העזר של הפרויקט נמצאות כאן בלבד.
app.py מייבא מכאן. אל תכתוב לוגיקה כבדה בתוך ה-routes עצמם.

הפונקציות שתבנה כאן לפי ההנחיות (השמות מופיעים במסמכי docs/):
  load_vortim_for_parsha(parsha_name)
  load_single_vort(parsha_name, vort_id)
  is_long(text)
  load_users() / save_users(users)
  load_admins()
  hash_password(password) / verify_password(password, hashed)
  create_token(username) / decode_token(token)
  get_current_parsha()
  validate_vort(data)
"""
import os
import json

BASE_PARSHIOT_DIR = os.path.join("data", "parshiot")


def is_long(text: str) -> bool:

    if not text:
        return False
    return len(text.splitlines()) > 20


def get_all_parshiot():

    if not os.path.exists(BASE_PARSHIOT_DIR):
        return []

    parshiot = [
        name for name in os.listdir(BASE_PARSHIOT_DIR)
        if os.path.isdir(os.path.join(BASE_PARSHIOT_DIR, name))
    ]
    return sorted(parshiot)


def load_vortim_for_parsha(parsha_name: str):

    parsha_path = os.path.join(BASE_PARSHIOT_DIR, parsha_name)

    if not os.path.isdir(parsha_path):
        return None

    vortim = []
    for filename in sorted(os.listdir(parsha_path)):
        if filename.endswith(".json"):
            file_path = os.path.join(parsha_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                vort_data = json.load(f)
                vort_data["is_long"] = is_long(vort_data.get("text", ""))
                vortim.append(vort_data)

    return vortim


def load_single_vort(parsha_name: str, vort_id: str):

    parsha_path = os.path.join(BASE_PARSHIOT_DIR, parsha_name)
    if not os.path.isdir(parsha_path):
        return None

    file_path = os.path.join(parsha_path, f"{vort_id}.json")
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        vort_data = json.load(f)
        vort_data["is_long"] = is_long(vort_data.get("text", ""))
        return vort_data