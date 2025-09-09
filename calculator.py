import tkinter as tk
from tkinter import font
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Hesap Makinesi")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Tema değişkenleri
        self.dark_mode = False
        self.colors = {
            "bg": "#f0f0f0",
            "display_bg": "white",
            "button_bg": "#e0e0e0",
            "button_fg": "black",
            "operator_bg": "#ff9500",
            "operator_fg": "white",
            "hover_bg": "#d0d0d0"
        }
        
        self.setup_ui()
        self.apply_theme()
        
    def setup_ui(self):
        # Ekran
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self.root, 
            textvariable=self.display_var, 
            font=('Arial', 24), 
            bd=10, 
            insertwidth=2, 
            width=14, 
            borderwidth=4, 
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")
        
        # Butonlar
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('x²', 5, 1), ('C', 5, 2), ('⚙', 5, 3)
        ]
        
        self.buttons = {}
        for (text, row, col) in buttons:
            btn = tk.Button(
                self.root, 
                text=text, 
                font=('Arial', 18), 
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.buttons[text] = btn
            
            # Hover efekti
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover(b, False))
        
        # Grid yapılandırması
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, text):
        current = self.display_var.get()
        
        if text == 'C':
            self.display_var.set('')
        elif text == '=':
            try:
                # x² ve √ için özel durum
                if '²' in current:
                    num = float(current.replace('²', ''))
                    result = num ** 2
                elif '√' in current:
                    num = float(current.replace('√', ''))
                    result = math.sqrt(num)
                else:
                    result = eval(current)
                
                self.display_var.set(str(result))
            except ZeroDivisionError:
                self.display_var.set("0'a bölünemez!")
            except Exception:
                self.display_var.set("Hata!")
        elif text in ['√', 'x²']:
            self.display_var.set(text + current)
        else:
            self.display_var.set(current + text)
    
    def on_hover(self, button, entering):
        if entering:
            button.config(bg=self.colors["hover_bg"])
        else:
            self.apply_theme_to_button(button)
    
    def apply_theme(self):
        bg = self.colors["bg"]
        self.root.config(bg=bg)
        self.display.config(bg=self.colors["display_bg"])
        
        for btn in self.buttons.values():
            self.apply_theme_to_button(btn)
    
    def apply_theme_to_button(self, button):
        text = button.cget("text")
        if text in ['+', '-', '*', '/', '=', '√', 'x²']:
            button.config(bg=self.colors["operator_bg"], fg=self.colors["operator_fg"])
        else:
            button.config(bg=self.colors["button_bg"], fg=self.colors["button_fg"])
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.colors = {
                "bg": "#2b2b2b",
                "display_bg": "#1e1e1e",
                "button_bg": "#3c3c3c",
                "button_fg": "white",
                "operator_bg": "#ff9500",
                "operator_fg": "white",
                "hover_bg": "#505050"
            }
        else:
            self.colors = {
                "bg": "#f0f0f0",
                "display_bg": "white",
                "button_bg": "#e0e0e0",
                "button_fg": "black",
                "operator_bg": "#ff9500",
                "operator_fg": "white",
                "hover_bg": "#d0d0d0"
            }
        self.apply_theme()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    
    # Tema değiştirme butonu
    theme_btn = tk.Button(
        root, 
        text="⚙", 
        font=('Arial', 18), 
        command=app.toggle_theme
    )
    theme_btn.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)
    theme_btn.bind("<Enter>", lambda e: app.on_hover(theme_btn, True))
    theme_btn.bind("<Leave>", lambda e: app.on_hover(theme_btn, False))
    
    root.mainloop()