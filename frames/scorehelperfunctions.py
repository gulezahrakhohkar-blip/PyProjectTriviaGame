import json, os
from frames.utils import widgets

PROGRESS_FILE = "prog.json"


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                data = json.load(f)
                data["completed_topics"] = set(data.get("completed_topics", []))
                if "topic_scores" not in data:
                    data["topic_scores"] = {}
                return data
        except Exception:
            pass
    return {
        "unlocked_topics": 1,
        "score": 0,
        "completed_topics": set(),
        "topic_scores": {}
    }

progress = load_progress()

def save_progress():
    data = {
        "unlocked_topics": progress["unlocked_topics"],
        "score": progress["score"],
        "completed_topics": list(progress["completed_topics"]),
        "topic_scores": progress.get("topic_scores", {})
    }
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_score(amount=1):
    if "score" not in progress:
        progress["score"] = 0
    progress["score"] += amount
    save_progress()
    refresh_score()

def get_score():
    return progress.get("score", 0)

def refresh_score():
    if widgets.get("score"):
        try:
            widgets["score"][0].setText(f"Score: {get_score()}")
        except Exception:
            pass

def reset_progress():
    from frames.frames12 import frame2
    global progress
    progress = {
        "unlocked_topics": 1,
        "score": 0,
        "completed_topics": set(),
        "topic_scores": {}
    }
    save_progress()
    frame2()

# Stats helpers
def get_highest(topic):
    return max(progress.get("topic_scores", {}).get(topic, [0]), default=0)

def get_average(topic):
    scores = progress.get("topic_scores", {}).get(topic, [])
    if not scores:
        return 0
    return int((sum(scores) / (len(scores) * 10)) * 100)

def get_overall_highest():
    h = 0
    for scores in progress.get("topic_scores", {}).values():
        if scores:
            h = max(h, max(scores))
    return h

def get_overall_percentage():
    total_attempts, earned = 0, 0
    for scores in progress.get("topic_scores", {}).values():
        for s in scores:
            total_attempts += 10
            earned += s
    if total_attempts == 0:
        return 0
    return int((earned / total_attempts) * 100)

