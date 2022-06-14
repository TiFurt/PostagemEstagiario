from datetime import datetime
from application.model.entity.postagem import Postagem
from application.model.dao import lista_postagens
from datetime import date

class PostagemDao:
    def __init__(self):
        pass

    def bubble_sort(self, lista):
        for i in range(len(lista)):
            for j in range(len(lista) - 1):
                if lista[j].get_data() < lista[j + 1].get_data():
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                elif lista[j].get_data() == lista[j + 1].get_data():
                    if lista[j].get_hora() < lista[j + 1].get_hora():
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def listar_postagens(self):
        return lista_postagens

    def listar_postagens_ordenadas(self):
        return self.bubble_sort(lista_postagens)

    def buscar_postagem(self, id):
        for postagem in lista_postagens:
            if postagem.get_id() == id:
                return postagem
        return None

    def salvar_postagem(self, autor, titulo, texto):
        id = len(lista_postagens) + 1
        today_date = datetime.today().strftime('%d/%m/%Y')
        hour_date = datetime.today().strftime('%H:%M:%S')
        lista_postagens.append(Postagem(id, autor, titulo, texto, today_date, hour_date))

    def add_like(self, id):
        for postagem in lista_postagens:
            if postagem.get_id() == id:
                postagem.add_like()
                return
