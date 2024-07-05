# 3dml_hw8
## [Моделирование в Blender](https://github.com/shlyahin/3dml_hw8/tree/main/blender)
Директория содержит блендер-файлы, также скрипт и текстуры к ним для 1 и 2 заданий. Смоделирован знак "Пешеходный переход".
### [Моделирование дорожного знака в Blender](https://github.com/shlyahin/3dml_hw8/blob/main/blender/traffic_sign.blend)
### [Моделирование разметки для дорожного знака в Blender](https://github.com/shlyahin/3dml_hw8/blob/main/blender/traffic_sign_markup.blend)
## [Датасет](https://drive.google.com/file/d/14t4KIasAMZ8m6FkEYll_AISpd5RgPR0q/view?usp=drive_link)
Разметка сгенерирована в формате YOLO. Полученный датасет выложен в заархивированном виде по ссылке https://drive.google.com/file/d/14t4KIasAMZ8m6FkEYll_AISpd5RgPR0q/view?usp=drive_link
## [Обучение YOLOv8 для детекции знака "Пешеходный переход"](https://github.com/shlyahin/3dml_hw8/tree/main/notebooks)
Дообучена модель YOLOv8-nano.

[Ноутбук](https://github.com/shlyahin/3dml_hw8/blob/main/notebooks/yolo_train_hw08.ipynb) скорее для ознакомления, для запуска нужно изменить все ссылки. Веса обученной модели [здесь](https://github.com/shlyahin/3dml_hw8/blob/main/notebooks/weights/best.pt).

Результаты теста на [реальных изображениях](notebooks/data/test) лежат [тут](https://github.com/shlyahin/3dml_hw8/tree/main/notebooks/preds).

