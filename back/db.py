import mysql.connector as con

class SyntaxException(Exception):pass
class NotFoundException(Exception):pass
class UserAlreadyExistException(Exception):pass
class DBConnectionFail(Exception):pass


class DBCon ():
	def up ():
		try:
			return con.connect(user="root",password="2591439",database="dedb")
		except: return DBConnectionFail	

#---------------------------------------------------------------------------------------------ACCOUNT
class Account():
	def get_all(self):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			query="""SELECT id,usuario,email FROM account;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		except: raise DBConnectionFail

	def get_by_id(self, id:int):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT id,email,senha FROM account where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException: raise NotFoundException

	def new(self, data:dict):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT `usuario` FROM account where `usuario` = "{data["usuario"]}";""")
			result = crs.fetchone()
			crs.close()
			if result != None : raise UserAlreadyExistException

			db = DBCon.up()	
			crs = db.cursor()
			query="""INSERT INTO account(`usuario`, `email`, `senha`) VALUES('%s','%s','%s');""" %(data["usuario"], data["email"], data["senha"])
			crs.execute(query)
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail	
		except UserAlreadyExistException: raise UserAlreadyExistException
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			Account().get_by_id(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM account WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		
	def update(self, data:dict):
		try:
			Account().get_by_id(data["id"])
			if len(data) != 4: raise SyntaxError

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(f"""UPDATE account SET 
			   `usuario`= '{data["usuario"]}', 
			   `email`= '{data["email"]}', 
			   `senha`= '{data["senha"]}'
			   WHERE `id` = {data["id"]};""")
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 





#---------------------------------------------------------------------------------------------BUILD
class Build():
	def get_all(self):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM build;"""
			crs.execute(query)
			result = crs.fetchall()
			crs.close()
			return result
		
		except DBConnectionFail: raise DBConnectionFail
		except: raise SyntaxException

	def get_by_id(self,id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM build WHERE `id`=%s ;""" %id
			crs.execute(query)
			result = crs.fetchone()
			crs.close()

			if result == None: raise NotFoundException
			return result
		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException : raise NotFoundException

	def new(self, data:dict):
		try:
			db = DBCon.up()	
			crs = db.cursor()
			keys,values = kv_query(data)
			query = f"""insert into build({keys}) values({values});"""
			
			crs.execute(query)
			db.commit()
			crs.close()
		except DBConnectionFail: raise DBConnectionFail
		except Exception:raise SyntaxException

	def drop(self, id:int):
		try:
			Build().get_by_id(id)

			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM build WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException : raise NotFoundException

	def update(self, data:dict):
		try:
			Build().get_by_id(data["id"])
			if len(data) != 12: raise SyntaxError
			db = DBCon.up()
			crs = db.cursor()
			query = f"""UPDATE build SET 
				`id_account`= {data["id_account"]},
				`name`= '{data["name"]}', 
				`helmet`= {data["helmet"]}, 
				`body`= {data["body"]},
				`gloves`= {data["gloves"]},
				`boots`= {data["boots"]},
				`main_hand`= {data["main_hand"]},
				`off_hand`= {data["off_hand"]},
				`amulet`= {data["amulet"]},
				`ring`= {data["ring"]},
				`belt`= {data["belt"]}
				WHERE `id` = {data["id"]};"""
			crs.execute(query)
			db.commit()
			crs.close()

		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 



def kv_query(data:dict):
	keys =""
	values=""
	for item in data.keys():
		keys+= f"{item},"
		values+= f"'{data[item]}'," if type(data[item]) is str else f"{data[item]}," if data[item] != None else "null,"
	keys=keys[0:-1]
	values=values[0:-1]
	return keys,values