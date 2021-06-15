import amino

client = amino.Client()
client.login(email='your mail', password='your password')
sub_client = amino.SubClient(comId='id of your community', profile=client.profile)

for title, blogId in zip(sub_client.get_user_blogs('your account id').title, sub_client.get_user_blogs('your account id').blogId):
	print(title, blogId)
