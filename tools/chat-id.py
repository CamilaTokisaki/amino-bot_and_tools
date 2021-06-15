import amino
client = amino.Client()
client.login(email='your mail', password='your password')
sub_client = amino.SubClient(comId='id community', profile=client.profile)

for name, id in zip(sub_client.get_chat_threads().title, sub_client.get_chat_threads().chatId):
	print(f"{name}: {id}")
