import aminofix

client = aminofix.Client()
client.login(email="here's your login", password="Here's your password")
sub_client = aminofix.SubClient(comId="and here's your amino ID", profile=client.profile)

for nickname, id in zip(sub_client.search_users('enter your nickname here').nickname,
                        sub_client.search_users('enter your nickname here').userId):
    print(nickname, id)
