from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = mysql.connector.connect(
    host=app.config['DB_HOST'],
    user=app.config['DB_USER'],
    password=app.config['DB_PASSWORD'],
    database=app.config['DB_NAME']
)
cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    return render_template('home.html', projects=projects)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        description = request.form['description']
        github_link = request.form['github_link']
        
        demo_video = request.files['demo_video']
        if demo_video:
            filename = secure_filename(demo_video.filename)
            demo_video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            demo_video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            demo_video_path = None
        
        cursor.execute(
            "INSERT INTO projects (name, title, description, github_link, demo_video_path) VALUES (%s, %s, %s, %s, %s)",
            (name, title, description, github_link, demo_video_path)
        )
        db.commit()
        
        return redirect(url_for('home'))
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
