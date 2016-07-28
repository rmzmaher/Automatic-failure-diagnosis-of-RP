import Tkinter as tk
from kin_predict import NeuralNetwork
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('360x150')
        self.title('Downhole Diagonsis of RP')
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text=" Run!", command=self.on_button)
        self.entry.place(x=100,y=50)
        self.button.place(x=130,y=100)

    def on_button(self):
        nn = NeuralNetwork()
        nn.predict(self.entry.get())


app = App()
app.mainloop()