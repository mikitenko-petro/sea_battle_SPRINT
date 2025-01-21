# project «Great Sea Battle» / проект «Great Sea Battle»
### Team composition / Склад команди:
- Mykytenko Petro / Микитенко Петро: [github.com/mikitenko-petro](https://github.com/mikitenko-petro)
- Hegor Halkin / Єгор Галкін: [github.com/EgorGalkinORG](https://github.com/EgorGalkinORG)
- David Petrenko / Давид Петренко: [github.com/Davidptn](https://github.com/Davidptn)

____

# How correctly run the project / Як правильно запустити проект

## Server / Сервер

### Commands for installing / Команди для встановлення:
ALL COMMANDS EXECUTE IN BASH TERMINAL / ВСІ КОМАНДИ ВИКОНАТИ В BASH ТЕРМІНАЛІ

#### clone the project / клонування проєкту
```bash
git clone https://github.com/mikitenko-petro/sea_battle_SPRINT_server.git
```

#### make virtual environment / робимо віртуальне середовище
```bash
python3 -m venv venv
```
#### activate the virtual environment / активуємо віртуальне середовище

##### for windows / для windows
```bash
source venv/Scripts/activate
```

##### for macOS / для macOS
```bash
source venv/bin/activate
```

#### run the project / запускаємо проєкт
```bash
python main.py 
```

### or just run exe/pkg file / або просто запустіть файл exe/pkg

## Game / Гра

### Commands for installing / Команди для встановлення:
ALL COMMANDS EXECUTE IN BASH TERMINAL / ВСІ КОМАНДИ ВИКОНАТИ В BASH ТЕРМІНАЛІ

#### clone the project / клонуємо проєкт
```bash
git clone https://github.com/mikitenko-petro/sea_battle_SPRINT.git
```

#### make virtual environment / робимо віртуальне середовище
```bash
python3 -m venv venv
```
#### activate the virtual environment / активуємо віртуальне середовище

##### for windows / для windows
```bash
source venv/Scripts/activate
```

##### for macOS / для macOS
```bash
source venv/bin/activate
```

#### download libraries / завантаження бібліотек
```bash
pip3 install -r requirements.txt
```

#### run the project / запускаємо проєкт
```bash
python main.py 
```

### or just run exe/pkg file😅 / або просто запустіть файл exe/pkg😅

### To play click on the button in the middle / щоб грати натисніть на кнопку по середині
![](https://cdn.discordapp.com/attachments/1330986741015908372/1330986789518840059/image.png?ex=678ff98b&is=678ea80b&hm=fcbe45ebb1659d33f2d33a86326b5f2176f2c164d3edecc30514e34f3e8808a6&)

### Enter the IP or click on the computer icon if server is using the same IP with your, and enter and port  / Введіть IP-адресу або клацніть на значок комп'ютера, якщо сервер використовує ту саму IP-адресу що й ваш, і введіть порт
![](https://cdn.discordapp.com/attachments/1330986741015908372/1330988978618241024/image.png?ex=678ffb95&is=678eaa15&hm=bf863f329336d67ccac925a7ef73b14328503fc98463e0049e27c8c9b30f93c2&)

____
# Main Information of project / Основна інформація про проект 

# Libraries which was used in the project / Бібліотеки які були використані у проекті:
1. pygame
We need pygame to create the main app / Для створення головної програми нам потрібен pygame
2. pyperclip
We need pyperclip to fast paste text / Нам потрібен pyperclip для швидкого вставлення тексту

____
# Project mechanics / Механіки проекту:

### Storage
stores variables and dictionaries / зберігає в собі змінні у словниках

```python
class Storage():
    def __init__(self):
        self.storage_dict = {}

    def add_variable(self, storage_object : dict):
        is_found = False
        value_key = list(storage_object.keys())

        for item in self.storage_dict.keys():
            if item != value_key[0]:
                is_found = False
            else:
                is_found = True
                break
        
        if is_found == False:
            self.storage_dict.update(storage_object)

storage = Storage()
``` 

Storage is needed to store and pass variables without loop import / Storage потрібен для зберігання та передачі змінних без циклічного імпорту


```python

storage.add_variable({"SceneManager": SceneManager()})
``` 

```python

storage.storage_dict["SceneManager"].show(event = event)
``` 

### Search path
need to create right path to file / потрібен для створення потрібний шлях до файла

```python
def search_path(file_name : str):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(os.path.join(".", "_internal", *file_name.split("/")))
    else:
        path = os.path.abspath(os.path.join(".", *file_name.split("/")))

    return path
```

### exemple / приклад
neded for searching images / використовуємо для пошуку зображень


```python
image = pygame.image.load(search_path(f'static/images/{filename}')).convert_alpha()
```
____
# Main Structure of project / Основна структура проекту:
```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    C{sea_battle_SPRINT}-->program_modules;

    program_modules-->game_modules;
    game_modules-->achievements;
    achievements-->parent_achievement_class.py;
    parent_achievement_class.py-->achievement_manager.py;
    achievement_manager.py-->fifth_win_achievement.py;
    fifth_win_achievement.py-->first_win_achievement.py;
    first_win_achievement.py-->still_standing_achievement.py;
    still_standing_achievement.py-->three_win_achievement.py;

    game_modules-->battle;
    battle-->cell.py;
    cell.py-->check_hit_collision.py;
    check_hit_collision.py-->check_random_ship_collision.py;
    check_random_ship_collision.py-->dummy_ship.py;
    dummy_ship.py-->grid.py;
    grid.py-->ship_manager.py;
    ship_manager.py-->ship.py;

    game_modules-->quests;
    quests-->first_kill_all_smallest_ships_quest.py;
    first_kill_all_smallest_ships_quest.py-->first_kill_largest_ship_quest.py;
    first_kill_largest_ship_quest.py-->first_kill_quest.py;
    first_kill_quest.py-->in_first_move_hit_enemy_quest.py;
    in_first_move_hit_enemy_quest.py-->kill_two_ships_in_time_quest.py;
    kill_two_ships_in_time_quest.py-->parent_quest_class.py;
    parent_quest_class.py-->quest_manager.py;

    game_modules-->B{main_game_manager.py};

    program_modules-->game_widgets;
    game_widgets-->capitan_icon.py;
    capitan_icon.py-->fire_animation_widget.py;
    fire_animation_widget.py-->fps_counter.py;
    fps_counter.py-->last_choise_button.py;
    last_choise_button.py-->quest_label.py;
    quest_label.py-->random_placement_button.py;
    random_placement_button.py-->return_button.py;
    return_button.py-->turn_button.py;

    program_modules-->scenes;
    scenes-->achievement_screen_scene.py;
    achievement_screen_scene.py-->conect_to_server_scene.py;
    conect_to_server_scene.py-->end_screen_scene.py;
    end_screen_scene.py-->game_screen_scene.py;
    game_screen_scene.py-->main_screen_scene.py;
    main_screen_scene.py-->prepare_to_game_screen_scene.py;

    program_modules-->tools;
    tools-->data_manager.py;
    data_manager.py-->image_container.py;
    image_container.py-->json_manager.py;
    json_manager.py-->music_manager.py;
    music_manager.py-->A;
    A{storage.py}-->scene_manager.py;
    scene_manager.py-->search_path.py;
    search_path.py-->string_manager.py;

    program_modules-->widgets;
    widgets-->pygame_animation.py;
    pygame_animation.py-->pygame_button.py;
    pygame_button.py-->pygame_check_box.py;
    pygame_check_box.py-->pygame_hitbox.py;
    pygame_hitbox.py-->pygame_image.py;
    pygame_image.py-->pygame_label.py;
    pygame_label.py-->pygame_rect.py;
    pygame_rect.py-->pygame_text_input.py;
    pygame_text_input.py-->pygame_text.py;

    program_modules-->__init__.py;
    __init__.py-->client.py;
    client.py-->pygame_setup.py;
    
    C-->static;
    static-->fonts;
    fonts-->images;
    images-->json;
    json-->sound;

    C-->venv;
    venv-->.gitignore;
    .gitignore-->requirements.txt;
    requirements.txt-->README.MD;
    README.MD-->main.py;

    style A fill:#706f70,stroke:#333,stroke-width:6px
    style B fill:#706f70,stroke:#333,stroke-width:6px
    style C fill:#4d007d,stroke:#333,stroke-width:6px
``` 
____

# Code problems we solved / Проблеми з кодом, які ми вирішили:
1. client-server structure problem / проблема структури клієнт-сервер
2. data routing problem / проблема маршрутизації даних
3. temporary animation problem / проблема тимчасової анімації

___

# Conclusion / Висновок:
### Davyd / Давид
1. Studied from the best team leader / Вчився у найкращого тімліда
2. I remembered the materials I went through before. / Пригадав материали які проходив до цього
3. I learned a little about drawing animations and drawings in Aseprite / Трошки навчився малювювати анімації та малюнки в Aseprite
4. I got to know pygame in a new way / По новому ознайомився з pygame
5. Learned to work with coordinates / Навчився працювати з кординатами
6. Worked with arithmetic progression / Працював з аріфметичною прогресією

### Hegor / Єгор
1. Studied from the best team leader / Вчився у найкращого тімліда
2. Learned new commands / Навчився новим командам (enumerate, match/case)
3. Improved skills in OOP / Покращив навички у ООП
4. Improved skills in socket / Покращив навички у socket
5. Repeated pygame / Повторив pygame

### Petro / Петро
1. improved team leader skills / покращив навички тімліда
2. learned to work with pygame (I had almost no experience with it before) / навчився працювати з pygame (до цього майже не вчив)
3. learned to work with web sockets / навчився працювати з веб сокетами
4. learned OOP principles (inheritance, encapsulation) / вивчив принципи ООП (наслідування, інкапсуляція)
5. learned the principles of good project architecture and code (DRY, KISS) / вивчив принципи гарної архітектури і коду проекта (DRY, KISS)
____

# Enjoy the game! / Приємної гри!