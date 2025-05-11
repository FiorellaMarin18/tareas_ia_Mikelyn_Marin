document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('taskForm');
  const taskList = document.getElementById('taskList');

  // Crear tarea
  form.onsubmit = async (e) => {
    e.preventDefault();
    const data = {
      titulo: document.getElementById('titulo').value,
      descripcion: document.getElementById('descripcion').value,
      fecha_vencimiento: document.getElementById('fecha_vencimiento').value
    };
    await fetch('/api/tareas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    form.reset();
    fetchTasks();
  };

  // Obtener y mostrar tareas
  async function fetchTasks() {
    const res = await fetch('/api/tareas');
    const tasks = await res.json();
    taskList.innerHTML = '';
    tasks.forEach(task => {
      const li = document.createElement('li');
      li.innerHTML = `
        <strong>${task.titulo}</strong> - ${task.descripcion}
        <br>📅 Vence: ${task.fecha_vencimiento || 'No definida'} | Estado: ${task.estado}
        <br>
        <button class="done-btn" data-id="${task.id}">Marcar hecho</button>
        <button class="delete-btn" data-id="${task.id}">Eliminar</button>
      `;
      // Eventos
      li.querySelector('.done-btn').addEventListener('click', () => markDone(task.id));
      li.querySelector('.delete-btn').addEventListener('click', () => deleteTask(task.id));
      taskList.appendChild(li);
    });
  }

  // Marcar tarea como hecha
  async function markDone(id) {
    const res = await fetch('/api/tareas');
    const tasks = await res.json();
    const task = tasks.find(t => t.id === id);
    if (task) {
      await fetch(`/api/tareas/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...task, estado: 'hecho' })
      });
      fetchTasks();
    }
  }

  // Eliminar tarea
  async function deleteTask(id) {
    await fetch(`/api/tareas/${id}`, { method: 'DELETE' });
    fetchTasks();
  }

  fetchTasks();
});
