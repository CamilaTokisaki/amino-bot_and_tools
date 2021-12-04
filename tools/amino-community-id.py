import aminofix

client = aminofix.Client()
client.login(email="here's your login", password="Here's your password")

for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print(f"{name}: {id}")
