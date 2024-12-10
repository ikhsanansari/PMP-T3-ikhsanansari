from flask import Blueprint, render_template

main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/")
def home():
    return render_template("home.html")


@main_routes.route("/masak")
def masak():
    return render_template("masak.html", image="images/masak.jpg", title="Masak")

@main_routes.route("/agama")
def agama():
    return render_template("agama.html", image="images/agama.jpg", title="Agama")

@main_routes.route("/olahraga")
def olahraga():
    return render_template("olahraga.html", image="images/olahraga.jpg", title="Olahraga")

@main_routes.route("/sosial")
def sosial():
    return render_template("sosial.html", image="images/sosial.jpg", title="Sosial")

@main_routes.route("/budaya")
def budaya():
    return render_template("b.html", image="images/budaya.jpg", title="Budaya")
