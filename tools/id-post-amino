import amino

client = amino.Client()
client.login(email='your mail', password='your password')
sub_client = amino.SubClient(comId='id of your community', profile=client.profile)

for title, blogId in zip(sub_client.get_user_blogs('your post').title, sub_client.get_user_blogs('your post').blogId):
	print(title, blogId)
