CREATE DATABASE IF NOT EXISTS project_submission_db;
USE project_submission_db;

CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    github_link VARCHAR(255) NOT NULL,
    demo_video_path VARCHAR(255)
);
