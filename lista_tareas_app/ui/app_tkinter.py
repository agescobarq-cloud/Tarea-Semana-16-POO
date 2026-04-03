import tkinter as tk
from tkinter import ttk, messagebox
from servicios.tarea_servicio import TareaServicio
from modelos.tarea import Tarea

class AppTkinter:
    def __init__(self, servicio: TareaServicio):
        self.servicio = servicio
        self.root = tk.Tk()
        self.root.title("Lista de Tareas - Semana 16 (Atajos de Teclado)")
        self.root.geometry("650x550")
        self.root.configure(bg="#f0f0f0")

        # Campo de entrada
        tk.Label(self.root, text="Nueva tarea:", bg="#f0f0f0", font=("Arial", 11)).pack(anchor="w", padx=20, pady=(20, 5))
        self.entry = tk.Entry(self.root, font=("Arial", 12), width=60)
        self.entry.pack(padx=20, pady=5, fill=tk.X)
        self.entry.bind("<Return>", lambda e: self.agregar_tarea())   # Enter para agregar

        # Botones (se mantienen por si el usuario prefiere usar mouse)
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea,
                  bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Marcar Completada (C)", command=self.marcar_completada,
                  bg="#2196F3", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar (Delete/D)", command=self.eliminar_tarea,
                  bg="#f44336", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Salir (Esc)", command=self.root.quit,
                  bg="#9E9E9E", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.tree = ttk.Treeview(self.root, columns=("ID", "Descripcion"), show="headings", height=18)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Descripcion", width=550)
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Estilos visuales
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11))
        self.tree.tag_configure("completada", foreground="gray", font=("Arial", 11, "overstrike"))

        # Atajos de teclado globales (recomendado: bind al root)
        self.root.bind("<c>", lambda e: self.marcar_completada())      # Tecla C
        self.root.bind("<C>", lambda e: self.marcar_completada())      # Tecla Shift+C (por si está en mayúsculas)
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())    # Tecla Delete
        self.root.bind("<d>", lambda e: self.eliminar_tarea())         # Tecla D
        self.root.bind("<D>", lambda e: self.eliminar_tarea())         # Tecla Shift+D
        self.root.bind("<Escape>", lambda e: self.root.quit())         # Tecla Escape → Cerrar

        # Doble clic (se mantiene de la versión anterior)
        self.tree.bind("<Double-1>", lambda e: self.marcar_completada())

        self.actualizar_lista()

    def agregar_tarea(self):
        desc = self.entry.get().strip()
        if not desc:
            messagebox.showwarning("Atención", "Escribe una descripción para la tarea")
            return
        self.servicio.agregar_tarea(desc)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()
        self.entry.focus()   # Volver el foco al Entry

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una tarea (usa flechas o clic)")
            return
        item = self.tree.item(seleccion[0])
        tarea_id = int(item["values"][0])
        if self.servicio.completar_tarea(tarea_id):
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar")
            return
        item = self.tree.item(seleccion[0])
        tarea_id = int(item["values"][0])
        if self.servicio.eliminar_tarea(tarea_id):
            self.actualizar_lista()

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tarea in self.servicio.listar_tareas():
            desc = f"{tarea.descripcion} [Hecho]" if tarea.completado else tarea.descripcion
            tag = "completada" if tarea.completado else "normal"
            self.tree.insert("", tk.END, values=(tarea.id, desc), tags=(tag,))

    def ejecutar(self):
        self.root.mainloop()