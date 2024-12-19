import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Lista para almacenar las tareas con detalles
tasks = []


# Funciones para manejar las tareas
def is_valid_date(date_str):
    """Valida que la fecha esté en formato YYYY-MM-DD"""
    if len(date_str) != 10:
        return False
    parts = date_str.split("-")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return False
    year, month, day = map(int, parts)
    return 1 <= month <= 12 and 1 <= day <= 31


def is_valid_time(time_str):
    """Valida que la hora esté en formato HH:MM"""
    if len(time_str) != 5:
        return False
    parts = time_str.split(":")
    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        return False
    hour, minute = map(int, parts)
    return 0 <= hour < 24 and 0 <= minute < 60


def add_task():
    task = entry_task.get()
    state = combo_state.get()
    deadline_date = entry_date.get()
    deadline_time = entry_time.get()

    if not task or not state or not deadline_date or not deadline_time:
        messagebox.showwarning(
            "Entrada incompleta", "Por favor, completa todos los campos."
        )
        return

    if not is_valid_date(deadline_date):
        messagebox.showerror(
            "Fecha inválida",
            "Por favor, ingresa una fecha válida en formato YYYY-MM-DD.",
        )
        return

    if not is_valid_time(deadline_time):
        messagebox.showerror(
            "Hora inválida", "Por favor, ingresa una hora válida en formato HH:MM."
        )
        return

    # Agregar la tarea si todos los campos son válidos
    tasks.append(
        {"task": task, "state": state, "deadline": f"{deadline_date} {deadline_time}"}
    )
    update_task_list()
    update_progress_bar()
    entry_task.delete(0, tk.END)
    combo_state.set("No iniciada")
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    messagebox.showinfo("Tarea agregada", f"Tarea '{task}' agregada con éxito.")


def remove_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task = tasks.pop(selected_task_index[0])
        update_task_list()
        update_progress_bar()
        messagebox.showinfo(
            "Tarea eliminada", f"Tarea '{task['task']}' eliminada con éxito."
        )
    else:
        messagebox.showwarning(
            "Selección vacía", "Por favor, selecciona una tarea para eliminar."
        )


def remove_completed_tasks():
    global tasks
    tasks = [task for task in tasks if task["state"] != "Completada"]
    update_task_list()
    update_progress_bar()
    messagebox.showinfo(
        "Tareas completadas eliminadas",
        "Todas las tareas completadas han sido eliminadas.",
    )


def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        task_display = f"{task['task']} - {task['state']} - {task['deadline']}"
        listbox_tasks.insert(tk.END, task_display)


def update_progress_bar():
    if not tasks:
        progress_bar["value"] = 0
        progress_label.config(text="Progreso: 0%")
        return

    completed_tasks = sum(1 for task in tasks if task["state"] == "Completada")
    progress = int((completed_tasks / len(tasks)) * 100)
    progress_bar["value"] = progress
    progress_label.config(text=f"Progreso: {progress}%")

    if progress == 100:
        messagebox.showinfo(
            "¡Felicidades!", "¡Has completado todas tus tareas del día!"
        )


# Temporizador Pomodoro
def start_timer():
    global timer_running
    timer_running = True
    update_timer()


def pause_timer():
    global timer_running
    timer_running = False


def reset_timer():
    global remaining_time, timer_running
    remaining_time = POMODORO_DURATION
    timer_running = False
    update_timer_label()


def update_timer():
    global remaining_time, timer_running
    if remaining_time > 0 and timer_running:
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        root.after(1000, update_timer)
    elif remaining_time == 0 and timer_running:
        timer_running = False
        messagebox.showinfo("Pomodoro completado", "¡Buen trabajo! Tómate un descanso.")
        reset_timer()


def update_timer_label():
    minutes, seconds = divmod(remaining_time, 60)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


# Configuración inicial del Pomodoro
POMODORO_DURATION = 25 * 60  # 25 minutos
remaining_time = POMODORO_DURATION
timer_running = False

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas y Temporizador Pomodoro")

# Entrada de tarea
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

label_task = tk.Label(frame_entry, text="Tarea:")
label_task.grid(row=0, column=0, padx=5, pady=5)

entry_task = tk.Entry(frame_entry, width=40)
entry_task.grid(row=0, column=1, padx=5, pady=5)

label_state = tk.Label(frame_entry, text="Estado:")
label_state.grid(row=1, column=0, padx=5, pady=5)

combo_state = ttk.Combobox(
    frame_entry, values=["No iniciada", "En progreso", "Completada"]
)
combo_state.grid(row=1, column=1, padx=5, pady=5)
combo_state.set("No iniciada")

label_date = tk.Label(frame_entry, text="Fecha (YYYY-MM-DD):")
label_date.grid(row=2, column=0, padx=5, pady=5)

entry_date = tk.Entry(frame_entry, width=20)
entry_date.grid(row=2, column=1, padx=5, pady=5)

label_time = tk.Label(frame_entry, text="Hora (HH:MM):")
label_time.grid(row=3, column=0, padx=5, pady=5)

entry_time = tk.Entry(frame_entry, width=20)
entry_time.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(frame_entry, text="Agregar Tarea", command=add_task)
button_add.grid(row=4, columnspan=2, pady=10)

# Lista de tareas
frame_list = tk.Frame(root)
frame_list.pack(pady=10)

listbox_tasks = tk.Listbox(frame_list, width=70, height=15)
listbox_tasks.pack(side=tk.LEFT, padx=5)

scrollbar_tasks = tk.Scrollbar(frame_list)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Barra de progreso
progress_bar = ttk.Progressbar(
    root, orient="horizontal", length=300, mode="determinate"
)
progress_bar.pack(pady=10)

progress_label = tk.Label(root, text="Progreso: 0%")
progress_label.pack()

# Temporizador Pomodoro
frame_pomodoro = tk.Frame(root)
frame_pomodoro.pack(pady=10)

timer_label = tk.Label(frame_pomodoro, text="25:00", font=("Helvetica", 24))
timer_label.pack()

button_start = tk.Button(frame_pomodoro, text="Iniciar", command=start_timer)
button_start.pack(side=tk.LEFT, padx=5)

button_pause = tk.Button(frame_pomodoro, text="Pausar", command=pause_timer)
button_pause.pack(side=tk.LEFT, padx=5)

button_reset = tk.Button(frame_pomodoro, text="Reiniciar", command=reset_timer)
button_reset.pack(side=tk.LEFT, padx=5)

# Botones adicionales
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_remove = tk.Button(
    frame_buttons, text="Eliminar Tarea Seleccionada", command=remove_task
)
button_remove.pack(side=tk.LEFT, padx=10)

button_remove_completed = tk.Button(
    frame_buttons, text="Eliminar Tareas Completadas", command=remove_completed_tasks
)
button_remove_completed.pack(side=tk.LEFT, padx=10)

# Iniciar la aplicación
root.mainloop()
