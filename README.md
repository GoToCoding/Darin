1Запускать так:
Скачать wget'ом модели: [link1](https://downloader.disk.yandex.ru/disk/bd06e8fd1e7d3d7084c65385bef9c761f9f8fcacf32502737cbbbc52d7c6ce30/5c9646cd/yJHPQbC5edZs7FVyJyOdYfsLy_-f3Z23oulj8EX2jdIwb8sIS9Bi7FWpDFB0zkOqMS7e7j5yJd5rA1apIocoBQ%3D%3D?uid=0&filename=myModelBlack%20%283%29.h5&disposition=attachment&hash=QqZ1KCi1dFtkGSH09ztZq/2AbLOzc9/Sj4/kuGBapqoWnBFuhT5bMWnEpHpSnLMMq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-hdf&fsize=97236208&hid=8700be8c9ac6a44dfb4f82a367db3cf2&media_type=data&tknv=v2), [link2](https://downloader.disk.yandex.ru/disk/f5a157528db517f73a23b6acccb1300581c2febbf132bc4df690e27037cfc61b/5c964700/yJHPQbC5edZs7FVyJyOdYdnhXELxv-Cli6CUY3JkTweftSRNeQ5IYI-oDe0PzADn_LsbLzDY8gKzKMiuBHqwXQ%3D%3D?uid=0&filename=myModelWhite%20%282%29.h5&disposition=attachment&hash=KNkzm26Jj8ldwrEeLD5YO0qZQgEdTWqi5N8gATrouvJ%2B%2Bmn4adXOtNMc0ONvJaZHq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-hdf&fsize=97236208&hid=ff2a5481162a0c6e4e1fb6494fdbc556&media_type=data&tknv=v2) положить их туда же, где находится main_runner.py, а затем запустить `python main_runner.py`
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
