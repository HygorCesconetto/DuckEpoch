from app import app
from flask import jsonify, request
from db import Account, Build, Monster, Item
from db import SyntaxException , NotFoundException, ItemAlreadyExistException,DBConnectionFail

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


##-------------------------------------------------API
##### ACCOUNT

@app.get("/account")
def api_account_get():
    data = Account().get_all()
    return jsonify(data)

@app.post("/account")
def api_account_new():
    Account().new(request.json)
    return "Conta cadastrada com Sucesso.", 200

@app.delete("/account/<int:id>")
def api_account_drop(id):
    Account().drop(id)
    return "Usuario deletado."

@app.patch("/account")
def api_account_update():
    Account().update(request.json)
    return "Dados Alterados com Sucesso.", 200


#### BUILD

@app.get("/build")
def api_build_get():
    data = Build().get_all()
    return jsonify(data)

@app.post("/build")
def api_build_new():
    Build().new(request.json)
    return "Build cadastrada.", 200

@app.delete("/build/<int:id>")
def api_build_drop(id):
    Build().drop(id)
    return "Build deletada.", 200

@app.patch("/build")
def api_build_update():
    Build().update(request.json)
    return "Build alterada.", 200

#### Item

@app.get("/itens")
def api_item_get():
    data = Item().get_all()
    return jsonify(data)

@app.get("/itens/<category>")
def api_item_get_category(category):
    data = Item().get_by_category(category)
    return jsonify(data)

@app.get("/itens/<type>")
def api_item_get_type(type):
    data = Item().get_by_type(type)
    return jsonify(data)

@app.post("/itens")
def api_item_new():
    Item().new(request.json)
    return "Item cadastrado.", 200

@app.delete("/itens/<int:id>")
def api_item_drop(id):
    Item().drop(id)
    return "Item deletado.", 200

@app.patch("/itens")
def api_item_update():
    Item().update(request.json)
    return "Item alterado.", 200

#### Monster

@app.get("/monsters")
def api_monster_get():
    data = Monster().get_all()
    return jsonify(data)

@app.get("/monsters/<type>")
def api_monster_get_type(type):
    data = Monster().get_by_type(type)
    return jsonify(data)

@app.post("/monsters")
def api_monster_new():
    Monster().new(request.json)
    return "Monstro cadastrado.", 200

@app.delete("/monsters/<int:id>")
def api_monster_drop(id):
    Monster().drop(id)
    return "Monstro deletado.", 200

@app.patch("/monsters")
def api_monster_update():
    Monster().update(request.json)
    return "Monstro alterado.", 200