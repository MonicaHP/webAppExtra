import json

class peliculas:
    dataPeliculas = []

    def readPeliculas(self):
        with open('data/peliculas.json','r') as file:
            dataPeliculas = json.load(file)
            self.dataPeliculas = dataPeliculas['results']
            
    def getPelicula(self):
        peliculas = []
        for row in self.dataPeliculas:
            pelicula = row['titulo']
            if pelicula not in peliculas:
                peliculas.append(pelicula)
        return peliculas