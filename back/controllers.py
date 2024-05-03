from app import app
from flask import jsonify, request , render_template, redirect, url_for
from db import Weapom,Armour,Trinket,Account,Build, SyntaxException ,NotFoundException, ItemAlreadyExistException,DBConnectionFail


@app.get("/")
def home():
    return "HOME"

##-------------------------------------------------EXCEPTIONS
@app.errorhandler(ItemAlreadyExistException)
def syntax_exception(error):
    return 'Nome já cadastrado, tente novamente.', 409

@app.errorhandler(SyntaxException)
def syntax_exception(error):
    return 'Dados incorretos, tente novamente.', 400

@app.errorhandler(NotFoundException)
def syntax_exception(error):
    return 'Usuário não encontrado.', 404

@app.errorhandler(DBConnectionFail)
def syntax_exception(error):
    return 'Falha ao acessar dados, tente mais tarde.', 500





## CRUD -------------------------------------------- ACCOUNTS
#READ
@app.get("/account")
def account_getAll():
    data = Account().getAll()
    return render_template("account.html", data=data)

#CREATE
@app.post("/account")
def new_account():
    Account().new(request.json)
    return "Conta cadastrada com Sucesso.", 200

#DELETE
@app.delete("/account/<int:id>")
def del_account(id):
    Account().drop(id)
    return "Usuario deletado."

#UPDATE
@app.put("/account")
def update_account():
    Account().full_update(request.json)
    return "Dados Alterados com Sucesso.", 200

## CRUD -------------------------------------------- BUILDS
#READ
@app.get("/build")
def build_getAll():
    builds = Build().get_all()
    itens = {
        "helmet":Armour().getByProp("helmet"),
        "body":Armour().getByProp("body"),
        "gloves":Armour().getByProp("gloves"),
        "boots":Armour().getByProp("boots"),
        "main_hand":Weapom().getAll(),
        "off_hand":Weapom().getAll(),
        "amulet":Trinket().getByProp("amulet"),
        "ring":Trinket().getByProp("ring"),
        "belt":Trinket().getByProp("belt")
             }
    return render_template("build.html", builds = builds, itens = itens)

@app.get("/build_api")
def build_getApi():
    build = Build().get_all()
    return jsonify(build)

@app.route("/build_api/<int:id>", methods=["GET"])
def build_getApi_Id(id):
    build= Build().get_byID(id)
    return jsonify(build)

@app.delete("/build/<int:id>")
def delete_build(id):
    Build().drop(id)
    return "Build deletada.", 200

@app.post("/build")
def new_build():
    Build().new(request.json)
    return "Build cadastrada.", 200

@app.put("/build")
def update_build():
    Build().full_update(request.json)
    return "Build alterada.", 200