class Postagem:
    def __init__(self, id, autor, titulo, texto, data, hora):
        self.__id = id
        self.__titulo = titulo
        self.__texto = texto
        self.__data = data
        self.__autor = autor
        self.__hora = hora
        self.__likes = 0

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_texto(self):
        return self.__texto

    def get_data(self):
        return self.__data

    def get_hora(self):
        return self.__hora

    def get_autor(self):
        return self.__autor

    def get_likes(self):
        return self.__likes

    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_texto(self, texto):
        self.__texto = texto

    def set_data(self, data):
        self.__data = data

    def set_autor(self, autor):
        self.__autor = autor

    def add_like(self):
        self.__likes += 1
