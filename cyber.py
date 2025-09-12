from flask import Flask, jsonify, request,session
from datetime import datetime, timedelta

app = Flask(__name__)

# 21 videos (you can later move this to a database)
videos = [
    {"day": 1, "title": "Your safety online is in your hands – Report, Protect, and Stay Cyber Aware!", "description": "Intro to Cyber Awareness", "youtube_id": "w_r-_VbpHFc?si=s_lBR5p9_CFKLPcW"},
    {"day": 2, "title": "Empowering Women with Cyber Awareness", "description": "Fake profiles and extortion", "youtube_id": "9Q8tauXl5pY?si=hRItFm8EGne9za_v"},
    {"day": 3, "title": "What are the laws for safe Cyber Space for Women?", "description": "understanding legal protections", "youtube_id": "taYuna1SfOM?si=KSekKo9maLUEvoBH"},
    {"day": 4, "title": "Girls safety awareness - Girls are Easy Target on Social platforms, Learn to be Safe", "description": "Safety Tips", "youtube_id": "xavhHIMNV_s?si=MdAhITYjnS3_3iTS"},
    {"day": 5, "title": "Cybercrime Awareness", "description": "Picture morphing", "youtube_id": "nOqW9qniMys?si=COnYtnipyNn-nhBm"},
    {"day": 6, "title": "", "description": "", "youtube_id": ""},
    {"day": 7, "title": "", "description": "", "youtube_id": ""},
    {"day": 8, "title": "", "description": "", "youtube_id": ""},
    {"day": 9, "title": "", "description": "", "youtube_id": ""},
    {"day": 10, "title": "", "description": "", "youtube_id": ""},
    {"day": 11, "title": "", "description": "", "youtube_id": ""},
    {"day": 12, "title": "", "description": "", "youtube_id": ""},
    {"day": 13, "title": "", "description": "", "youtube_id": ""},
    {"day": 14, "title": "", "description": "", "youtube_id": ""},
    {"day": 15, "title": "", "description": "", "youtube_id": ""},
    {"day": 16, "title": "", "description": "", "youtube_id": ""},
    {"day": 17, "title": "", "description": "", "youtube_id": ""},
    {"day": 18, "title": "", "description": "", "youtube_id": ""},
    {"day": 19, "title": "", "description": "", "youtube_id": ""},
    {"day": 20, "title": "", "description": "", "youtube_id": ""},
    {"day": 21, "title": "", "description": "", "youtube_id": ""},
]
    # ... repeat until day 21

# temporary "user progress" store (later: use DB)
user_progress = {}

@app.route("/course", methods=["GET"])
def get_course():
    return jsonify(videos)

@app.route("/course/<int:day>", methods=["GET"])
def get_day(day):
    video = next((v for v in videos if v["day"] == day), None)
    if video:
        video["embed_url"] = f"https://www.youtube.com/embed/{video['youtube_id']}"
        return jsonify(video)
    return jsonify({"error": "Day not found"}), 404


    

@app.route("/progress", methods=["POST"])
def update_progress():
    if 'username' not in session:
        return jsonify({"error": "User not logged in"}), 401

    user = session['username']
    data = request.json
    day = data.get("day")

    if not day:
        return jsonify({"error": "Missing day"}), 400


    user_progress.setdefault(user, []).append(day)
    if day not in [d['day'] for d in user_progress[user]]:
        user_progress[user].append({
            "day": day,
            "COMPLETION AT": datetime.now().isoformat()
        })
        user_progress[user].append(day)

    return jsonify({"message": "Progress updated", "progress": user_progress[user]})

@app.route("/progress/<user>", methods=["GET"])
def get_progress(user):
    return jsonify({"user": user, "progress": user_progress.get(user, [])})

if __name__== "_main_":
    app.run(debug=True)