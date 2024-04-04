from app import app
from flask import jsonify, request , render_template, redirect, url_for
from db import Weapom,Armour,Trinket,Account, SyntaxException ,NotFoundException, UserAlreadyExistException


@app.get("/")
def home():
    return "HOME"

##-------------------------------------------------EXCEPTIONS
@app.errorhandler(UserAlreadyExistException)
def syntax_exception(error):
    return 'Usuário já cadastrado, tente novamente.', 409

@app.errorhandler(SyntaxException)
def syntax_exception(error):
    return 'Sintaxe incorreta, tente novamente.', 400

@app.errorhandler(NotFoundException)
def syntax_exception(error):
    return 'Não encontrado.', 404


## CRUD --------------------------------------------WEAPON
#READ
@app.get("/weapon")
def weapon_getAll():
    data=Weapom().getAll()
    return render_template("weapon_all.html",data=data)

@app.get("/weapon/<int:id>")
def weapon_getByID(id):
    data=dict(Weapom().getByID(id))
    return render_template("weapon_id.html", data = data)

@app.get("/weapon/<prop>")
def weapon_getByType(prop):
    data = Weapom().getByProp(prop)
    return render_template("weapon_prop.html", data=data)

#CREATE
@app.post("/weapon")
def new_weapon():
    Weapom().new(request.json)
    return jsonify({"message":"ok"})

#DELETE
@app.delete("/weapon/<int:id>")
def del_weapon(id):
        Weapom().drop(id)
        return ("ok",200)

#UPDATE
@app.route("/weapon", methods =["PUT","PATCH"])
def update_weapon():
    if request.method == "PUT": Weapom().full_update(request.json)
    elif request.method == "PATCH": Weapom().parcial_update(request.json)
    return "ok"


## CRUD --------------------------------------------ARMOUR
#READ
@app.get("/armour")
def armour_getAll():
    return jsonify(Armour().getAll())

@app.get("/armour/<int:id>")
def armour_getByID(id):
    return jsonify(Armour().getByID(id))

@app.get("/armour/<prop>")
def armour_getByType(prop):
    return jsonify(Armour().getByProp(prop))

#CREATE
@app.post("/armour")
def new_armour():
    Armour().new(request.json)
    return jsonify({"message":"ok"})


#DELETE
@app.delete("/armour/<int:id>")
def del_armour(id):
    Armour().drop(id)
    return "ok"

#UPDATE
@app.route("/armour", methods =["PUT","PATCH"])
def update_armour():
    if request.method == "PUT": Armour().full_update(request.json)
    elif request.method == "PATCH": Armour().parcial_update(request.json)
    return "ok"


## CRUD --------------------------------------------TRINKET
#READ
@app.get("/trinket")
def trinket_getAll():
    return jsonify(Trinket().getAll())

@app.get("/trinket/<int:id>")
def trinket_getByID(id):
    return jsonify(Trinket().getByID(id))

@app.get("/trinket/<prop>")
def trinket_getByType(prop):
    return jsonify(Trinket().getByProp(prop))

#CREATE
@app.post("/trinket")
def new_trinket():
    Trinket().new(request.json)
    return jsonify({"message":"ok"})

#DELETE
@app.delete("/trinket/<int:id>")
def del_trinket(id):
    Trinket().drop(id)
    return "ok"

#UPDATE
@app.route("/trinket", methods =["PUT","PATCH"])
def update_trinket():
    if request.method == "PUT": Trinket().full_update(request.json)
    elif request.method == "PATCH": Trinket().parcial_update(request.json)
    return "ok"


## CRUD -------------------------------------------- ACCOUNTS
#READ
@app.get("/account")
def account_getAll():
    data = Account().getAll()
    return render_template("account.html", data=data)

@app.get("/account/<int:id>")
def account_getByID(id):
    return jsonify(Account().getByID(id))

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