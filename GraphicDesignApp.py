# Tema: Desarrollo de un software de fácil uso e interactivo sobre DISEÑO GRÁFICO

# Descripción breve:
# El software se enfocará en diseño gráfico accesible para principiantes, utilizando interfaces afectivas
# y elementos de experiencia de usuario intuitivos. Permitirá crear ilustraciones simples
# mediante herramientas amigables como paletas de colores, formas prediseñadas y ajustes
# visuales interactivos.

# Propuesta inicial de código para la interfaz del software
import tkinter as tk
from tkinter import colorchooser, filedialog

class GraphicDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseño Gráfico Interactivo")
        self.root.geometry("800x600")

        # Paleta de colores
        self.color = "#000000"  # Color inicial: negro

        # Tamaño del liezo
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(pady=20)
        
        # Crear botones de interacción
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack()

        self.color_button = tk.Button(self.controls_frame, text="Seleccionar Color", command=self.choose_color)
        self.color_button.grid(row=0, column=0, padx=10)

        self.save_button = tk.Button(self.controls_frame, text="Guardar Diseño", command=self.save_design)
        self.save_button.grid(row=0, column=1, padx=10)

        self.clear_button = tk.Button(self.controls_frame, text="Limpiar Lienzo", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=2, padx=10)

        # Habilitar dibujo
        self.canvas.bind("<B1-Motion>", self.draw)

    def choose_color(self):
        """Abrir selector de color"""
        color_code = colorchooser.askcolor(title="Elige un color")[1]
        if color_code:
            self.color = color_code

    def draw(self, event):
        """Dibujar en el lienzo con el color seleccionado"""
        x, y = event.x, event.y
        size = 5  # Tamaño del pincel
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=self.color, outline=self.color)

    def save_design(self):
        """Guardar el trabajo como imagen"""
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.canvas.postscript(file=file_path + ".eps")  # Guardar como postscript para convertir a imagen
            print(f"Diseño guardado en: {file_path}")

    def clear_canvas(self):
        """Limpiar el lienzo"""
        self.canvas.delete("all")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicDesignApp(root)
    root.mainloop()
