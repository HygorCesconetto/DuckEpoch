from app import app
from flask import jsonify, request
from db import Account, Build, Monster, Item
from db import SyntaxException , NotFoundException, ItemAlreadyExistException,DBConnectionFail
import random
from numpy import ceil

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

@app.get("/accounts")
def api_account_get():
    data = Account().get_all()
    return jsonify(data)

@app.post("/accounts")
def api_account_new():
    Account().new(request.json)
    return "Conta cadastrada com Sucesso.", 200

@app.delete("/accounts/<int:id>")
def api_account_drop(id):
    Account().drop(id)
    return "Usuario deletado."

@app.patch("/accounts")
def api_account_update():
    Account().update(request.json)
    return "Dados Alterados com Sucesso.", 200


#### BUILD

@app.get("/builds")
def api_build_get():
    data = Build().get_all()
    return jsonify(data)

@app.post("/builds")
def api_build_new():
    Build().new(request.json)
    return "Build cadastrada.", 200

@app.delete("/builds/<int:id>")
def api_build_drop(id):
    Build().drop(id)
    return "Build deletada.", 200

@app.patch("/builds")
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


@app.get("/dps/<int:b>/<int:m>")
def dps_calc(b,m):

    b2 = Build().get_by_id(b)
    m2 = Monster().get_by_id(m)
    build_itens=[]
    
    for key in b2.keys():
        if key not in ["id","id_account","name"]:
            item_dict = Item().get_by_id(b2[key])
            item_dict.pop("id")
            item_dict.pop("name")
            item_dict.pop("type")
            item_dict.pop("category")
            item_dict.pop("def")
            item_dict.pop("hp")
            build_itens.append(item_dict)
    ###
    stats={'atk':0,'atks':0,'crit_chance':0,'crit_mult':0}
    for item in build_itens:
        for status in item.keys():
            stats[status]+=item[status]
        stats["atks"]= round(stats["atks"],2)
    stats["crit_chance"]=stats["crit_chance"]/1000
    stats["crit_mult"]/=100

    dps=0
    for _ in range(1000000):
        if random.random() <= stats["crit_chance"]: dps+= stats["atk"]*stats["crit_mult"]
        else: dps+=stats["atk"]
    dps/=1000000
    dps*=stats["atks"]
    
    dps_on_monster= dps*m2["def"]/1000
    time_tokill= ceil(m2["hp"]/dps_on_monster)
    res = {"build_id":b,"monster_id":m,"raw_dps":int(dps),"dps_on_monster":int(dps_on_monster),"time_to_kill":int(time_tokill)}
    return jsonify(res)
