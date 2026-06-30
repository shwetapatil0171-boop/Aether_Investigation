from flask import Flask, render_template, session, redirect, url_for
import random

from data import victims, locations, suspects, weapons, occupations, ages, personalities

app = Flask(__name__)
app.secret_key = "aether_secret_key"


# -------------------------
# SCORE SYSTEM
# -------------------------
def calculate_score(suspect, evidence_list):
    score = 0

    if suspect["clue"] in evidence_list:
        score += 5

    if suspect["clue"] == "Has scratches on hands":
        score += 3
    elif suspect["clue"] == "Was nervous during questioning":
        score += 2
    elif suspect["clue"] == "Has no alibi":
        score += 4
    elif suspect["clue"] == "Avoids eye contact":
        score += 1

    return score


# -------------------------
# CASE GENERATION
# -------------------------
def generate_case():
    case_suspects = []
    suspect_scores = []

    for i in range(4):
        suspect = {
            "name": suspects[i],
            "occupation": random.choice(occupations),
            "age": random.choice(ages),
            "personality": random.choice(personalities),
            "clue": random.choice([
                "Saw near crime scene",
                "Has scratches on hands",
                "Was nervous during questioning",
                "Has no alibi",
                "Avoids eye contact",
                "Claims innocence"
            ])
        }

        case_suspects.append(suspect)

    # initial scoring (before evidence)
    for s in case_suspects:
        suspect_scores.append(random.randint(1, 5))

    killer_index = suspect_scores.index(max(suspect_scores))

    return {
        "victim": random.choice(victims),
        "location": random.choice(locations),
        "weapon": random.choice(weapons),
        "suspects": case_suspects,
        "scores": suspect_scores,
        "killer": killer_index,
        "evidence": []
    }


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    session["case"] = generate_case()
    return render_template("index.html", case=session["case"])


# -------------------------
# INTERROGATION PAGE
# -------------------------
@app.route("/interrogate/<int:index>")
def interrogate(index):
    case = session.get("case")

    if not case:
        return redirect("/")

    suspect = case["suspects"][index]

    response = random.choice([
        f"{suspect['name']} looks nervous...",
        f"{suspect['name']} avoids eye contact...",
        f"{suspect['name']} is too calm...",
        f"{suspect['name']} hesitates before answering..."
    ])

    return render_template(
        "interrogate.html",
        suspect=suspect,
        response=response
    )


# -------------------------
# COLLECT EVIDENCE
# -------------------------
@app.route("/evidence/<int:index>")
def evidence(index):
    case = session.get("case")

    if not case:
        return redirect("/")

    suspect = case["suspects"][index]
    clue = suspect["clue"]

    if clue not in case["evidence"]:
        case["evidence"].append(clue)

    session["case"] = case

    return render_template("index.html", case=case)


# -------------------------
# ACCUSE SYSTEM
# -------------------------
@app.route("/accuse/<int:index>")
def accuse(index):
    case = session.get("case")

    if not case:
        return redirect("/")

    evidence = case.get("evidence", [])

    scores = []
    for s in case["suspects"]:
        scores.append(calculate_score(s, evidence))

    killer_index = scores.index(max(scores))

    if index == killer_index:
        result = "🎉 Correct! You solved the case!"
    else:
        result = f"❌ Wrong! The killer was {case['suspects'][killer_index]['name']}"

    return render_template("index.html", case=case, result=result)


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
   import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))