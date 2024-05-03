data = {
    "id":1,
    "name":"kazuki",
    "age":32,
    "code":"12fa4"
}

def insert_query(table,data:dict):
	query=f"INSERT INTO {table}"
	keys ="("
	values=" VALUES("
	for item in data.items():
		keys+= f"{item[0]},"
		values+= f"'{item[1]}'," if type(item[1]) is str else f"{item[1]},"

	return query + keys[0:-1] + ')' + values[0:-1] + ');'

print(insert_query('account',data))