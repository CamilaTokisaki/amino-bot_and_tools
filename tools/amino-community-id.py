import amino

client = amino.Client()
client.login(email='', password='')

for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print(f"{name}: {id}")
