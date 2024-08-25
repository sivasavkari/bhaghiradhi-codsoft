import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#F5F5F5')  # Background changed to light gray
root.resizable(width=False, height=False)

# Entry Field
ent_field = tk.Entry(root, bg='#E0E0E0', fg='#000000', font=('Arial', 25), 
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=8, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')

class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(self.current)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(int(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Ln(self):
        try:
            self.result = False
            self.current = math.log(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_10(self):
        try:
            self.result = False
            self.current = math.log10(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_2(self):
        try:
            self.result = False
            self.current = math.log2(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**2
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**3
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.result = False
            self.current = 10**int(ent_field.get())
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.result = False
            self.current = 1 / float(ent_field.get())
            self.Entry(self.current)
        except (ValueError, ZeroDivisionError, SyntaxError):
            self.Entry('Error')

    def Abs(self):
        try:
            self.result = False
            self.current = abs(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

# Define button colors
btn_fg = "#FFFFFF"
btn_bg = "#007ACC"  # Changed button background color
highlight_bg = '#005B99'  # Changed button highlight background color

numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg=btn_fg, bg=btn_bg, width=6, height=2,
                                highlightbackground=highlight_bg, highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='nsew', padx=5, pady=5)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

btn_CE = tk.Button(root, text='CE', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg=btn_fg, bg=btn_bg,
                   highlightbackground=highlight_bg, highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='nsew', padx=5, pady=5)

btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_sqr.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                  highlightbackground=highlight_bg, highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='nsew', padx=5, pady=5)

btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                      highlightbackground=highlight_bg, highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='nsew', padx=5, pady=5)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                      highlightbackground=highlight_bg, highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='nsew', padx=5, pady=5)

btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_add.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_sub.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)

btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_mul.grid(row=4, column=3, sticky='nsew', padx=5, pady=5)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_div.grid(row=1, column=3, sticky='nsew', padx=5, pady=5)

sc_app = SC_Calculator()
root.mainloop()


