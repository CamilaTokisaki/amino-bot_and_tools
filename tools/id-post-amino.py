import aminofix

client = aminofix.Client()
client.login(email="here's your login", password="Here's your password")
sub_client = aminofix.SubClient(comId="and here's your amino ID", profile=client.profile)

for title, blogId in zip(sub_client.get_user_blogs('your account id').title, sub_client.get_user_blogs('your account id').blogId):
	print(title, blogId)
