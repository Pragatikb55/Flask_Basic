"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample tasks data
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'description': 'Complete Flask tutorial', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'description': 'Create a personal to-do list application', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'description': 'Upload project to GitHub repository', 'status': 'Pending', 'priority': 'Low'},
    {'id': 4, 'title': 'Personal Website', 'description': 'Design and build a personal website', 'status': 'Pending', 'priority': 'Medium'}
]

# Home page - display all tasks
@app.route('/')
def index():
    # Calculate statistics for the dashboard
    total_tasks = len(TASKS)
    completed_tasks = len([task for task in TASKS if task['status'] == 'Completed'])
    in_progress_tasks = len([task for task in TASKS if task['status'] == 'In Progress'])
    pending_tasks = len([task for task in TASKS if task['status'] == 'Pending'])
    
    return render_template('index.html', 
                         tasks=TASKS, 
                         total_tasks=total_tasks,
                         completed_tasks=completed_tasks,
                         in_progress_tasks=in_progress_tasks,
                         pending_tasks=pending_tasks)

# Page with a form to add new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status')
        priority = request.form.get('priority')
        due_date = request.form.get('due_date')
        
        # Create new task with next available ID
        new_id = max([task['id'] for task in TASKS]) + 1 if TASKS else 1
        new_task = {
            'id': new_id,
            'title': title,
            'description': description,
            'status': status,
            'priority': priority,
            'due_date': due_date
        }
        
        # Add to tasks list
        TASKS.append(new_task)
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

# View single task details
@app.route('/task/<int:id>')
def view_task(id):
    # Find task with the given ID
    task = next((task for task in TASKS if task['id'] == id), None)
    
    if task is None:
        return "Task not found", 404
    
    return render_template('task.html', task=task)

# About the app page
@app.route('/about')
def about():
    return render_template('about.html')

# Bonus: Filter tasks by priority
@app.route('/priority/<name>')
def filter_by_priority(name):
    # Filter tasks by priority
    filtered_tasks = [task for task in TASKS if task['priority'].lower() == name.lower()]
    
    # Calculate statistics for filtered tasks
    total_filtered = len(filtered_tasks)
    completed_filtered = len([task for task in filtered_tasks if task['status'] == 'Completed'])
    in_progress_filtered = len([task for task in filtered_tasks if task['status'] == 'In Progress'])
    pending_filtered = len([task for task in filtered_tasks if task['status'] == 'Pending'])
    
    return render_template('index.html', 
                         tasks=filtered_tasks, 
                         total_tasks=total_filtered,
                         completed_tasks=completed_filtered,
                         in_progress_tasks=in_progress_filtered,
                         pending_tasks=pending_filtered,
                         filter_by=f"Priority: {name}")

# Bonus: Filter tasks by status
@app.route('/status/<name>')
def filter_by_status(name):
    # Filter tasks by status
    status_name = name.replace('-', ' ').title()
    filtered_tasks = [task for task in TASKS if task['status'].lower() == status_name.lower()]
    
    # Calculate statistics for filtered tasks
    total_filtered = len(filtered_tasks)
    
    return render_template('index.html', 
                         tasks=filtered_tasks, 
                         total_tasks=total_filtered,
                         completed_tasks=0,
                         in_progress_tasks=0,
                         pending_tasks=0,
                         filter_by=f"Status: {status_name}")

if __name__ == '__main__':
    app.run(debug=True)