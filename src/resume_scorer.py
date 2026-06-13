# Skill weights

skill_weights = {
    "python": 10,
    "java": 10,
    "sql": 10,
    "machine learning": 15,
    "deep learning": 15,
    "tensorflow": 10,
    "pytorch": 10,
    "aws": 10,
    "docker": 10,
    "git": 5,
    "github": 5,
    "react": 10,
    "nodejs": 10,
}


def calculate_score(skills):
    score = 0

    for skill in skills:
        if skill in skill_weights:
            score += skill_weights[skill]

    return min(score, 100)


# Required skills for each role

role_skills = {
    "Data Science": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "tensorflow",
        "sql"
    ],

    "Java Developer": [
        "java",
        "sql",
        "git",
        "spring"
    ],

    "Web Designing": [
        "html",
        "css",
        "javascript",
        "react"
    ]
}


def get_missing_skills(role, detected_skills):

    required = role_skills.get(role, [])

    missing = []

    for skill in required:
        if skill not in detected_skills:
            missing.append(skill)

    return missing


if __name__ == "__main__":

    skills = [
        "python",
        "numpy",
        "pandas"
    ]

    score = calculate_score(skills)

    missing = get_missing_skills(
        "Data Science",
        skills
    )

    print("Score:", score)
    print("Missing Skills:", missing)