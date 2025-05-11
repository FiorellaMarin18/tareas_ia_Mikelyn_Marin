from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

# --- Funciones auxiliares ---

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# --- Rutas del frontend ---

@app.route('/')
def index():
    return render_template('index.html')

# --- API REST ---

@app.route('/api/tareas', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/api/tareas', methods=['POST'])
def create_task():
    data = request.json
    if not data or 'titulo' not in data:
        return jsonify({'error': 'Falta título'}), 400
    tasks = load_tasks()
    new_task = {
        'id': get_next_id(tasks),
        'titulo': data['titulo'],
        'descripcion': data.get('descripcion', ''),
        'estado': 'pendiente',
        'fecha_vencimiento': data.get('fecha_vencimiento', '')
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/api/tareas/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update({
                'titulo': data.get('titulo', task['titulo']),
                'descripcion': data.get('descripcion', task['descripcion']),
                'estado': data.get('estado', task['estado']),
                'fecha_vencimiento': data.get('fecha_vencimiento', task['fecha_vencimiento']),
            })
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Tarea no encontrada'}), 404

@app.route('/api/tareas/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        return jsonify({'error': 'Tarea no encontrada'}), 404
    save_tasks(new_tasks)
    return jsonify({'mensaje': 'Tarea eliminada'}), 200

# --- Ejecutar app ---

if __name__ == '__main__':
    app.run(debug=True)
