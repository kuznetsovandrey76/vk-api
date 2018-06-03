import requests

def main():
	r=requests.get('https://api.vk.com/method/friends.get?user_id=YOUR-USER-ID&order=hints&fields=bdate,photo_100&access_token=YOUR-ACCESS-TOKEN&v=5.78')

	friends = list(r.json()['response']['items'])
	# {'id': int, 'first_name': str, 'last_name': str, 'bdate': str|None}
	
	for i in friends:
		try:
			if i['bdate'].count('.') == 2:
				i['bdate'] = i['bdate'][:i['bdate'].rfind('.')]
		except KeyError: 
			i['bdate'] = None

		# Создастся новый файл или допишется в существующий 
		with open('test.html', 'a', encoding='utf-8') as t:
			# <li><img src="https://pp.userapi.com/.../.../.../....jpg?ava=1"><a href="https://vk.com/id123456789">Ivan Ivanov</a></li>
			t.write(f'<li><img src="{i["photo_100"]}"><a href="https://vk.com/id{i["id"]}">{i["first_name"]} {i["last_name"]}</a></li>')
			t.write('\n')

		# id: 123456789, name: Ivan Ivanov - 15.1
		# print(f'id: {i["id"]}, name: {i["first_name"]} {i["last_name"]} - {i["bdate"]}')

if __name__ == '__main__':
	main()


