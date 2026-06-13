skills_db = [
    "python",
    "java",
    "c++",
    "javascript",
    "react",
    "nodejs",
    "mongodb",
    "mysql",
    "postgresql",
    "html",
    "css",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "tensorflow",
    "pytorch",
    "machine learning",
    "deep learning",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "data analysis",
    "power bi",
    "tableau"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))

sample_resume = """
I have experience in Python, Pandas, NumPy,
Machine Learning, TensorFlow, Git and AWS.
"""

print(extract_skills(sample_resume))