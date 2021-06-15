import amino

client = amino.Client()
client.login(email='your mail', password='your password')
sub_client = amino.SubClient(comId='your id community', profile=client.profile)

for nickname, id in zip(sub_client.search_users('enter your nickname here').nickname,
                        sub_client.search_users('enter your nickname here').userId):
    print(nickname, id)
