import tkinter as tk
import requests
from PIL import ImageTk, Image
import io
import random

MAX_WIDTH = 500

class interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        root.configure(bg="white")
        root.iconbitmap(r'C:\Users\carlo\Documents\PROJETOS\Filminho/icone.ico')
        self.root.title("Gerador de comida e filmes aleatórias <3")

        bg_image = Image.open(r'C:\Users\carlo\Documents\PROJETOS\Filminho/fundo 4.jpg')
        bg_image = bg_image.resize((1820, 980), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.max_image_size = (400, 400)

        self.api_key = '691ca66c76648902b2d4bc34a1abdc3f'

        #cria um botão para gerar a comida
        self.button1 = tk.Button(self.root, text="Gerar Comida", bg= "#C71585", fg= "white", width=15, height=2, font=("Arial", 20, "bold"), activebackground="#FFB6C1", border= 15, foreground='white', activeforeground='white', relief= 'ridge', command=self.get_random_comida)
        self.button1.pack(side= "right", padx=(0,0), pady= (0,0), expand=False)
        self.button1.place(x=1100, y=100)

        #cria um botão para gerar o filme
        self.button2 = tk.Button(self.root, text="Gerar Filme", bg= "#C71585", fg= "white", width=15, height=2, font=("Arial", 20, "bold"), activebackground="#FFB6C1", border= 15, foreground='white', activeforeground='white', relief= 'ridge', command=self.get_random_filme)
        self.button2.pack(side= "left", padx=(0,0), pady= (0,0), expand=False)
        self.button2.place(x=130, y=100)


        self.lbl_meal_filme = tk.Label(self.root, text="", font=("Arial", 15, "bold"), bg ="white")
        self.lbl_meal_filme.pack(side= "left", expand=False)
        self.lbl_meal_filme.place(x=130, y= 220)

        self.lbl_meal_comida = tk.Label(self.root, text="", font=("Arial", 15, "bold"), bg ="white")
        self.lbl_meal_comida.pack(side= "right", expand=False)
        self.lbl_meal_comida.place(x=1100 ,y=220)

        self.lbl_meal_image = tk.Label(self.root)
        self.lbl_meal_image.pack(side= "right", expand=False)
        self.lbl_meal_image.place(x=1050, y=300)

        self.lbl_meal_image_filme = tk.Label(self.root)
        self.lbl_meal_image_filme.pack(side= "left", expand=False)
        self.lbl_meal_image_filme.place(x=130 ,y=300)
        

    def get_random_comida(self):
        response = requests.get("https://api.spoonacular.com/recipes/random?apiKey=a1c8556f2a0a46b5b70d3604bf782a03")

        food_name = response.json()["recipes"][0]["title"]
        image_url = response.json()["recipes"][0]["image"]

        self.lbl_meal_comida.config(text=food_name)

        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail(self.max_image_size)
        photo = ImageTk.PhotoImage(image)
        self.lbl_meal_image.configure(image=photo)
        self.lbl_meal_image.image = photo

    def get_random_filme(self):
        response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={self.api_key}&language=en-US&page=1")

        data = response.json()
        if data.get("results"):
            movie = random.choice(data["results"])  # Seleciona um filme aleatório
            title = movie["title"]
            poster_path = movie.get("poster_path", None)
            
            if poster_path is None:
                print("Cartaz não encontrado.")
                return

            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            response = requests.get(poster_url)

            max_size = (400, 400)  # Define o tamanho máximo da imagem
            poster_image = Image.open(io.BytesIO(response.content))
            poster_image.thumbnail(max_size, Image.LANCZOS)  # Redimensiona a imagem para o tamanho máximo definido

            self.lbl_meal_filme.config(text=title)
            poster_photo = ImageTk.PhotoImage(poster_image)
            self.lbl_meal_image_filme.config(image=poster_photo)
            self.lbl_meal_image_filme.image = poster_photo

        else:
            print("Nenhum filme encontrado!")


root = tk.Tk()
interface(root)
root.mainloop()