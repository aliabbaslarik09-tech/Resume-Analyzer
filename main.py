# ===== AI Resume Feedback Program (Auto Path Version) =====

import os

def rate_resume(resume_text):
    score = 0
    feedback = []

    resume_text = resume_text.lower()

    # 1️⃣ Check for important sections
    sections = ["education", "experience", "skills", "projects"]
    for section in sections:
        if section in resume_text:
            score += 10
        else:
            feedback.append(f"Missing section: {section.title()}")

    # 2️⃣ Check for technical skills
    skills = ["python", "java", "c++", "html", "css", "javascript", "sql", "machine learning", "ai"]
    skill_count = sum(1 for skill in skills if skill in resume_text)
    score += min(skill_count * 5, 25)

    if skill_count < 3:
        feedback.append("Add more technical skills.")

    # 3️⃣ Check for action words
    action_words = ["developed", "designed", "built", "implemented", "led", "created"]
    action_count = sum(1 for word in action_words if word in resume_text)
    score += min(action_count * 3, 15)

    if action_count < 2:
        feedback.append("Use more action verbs to describe your work.")

    # 4️⃣ Check resume length
    word_count = len(resume_text.split())
    if 150 <= word_count <= 400:
        score += 20
    else:
        feedback.append("Resume length should be between 150–400 words.")

    # Final score cap
    score = min(score, 100)

    return score, feedback


# ===== MAIN PROGRAM =====
print("=== AI Resume Feedback Program ===\n")

# Get the folder where this script is located
script_folder = os.path.dirname(os.path.abspath(__file__))
resume_path = os.path.join(script_folder, "resume.txt")

# Read resume from file
try:
    with open(resume_path, "r", encoding="utf-8") as file:
        resume = file.read()
except FileNotFoundError:
    print(f"Error: 'resume.txt' not found in {script_folder}")
    exit()

score, feedback = rate_resume(resume)

print("\n--- Resume Analysis ---")
print(f"Score: {score}/100")

if feedback:
    print("\nSuggestions:")
    for f in feedback:
        print("- " + f)
else:
    print("\nExcellent resume! No major issues found.")
