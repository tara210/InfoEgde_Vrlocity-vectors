from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load data from JSON files
with open('data/user_data.json') as f:
    user_data = json.load(f)

with open('data/courses.json') as f:
    courses = json.load(f)

with open('data/blog.json') as f:
    blog_posts = json.load(f)

@app.route('/')
def dashboard():
    user = user_data['user']
    progress = (user['psychometric_score'] + user['learning_assessment_score']) // 2
    recommended_courses = [course['course_name'] for course in courses]
    return render_template('dashboard.html', user=user, progress=progress, recommended_courses=recommended_courses)

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', blog_posts=blog_posts)

@app.route('/course')
def course():
    return render_template('course.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
