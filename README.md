Изменяем:   
`YOUR-USER-ID` - вставляем id из vk  
`YOUR-ACCESS-TOKEN` - вставляем свой access token из своих приложений `https://vk.com/apps?act=manage`  

Запускаем:  
```sh
$ python main.py  
```

Создается `test.html` со списком всех друзей выбранного пользователя `YOUR-USER-ID` __фото + ссылка__  

Запускаем:  
```sh
$ python top100.py  
```

Создается `top100.html` ТОП самых частых друзей у друзей `VK-USER-ID` __фото + ссылка__  

> [Дополнительная информация](https://vk.com/dev/friends.get) - friends.get  

