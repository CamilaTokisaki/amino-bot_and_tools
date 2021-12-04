import aminofix

client = aminofix.Client()
client.login(email="here's your login", password="Here's your password")
sub_client = aminofix.SubClient(comId="and here's your amino ID", profile=client.profile)

for name, id in zip(sub_client.get_chat_threads().title, sub_client.get_chat_threads().chatId):
	print(f"{name}: {id}")
