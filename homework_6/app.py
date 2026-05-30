from flask import Flask, render_template, request, redirect, url_for
import json
import os


app = Flask(__name__)
JSON_FILE = "workouts.json"


def load_json():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_json(data):
    with open(JSON_FILE, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
        
def day_exists(day, data):
    return any(w["day"] == day for w in data)
    
    
@app.route('/', methods=['GET', 'POST'])
def create_workout_day():
    data = load_json()
    if request.method == 'POST':
        day = request.form['day'].strip()
        
        if not day:
            return redirect(url_for('create_workout_day'))
        
        new_workout = {
            "day": day,
            "exercises": []
        }
        if not day_exists(day, data):
            data.append(new_workout)
            save_json(data)
        return redirect(url_for('create_workout_day'))
    
    return render_template('index.html', workouts=data)


@app.route('/workout/<day>', methods=['GET', 'POST'])
def add_exercise(day):
    data = load_json()
    current_workout = None
    for workout in data:
        if workout['day'] == day:
            current_workout = workout
            break
    
    if current_workout is None:
        return "Workout not found", 404
    
    if request.method == 'POST':
        exercise = request.form['exercise'].strip()
        
        if not exercise:
            return redirect(url_for('add_exercise', day=day))
        
        reps = request.form['reps'].strip()
        if not reps.isdigit() or int(reps) < 0:
            return redirect(url_for('add_exercise', day=day))
        
        new_exercise = {
            "name": exercise,
            "reps": reps,
            "done": False
        }
        for e in current_workout["exercises"]:
            if e['name'] == exercise:
                return redirect(url_for('add_exercise', day=day))
        current_workout['exercises'].append(new_exercise)
        save_json(data)
        return redirect(url_for('add_exercise', day=day))
    
    return render_template('workout.html', workout=current_workout)


@app.route('/workout/<day>/toggle/<exercise_name>', methods=['POST'])
def toggle_exercise(day, exercise_name):
    data = load_json()
    current_workout = None
    for workout in data:
        if workout['day'] == day:
            current_workout = workout
            break
    if current_workout is None:
        return "Workout not found", 404

    changed = False
    for exercise in current_workout['exercises']:
        if exercise['name'] == exercise_name:
            exercise['done'] = not exercise['done']
            changed = True 
            break

    if changed:
        save_json(data)

    return redirect(url_for('add_exercise', day=day))


@app.route('/workout/<day>/reset', methods=['POST'])
def reset_workout(day):
    data = load_json()
    current_workout = None
    for workout in data:
        if workout['day'] == day:
            current_workout = workout
            break

    
    if current_workout is None:
        return "Workout not found", 404

    for exercise in current_workout['exercises']:
        exercise['done'] = False
    save_json(data)
    return redirect(url_for('add_exercise', day=day))


if __name__ == '__main__':
    app.run(debug=True)