import mysql.connector as con

class SyntaxException(Exception):pass
class NotFoundException(Exception):pass
class ItemAlreadyExistException(Exception):pass
class DBConnectionFail(Exception):pass


class DBCon ():
	def up ():
		try:
			return con.connect(user="root",password="2591439",database="dedb")
		except: return DBConnectionFail	

def insert_query(table,data:dict):
	query=f"INSERT INTO {table}"
	keys ="("
	values=" VALUES("
	for item in data.items():
		keys+= f"{item[0]},"
		values+= f"'{item[1]}'," if type(item[1]) is str else f"{item[1]},"

	return query + keys[0:-1] + ')' + values[0:-1] + ');'

def update_query(table,data:dict):

	query= f"UPDATE {table} SET "
	id = f" WHERE id = {data['id']}"
	data.pop("id")
	sets=""

	for item in data.items():
		sets+= f"{item[0]} = "
		sets+= f"'{item[1]}'," if type(item[1]) is str else f"{item[1]},"

	return query+sets[0:-1]+id+";"

def item_exist(table, name):
	db = DBCon.up()

	crs = db.cursor(dictionary=True)
	crs.execute(f"""SELECT id FROM {table} where name = "{name}";""")
	result = crs.fetchone()
	db.close()
	return result != None


class Account():
	def get_all(self):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			query="""SELECT id,name,email FROM account;"""
			crs.execute(query)
			results = crs.fetchall()
			crs.close()
			return results
		
		except: raise DBConnectionFail

	def get_by_id(self, id:int):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			crs.execute(f"""SELECT id,name,email FROM account where `id` = {id};""")
			result = crs.fetchone()
			crs.close()

			if result == None : raise NotFoundException
			return result
		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException: raise NotFoundException

	def new(self, data:dict):
		try:
			if item_exist('account', data["name"]): raise ItemAlreadyExistException
			db = DBCon.up()

			crs = db.cursor()
			crs.execute(insert_query('account',data))
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail	
		except ItemAlreadyExistException: raise ItemAlreadyExistException
		except Exception:raise SyntaxException
	
	def drop(self, id:int):
		try:
			self.get_by_id(id)
			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM account WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()
		except NotFoundException : raise NotFoundException
		
	def update(self, data:dict):
		try:
			self.get_by_id(data["id"])
			db = DBCon.up()
			crs = db.cursor()
			crs.execute(update_query('account',data))
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

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
		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def new(self, data:dict):
		try:
			db = DBCon.up()	

			crs = db.cursor()
			crs.execute(insert_query('build',data))
			db.commit()
			crs.close()

		except DBConnectionFail: raise DBConnectionFail
		except Exception:raise SyntaxException

	def drop(self, id:int):
		try:
			self.get_by_id(id)

			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM build WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def update(self, data:dict):
		try:
			self.get_by_id(data["id"])

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(update_query('build',data))
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

class Monster():
	def get_all(self):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM monster;"""
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
			query = """SELECT * FROM monster WHERE `id`=%s ;""" %id
			crs.execute(query)
			result = crs.fetchone()
			crs.close()

			if result == None: raise NotFoundException
			return result
		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def get_by_type(self,type:str):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = f"select * from monster where type = '{type}'"
			crs.execute(query)
			result = crs.fetchall()
			db.close()
			return result
		except DBConnectionFail: raise DBConnectionFail
		except: raise SyntaxError

	def new(self,data:dict):
		try:
			if item_exist('monster', data["name"]): raise ItemAlreadyExistException
			db = DBCon.up()

			crs = db.cursor()
			crs.execute(insert_query('monster',data))
			db.commit()
			crs.close()

		except ItemAlreadyExistException: raise ItemAlreadyExistException
		except DBConnectionFail: raise DBConnectionFail
		except Exception:raise SyntaxException

	def drop(self,id:int):
		try:
			self.get_by_id(id)

			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM monster WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def update(self,data:dict):
		try:
			self.get_by_id(data["id"])

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(update_query('monster',data))
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException

class Item():
	def get_all(self):
		try:
			db = DBCon.up()

			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM item;"""
			crs.execute(query)
			result = crs.fetchall()
			crs.close()
			return result
		
		except DBConnectionFail: raise DBConnectionFail
		except: raise SyntaxException

	def get_by_id(self, id:int):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = """SELECT * FROM item WHERE `id`=%s ;""" %id
			crs.execute(query)
			result = crs.fetchone()
			crs.close()

			if result == None: raise NotFoundException
			return result
		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def get_by_category(self,category:str):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = f"select * from item where category = '{category}'"
			crs.execute(query)
			result = crs.fetchall()
			db.close()
			return result
		except DBConnectionFail: raise DBConnectionFail
		except: raise SyntaxError

	def get_by_type(self,type:str):
		try:
			db = DBCon.up()
			crs = db.cursor(dictionary=True)
			query = f"select * from item where type = '{type}'"
			crs.execute(query)
			result = crs.fetchall()
			db.close()
			return result
		except DBConnectionFail: raise DBConnectionFail
		except: raise SyntaxError

	def new(self, data:dict):
		try:
			if item_exist('item', data["name"]): raise ItemAlreadyExistException
			db = DBCon.up()

			crs = db.cursor()
			crs.execute(insert_query('item',data))
			db.commit()
			crs.close()

		except ItemAlreadyExistException: raise ItemAlreadyExistException
		except DBConnectionFail: raise DBConnectionFail
		except Exception:raise SyntaxException

	def drop(self, id:int):
		try:
			self.get_by_id(id)

			db = DBCon.up()
			crs = db.cursor()
			crs.execute("""DELETE FROM item WHERE `id` = %s;"""%id)
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException 

	def update(self, data:dict):
		try:
			self.get_by_id(data["id"])

			db = DBCon.up()
			crs = db.cursor()
			crs.execute(update_query('item',data))
			db.commit()
			crs.close()

		except DBConnectionFail: DBConnectionFail
		except NotFoundException: raise NotFoundException
		except Exception:raise SyntaxException
