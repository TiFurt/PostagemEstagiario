from flask import render_template, redirect, url_for, request
from application import app
from application.model.dao.postagem_dao import PostagemDao


@app.route("/")
def timeline():
    return render_template("timeline.html", postagens=PostagemDao().listar_postagens_ordenadas())


@app.route("/salvar/postagem", methods=['POST', 'GET'])
def salvar_postagem():
    autor = request.form.get('autor', 'none')
    titulo = request.form.get('titulo', 'none')
    texto = request.form.get('texto', 'none')
    PostagemDao().salvar_postagem(autor, titulo, texto)
    return redirect(url_for("timeline"))


@app.route("/like/<int:id>", methods=['POST', 'GET'])
def like(id):
    PostagemDao().add_like(id)
    return redirect(url_for("timeline"))
