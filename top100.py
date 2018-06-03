import requests
import operator # Сортировка result

def main(num:int):
	""" num - количество пользователей в рейтинге """

	vk_id = 'VK-USER-ID' # Выбери id пользователя для которого хочешь составить рейтинг
	access_token = 'YOUR-ACCESS-TOKEN'
	r = requests.get(f'https://api.vk.com/method/friends.get?user_id={vk_id}&order=hints&access_token={access_token}&v=5.78')

	my_friends = list(r.json()['response']['items'])

	result = {}

	for index, value in enumerate(my_friends):
		try:
			temp = requests.get(f'https://api.vk.com/method/friends.get?user_id={value}&order=hints&access_token={access_token}&v=5.78')
			his_friends = list(temp.json()['response']['items'])
			print(f'{index}. ok')
			for j in his_friends:
				if j not in result:
					result[j] = 1
				else:
					result[j] += 1
		except KeyError: 
			print(f'{index}. delete account') 	

	sorted_result = sorted(result.items(), key=operator.itemgetter(1))

	# ТОП {num} самых частых друзей у моих друзей
	best_list = sorted_result[-1*num-1:-1]
	best_list.reverse()

	print('\nloading...')

	for i in best_list:

		# Запрашиваем фото всех участников списка
		r = requests.get(f'https://api.vk.com/method/users.get?user_id={i[0]}&fields=photo_100&access_token=7eb0f9ab7eb0f9ab7eb0f9ab767ed3de1d77eb07eb0f9ab25a37d1b9e80ceedcf71e8ee&v=5.78')

		info = r.json()['response'][0]

		with open(f'top{num}.html', 'a', encoding='utf-8') as t:
			t.write(f'<li>rate: {i[1]} <img src="{info["photo_100"]}"><a href="https://vk.com/id{info["id"]}">{info["first_name"]} {info["last_name"]}</a></li>')
			t.write('\n')

	print(f'File top{num}.html is ready')


if __name__ == '__main__':
	main(100)


