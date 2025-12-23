import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')
        
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg='#1e1e1e')
        display_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Result display
        display_font = font.Font(family='Arial', size=32, weight='bold')
        display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=display_font,
            bg='#2d2d2d',
            fg='#ffffff',
            anchor='e',
            padx=20,
            pady=20
        )
        display.pack(expand=True, fill='both')
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg='#1e1e1e')
        buttons_frame.pack(expand=True, fill='both', padx=10, pady=(0, 10))
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        button_font = font.Font(family='Arial', size=18, weight='bold')
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                bg_color = '#4a4a4a'  # Default gray
                fg_color = '#ffffff'
                
                if button_text in ['/', '*', '-', '+', '=']:
                    bg_color = '#ff9500'  # Orange for operators
                elif button_text in ['C', '⌫', '%', '±']:
                    bg_color = '#505050'  # Dark gray for functions
                
                btn = tk.Button(
                    buttons_frame,
                    text=button_text,
                    font=button_font,
                    bg=bg_color,
                    fg=fg_color,
                    activebackground='#666666',
                    activeforeground='#ffffff',
                    border=0,
                    command=lambda x=button_text: self.on_button_click(x)
                )
                btn.grid(row=i, column=j, sticky='nsew', padx=3, pady=3)
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("0")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression if self.expression else "0")
        elif char == '%':
            # Yüzde hesaplama mantığı:
            # Kullanıcı "200*17" yazıp "%" ye bastığında, bunu (200*17)/100 olarak hesaplar.
            if self.expression:
                try:
                    # Mevcut ifadeyi 100'e bölecek stringi oluşturuyoruz
                    temp_expression = self.expression + "/100"
                    
                    # Hesaplamayı yapıyoruz
                    result = eval(temp_expression)
                    
                    # Sonucu ekrana yazdırıyoruz
                    self.result_var.set(str(result))
                    self.expression = str(result)
                except:
                    self.result_var.set("Error")
                    self.expression = ""
        elif char == '=':
            try:
                result = eval(self.expression)
                self.result_var.set(str(result))
                self.expression = str(result)
            except:
                self.result_var.set("Error")
                self.expression = ""
        elif char == '±':
            if self.expression:
                try:
                    result = eval(self.expression)
                    result = -result
                    self.result_var.set(str(result))
                    self.expression = str(result)
                except:
                    pass
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()