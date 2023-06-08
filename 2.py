import tkinter as tk
import requests
from PIL import ImageTk, Image

pi_key = "a1c8556f2a0a46b5b70d3604bf782a03"

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Gerador de Comidas Aleatórias")

        # Crie um botão para gerar uma nova comida aleatória
        self.btn = tk.Button(self.root, text="Gerar Comida", command=self.get_random_meal)
        self.btn.pack()

        # Crie um rótulo para exibir o nome da comida
        self.lbl_meal_name = tk.Label(self.root, text="")
        self.lbl_meal_name.pack()

        # Crie um rótulo para exibir a imagem da comida
        self.lbl_meal_image = tk.Label(self.root)
        self.lbl_meal_image.pack()

    def get_random_meal(self):
        # Faça uma solicitação GET para a API Spoonacular para obter uma comida aleatória
        response = requests.get("https://api.spoonacular.com/recipes/random?apiKey=YOUR_API_KEY")

        # Analise o JSON retornado e obtenha o nome da comida e a URL da imagem
        data = response.json()
        meal_name = data["recipes"][0]["title"]
        meal_image_url = data["recipes"][0]["image"]

        # Exiba o nome da comida no rótulo correspondente
        self.lbl_meal_name.config(text=meal_name)

        # Carregue a imagem da comida da URL usando o Pillow e exiba-a no rótulo correspondente
        meal_image_response = requests.get(meal_image_url)
        img = Image.open(BytesIO(meal_image_response.content))
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)
        self.lbl_meal_image.config(image=img)
        self.lbl_meal_image.image = img  # Armazene a referência à imagem para evitar a coleta de lixo

root = tk.Tk()
app = App(root)
root.mainloop()
