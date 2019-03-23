Запускать так:
Скачать wget'ом модели: [link1](https://downloader.disk.yandex.ru/disk/044cf90a94c0ada997350578cac6b6794e26be1fc782ab391b45e49352736261/5c95bb3b/yJHPQbC5edZs7FVyJyOdYdnhXELxv-Cli6CUY3JkTweftSRNeQ5IYI-oDe0PzADn_LsbLzDY8gKzKMiuBHqwXQ%3D%3D?uid=0&filename=myModelWhite.h5&disposition=attachment&hash=I%2BiQ9ovU6GSb00B7W5dfdpRiT9Et%2BIEiAXKVD7WpcS5t8stFdnmtkBm9JX5a%2BBzYq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-hdf&fsize=97236208&hid=ff2a5481162a0c6e4e1fb6494fdbc556&media_type=data&tknv=v2), [link2](https://downloader.disk.yandex.ru/disk/8b38c7d4375fed6cc4c6a91fbe4494d8e5037c4ac45490367df51a9cc4739e4c/5c95bba4/yJHPQbC5edZs7FVyJyOdYZvNBW1h2frbT7o2N5rRJceoAvEaZPsjhzkeRFg2OsdajJ0v5A9tW5x5JHlRnfOEag%3D%3D?uid=0&filename=myModelBlack.h5&disposition=attachment&hash=ScvBTk7JedeSmtKslKEDjgX02rw/dqgC1YjGK3Tub4wTa1Jg08iFuOFb%2ByJTF6xhq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-hdf&fsize=97236208&hid=22401d1fd659ccf79a8b5d2c4b031a9f&media_type=data&tknv=v2) положить их туда же, где находится main_runner.py, а затем запустить `python main_runner.py`
Если ссылки перестали действовать, напишите мне.

# Darin
~
План:
1) - [x] неинтерактивный UI, который просто рисует доску
2) - [x] обучить простую модель с учителем, без фичей - на вход доска, заполненная 1, 0, -1, на выходе - доска с ожиданием выигрыша. Ходим туда, где максимум.
3) - [x] добавить к пункту выше фичи - переворот, симметричный поворот, ходить только в ближние поля.
4) - [x] сделать так, чтобы модель могла играть хотя-бы с самим собой. Возможно это стоит сделать до пункта 3.
5) - [x] т.к. ожидания от обучения с учителем очень низкие, то добавим дерево разбора случаев, чем-то напоминающее дерево Монте-карло (но это не то).
6) - [ ] тут мощности обучения с учителем подходят к концу, пора бы уже RL внедрять. Сначала скопирую модель с крестиков-ноликов, которые были 3x3 и придумаю, как эту модель применить тут.
7) - [ ] сделать нормальную модель на RL
8) - [ ] (опционально) Нужно сделать интерактивный UI, чтобы показать комиссии нашего <s>крутого и сильного</s> бота.

Пункты 1-5 нужно сделать до начала марта. Остальное - не знаю, как пойдет по сложности.
