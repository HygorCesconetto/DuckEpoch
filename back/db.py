import mysql.connector as con

class SyntaxException(Exception):pass
class NotFoundException(Exception):pass
class UserAlreadyExistException(Exception):pass


class DBCon ():
	def up ():
		try:
			return con.connect(user="root",password="2591439",database="dedb")
		except: return SyntaxException
		


#---------------------------------------------------------------------------------------------WEAPON
class Weapom():
	def getAll(self):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query="""SELECT * FROM weapon;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		except Exception: raise SyntaxException

	def getByID(self, id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT * FROM weapon where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except NotFoundException: raise NotFoundException
		except Exception: raise SyntaxException

	def getByProp(self, prop:str):
		try:
			db = DBCon.up()
			crs= db.cursor(dictionary=True)
			crs.execute("select `type` from  weapon group by `type`;")
			types=[x["type"] for x in crs.fetchall()]

			if prop in types:
				crs.execute(f"select * from  weapon WHERE `type`= '{prop.lower()}';")
				results= crs.fetchall()
				crs.close()
			else: 
				crs.execute(f"select * from  weapon WHERE `name`= '{prop.lower()}';")
				results= crs.fetchone()
				if results == None: raise NotFoundException
				crs.close()
			return results
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def new(self, data:dict):
		try:
			keys=""
			values=""
			for key in data.keys():
				keys+="`%s`,"%key
				match key:
					case "name": values+="'%s',"%data[key].lower()
					case "type": values+="'%s',"%data[key].lower()
					case _: values+="%s,"%data[key]
				
			db = DBCon.up()
			crs = db.cursor()
			query="""INSERT INTO weapon(%s) VALUES(%s);""" %(keys[:-1],values[:-1])
			crs.execute(query)
			db.commit()
			crs.close()
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			Weapom().getByID(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM weapon WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		except Exception: raise SyntaxException
		
	def full_update(self, data:dict):
		try:
			Weapom().getByID(data["id"])
			if len(data) != 6: raise SyntaxError
			db = DBCon.up()
			crs = db.cursor()
			crs.execute(f"""UPDATE weapon SET 
			   `type`='{data["type"].lower()}', 
			   `name`='{data["name"].lower()}', 
			   `atk`={data["atk"]},
			   `atks`={data["atks"]},
			   `def`={data["def"]}
			   WHERE `id` = {data["id"]};""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def parcial_update(self, data:dict):
		try:
			Weapom().getByID(data["id"])
			sets = ""
			for key in data.keys():
				sets+= f"`{key}`="
				match key:
					case "name": sets += f"'{data[key].lower()}',"
					case "type": sets += f"'{data[key].lower()}',"
					case _: sets += f"{data[key]},"

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(f"""UPDATE weapon SET {sets[:-1]} WHERE `id`={data["id"]} ;""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException


#---------------------------------------------------------------------------------------------ARMOUR
class Armour():
	def getAll(self):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query="""SELECT * FROM armour;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		except: raise SyntaxException

	def getByID(self, id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT * FROM armour where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except NotFoundException: raise NotFoundException
		except Exception: raise SyntaxException

	def getByProp(self, prop:str):
		try:
			db = DBCon.up()
			crs= db.cursor(dictionary=True)
			crs.execute("select `type` from  armour group by `type`;")
			types=[x["type"] for x in crs.fetchall()]

			if prop in types:
				crs.execute(f"select * from  armour WHERE `type`= '{prop.lower()}';")
				results= crs.fetchall()
				crs.close()
			else: 
				crs.execute(f"select * from  armour WHERE `name`= '{prop.lower()}';")
				results= crs.fetchone()
				if results == None: raise NotFoundException
				crs.close()
			return results
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def new(self, data:dict):
		try:
			keys=""
			values=""
			for key in data.keys():
				keys+="`%s`,"%key
				match key:
					case "name": values+="'%s',"%data[key].lower()
					case "type": values+="'%s',"%data[key].lower()
					case _: values+="%s,"%data[key]
				
			db = DBCon.up()
			crs = db.cursor()
			query="""INSERT INTO armour(%s) VALUES(%s);""" %(keys[:-1],values[:-1])
			crs.execute(query)
			db.commit()
			crs.close()
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			Armour().getByID(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM armour WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		except Exception: raise SyntaxException
		
	def full_update(self, data:dict):
		try:
			db = DBCon.up()
			Armour().getByID(data["id"])
			if len(data) != 6: raise SyntaxError
			crs = db.cursor()
			crs.execute(f"""UPDATE armour SET 
			   `type`='{data["type"].lower()}', 
			   `name`='{data["name"].lower()}', 
			   `atk`={data["atk"]},
			   `hp`={data["hp"]},
			   `def`={data["def"]}
			   WHERE `id` = {data["id"]};""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def parcial_update(self, data:dict):
		try:
			Armour().getByID(data["id"])
			sets = ""
			for key in data.keys():
				sets+= f"`{key}`="
				match key:
					case "name": sets += f"'{data[key].lower()}',"
					case "type": sets += f"'{data[key].lower()}',"
					case _: sets += f"{data[key]},"

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(f"""UPDATE armour SET {sets[:-1]} WHERE `id`={data["id"]} ;""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

#---------------------------------------------------------------------------------------------TRINKET
class Trinket():
	def getAll(self):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query="""SELECT * FROM trinket;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		except: raise SyntaxException

	def getByID(self, id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT * FROM trinket where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except NotFoundException: raise NotFoundException
		except Exception: raise SyntaxException

	def getByProp(self, prop:str):
		try:
			db = DBCon.up()
			crs= db.cursor(dictionary=True)
			crs.execute("select `type` from  trinket group by `type`;")
			types=[x["type"] for x in crs.fetchall()]

			if prop in types:
				crs.execute(f"select * from  trinket WHERE `type`= '{prop.lower()}';")
				results= crs.fetchall()
				crs.close()
			else: 
				crs.execute(f"select * from  trinket WHERE `name`= '{prop.lower()}';")
				results= crs.fetchone()
				if results == None: raise NotFoundException
				crs.close()
			return results
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def new(self, data:dict):
		try:
			keys=""
			values=""
			for key in data.keys():
				keys+="`%s`,"%key
				match key:
					case "name": values+="'%s',"%data[key].lower()
					case "type": values+="'%s',"%data[key].lower()
					case _: values+="%s,"%data[key]

			db = DBCon.up()	
			crs = db.cursor()
			query="""INSERT INTO trinket(%s) VALUES(%s);""" %(keys[:-1],values[:-1])
			crs.execute(query)
			db.commit()
			crs.close()
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			Trinket().getByID(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM trinket WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		except Exception: raise SyntaxException
		
	def full_update(self, data:dict):
		try:
			Trinket().getByID(data["id"])
			db = DBCon.up()
			if len(data) != 6: raise SyntaxError
			crs = db.cursor()
			crs.execute(f"""UPDATE trinket SET 
			   `type`='{data["type"].lower()}', 
			   `name`='{data["name"].lower()}', 
			   `atk`={data["atk"]},
			   `hp`={data["hp"]},
			   `def`={data["def"]}
			   WHERE `id` = {data["id"]};""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

	def parcial_update(self, data:dict):
		try:
			db = DBCon.up()
			Trinket().getByID(data["id"])
			sets = ""
			for key in data.keys():
				sets+= f"`{key}`="
				match key:
					case "name": sets += f"'{data[key].lower()}',"
					case "type": sets += f"'{data[key].lower()}',"
					case _: sets += f"{data[key]},"

			crs = db.cursor()
			crs.execute(f"""UPDATE trinket SET {sets[:-1]} WHERE `id`={data["id"]} ;""")
			db.commit()
			crs.close()
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

#---------------------------------------------------------------------------------------------ACCOUNT
class Account():
	def getAll(self):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query="""SELECT * FROM account;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		except: raise SyntaxException

	def getByID(self, id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT * FROM account where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except NotFoundException: raise NotFoundException
		except Exception: raise SyntaxException

	def new(self, data:dict):
		try:
			#teste para ususario ja existente
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT * FROM account where `usuario` = "{data["usuario"]}";""")
			result = crs.fetchone()
			crs.close()
			if result != None : raise UserAlreadyExistException

			db = DBCon.up()	
			crs = db.cursor()
			query="""INSERT INTO account(`usuario`, `email`, `senha`) VALUES('%s','%s','%s');""" %(data["usuario"], data["email"], data["senha"])
			crs.execute(query)
			db.commit()
			crs.close()
		except UserAlreadyExistException: raise UserAlreadyExistException
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			Account().getByID(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM account WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		except Exception: raise SyntaxException
		
	def full_update(self, data:dict):
		try:
			Account().getByID(data["id"])
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
		except: raise SyntaxException

	def get_byID(self,id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM build WHERE `id`=%s ;""" %id
			crs.execute(query)
			result = crs.fetchone()
			crs.close()

			if result == None: raise NotFoundException
			return result
		except NotFoundException : raise NotFoundException
		except Exception : raise SyntaxError

	def new(self, data:dict):
		print(data)
		try:
			db = DBCon.up()	
			crs = db.cursor()
			query = f"""INSERT INTO build(`name`, `helmet`, `body`, `gloves`, `boots`, `main_hand`, `off_hand`, `amulet`, `ring`, `belt`) VALUES(
				'{data["name"]}', {data["helmet"]}, {data["body"]}, {data["gloves"]}, {data["boots"]}, {data["main_hand"]},
				 {data["off_hand"]}, {data["amulet"]}, {data["ring"]}, {data["belt"]}
				 );""" 
			crs.execute(query)
			db.commit()
			crs.close()
		except Exception:raise SyntaxException

	def drop(self, id:int):
		try:
			Build().get_byID(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM build WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		except Exception: raise SyntaxException

	def full_update(self, data:dict):
		try:
			Build().get_byID(data["id"])
			if len(data) != 11: raise SyntaxError
			db = DBCon.up()
			crs = db.cursor()
			query = f"""UPDATE build SET 
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