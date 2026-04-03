# Tarea-Semana-16-POO
📋 Lista de Tareas con Atajos de Teclado  
**Semana 16 – Mejora del Sistema (Semana 15)**
## 🎯 Objetivo

Desarrollar una **nueva versión** de la aplicación GUI "Lista de Tareas" utilizando **Tkinter**, incorporando **atajos de teclado** para mejorar la interacción del usuario, manteniendo estrictamente la **arquitectura modular por capas** (Modelo, Servicio y UI) de la versión anterior.

## ✨ Características Principales

- ✅ Agregar tareas con el botón o presionando **Enter**
- ✅ Marcar tareas como completadas con el botón o la tecla **C**
- ✅ Eliminar tareas con el botón, la tecla **Delete** o **D**
- ✅ Cerrar la aplicación con la tecla **Escape**
- ✅ Doble clic sobre una tarea para marcarla como completada
- ✅ Feedback visual claro: tareas completadas aparecen en **gris y tachadas**
- ✅ Interfaz limpia y responsive con `ttk.Treeview`
- ✅ Soporte completo para mouse y teclado
- ✅ Arquitectura modular respetada (sin mezclar lógica de negocio con la interfaz)

## 🏗️ Estructura del Proyecto
lista_tareas_app/
├── main.py                  # Punto de entrada y orquestador
├── modelos/
│   └── tarea.py             # Clase Tarea (Modelo de datos)
├── servicios/
│   └── tarea_servicio.py    # Lógica de negocio (Servicio)
└── ui/
└── app_tkinter.py       # Interfaz gráfica + manejo de eventos y atajos de teclado
