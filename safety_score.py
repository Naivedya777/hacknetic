# -------------------------
# Safety Score Engine
# -------------------------

from collections import Counter
import re

# Penalty system: higher points = more severe
PENALTY = {
    "abuse": 15,
    "harass": 20,
    "stalk": 25,
    "threat": 30,
    "creep": 10,
    "idiot": 10,
    "dumb": 10,
    "stupid": 15,
    "loser": 10,
    "ugly": 15,
    "hate": 20,
    "fraud": 15,
    "trash": 15,
    "jerk": 15,
    "troll": 15,
    "noob": 10
}

# -------------------------
# Classification
# -------------------------
def classify_score(score: float) -> str:
    """Convert score to category."""
    if score >= 71:
        return "Safe"
    elif score >= 41:
        return "Moderate"
    else:
        return "Unsafe"

# -------------------------
# Single Message Scoring
# -------------------------
def calculate_safety_score(message: str) -> dict:
    """Calculate safety score for a single message."""
    score = 100
    detected_words = Counter()
    msg_lower = message.lower()
    
    for word, penalty in PENALTY.items():
        # Use word boundaries to avoid partial matches
        if re.search(rf"\b{re.escape(word)}\b", msg_lower):
            score -= penalty
            detected_words[word] += 1
    
    score = max(score, 0)  # no negative scores
    status = classify_score(score)
    
    # Suggestion based on score
    if score < 41:
        suggestion = "Unsafe: Consider blocking or reporting users."
    elif score < 71:
        suggestion = "Moderate: Be cautious and use privacy settings."
    else:
        suggestion = "Safe: Community seems healthy."
    
    return {
        "score": score,
        "status": status,
        "detected_words": dict(detected_words),
        "suggestion": suggestion
    }

# -------------------------
# Batch Analysis
# -------------------------
def analyze_messages(messages: list[str]) -> dict:
    """Analyze a batch of messages and return average score."""
    results = []
    total_score = 0
    
    for msg in messages:
        result = calculate_safety_score(msg)
        results.append({"message": msg, **result})
        total_score += result["score"]
    
    average_score = total_score / len(messages) if messages else 100
    overall_status = classify_score(average_score)
    
    return {
        "average_score": round(average_score, 2),
        "overall_status": overall_status,
        "results": results
    }