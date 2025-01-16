# project «Great Sea Battle» / проект «Great Sea Battle»
### Team composition / Склад команди:
- Hegor Halkin / Єгор Галкін [github.com/EgorGalkinORG](https://github.com/EgorGalkinORG)
- Mykytenko Petro / Микитенко Петро [github.com/mikitenko-petro](https://github.com/mikitenko-petro)
- David Petrenko / Давид Петренко [github.com/Davidptn](https://github.com/Davidptn)
____

# Main Information of project / Основна інформація про проект 
### Project can / Проект може:
1. Create a Battleship game / Створювати гру у кораблі
1. Create the server / Створювати сервер
1. Connect to server / Підключатися до сервера 
____

### Project mechanics / Механіки проекту:
1. Quests / Квести
2. Achievements / Ачівки
3. Abilities / Здібності

# How correctly run the project / Як правильно запустити проект
### Libraries which you need for run the project / Бібліотеки які необхідні для запуску проекту:
1. pygame
We need pygame to create the main app / Для створення головної програми нам потрібен pygame
1. pyperclip
We need pyperclip to fast paste text / Нам потрібен pyperclip для швидкого вставлення тексту

### Command for fast installing / Команда для швидкого встановлення:
```python
pip install -r requirements.txt
```

### Run main file / Запустіть основний файл
Done! / Готово!
# How correctly run the server / Як правильно запустити сервер

### Run main file / Запустіть основний файл

### Enter your IP and any port / Введіть свій IP та будь-який порт

Done! / Готово!
____

# Main Structure of project / Основна структура проекту:
```mermaid
graph TD;
    sea_battle_SPRINT-->program_modules;
    program_modules-->game_modules;
    game_modules-->grid.py;
    game_modules-->ship.py;
    game_modules-->ships_lable.py;

    program_modules-->game_modules;
    game_modules-->achievements;
    achievements-->parent_achievement_class.py;

    game_modules-->battle;
    battle-->cell.py;
    battle-->check_hit_collision.py;
    battle-->check_random_ship_collision.py;
    battle-->dummy_ship.py;
    battle-->grid.py;
    battle-->ship_manager.py;
    battle-->ship.py;

    game_modules-->quests;
    quests-->first_kill_all_smallest_ships_quest.py;
    quests-->first_kill_largest_ship_quest.py;
    quests-->first_kill_quest.py;
    quests-->in_first_move_hit_enemy_quest.py;
    quests-->kill_two_ships_in_time_quest.py;
    quests-->parent_quest_class.py;
    quests-->quest_manager.py;

    game_modules-->main_game_manager.py;

    program_modules-->game_widgets;
    game_widgets-->capitan_icon.py;
    game_widgets-->fire_animation_widget.py;
    game_widgets-->fps_counter.py;
    game_widgets-->last_choise_button.py;
    game_widgets-->quest_label.py;
    game_widgets-->random_placement_button.py;
    game_widgets-->return_button.py;
    game_widgets-->turn_button.py;

    program_modules-->scenes;
    scenes-->achievement_screen_scene.py;
    scenes-->conect_to_server_scene.py;
    scenes-->end_screen_scene.py;
    scenes-->game_screen_scene.py;
    scenes-->main_screen_scene.py;
    scenes-->prepare_to_game_screen_scene.py;

    program_modules-->tools;
    tools-->data_manager.py;
    tools-->image_container.py;
    tools-->json_manager.py;
    tools-->music_manager.py;
    tools-->pygame_storage.py;
    tools-->scene_manager.py;
    tools-->search_path.py;
    tools-->string_manager.py;

    program_modules-->widgets;
    widgets-->pygame_animation.py;
    widgets-->pygame_button.py;
    widgets-->pygame_check_box.py;
    widgets-->pygame_hitbox.py;
    widgets-->pygame_image.py;
    widgets-->pygame_label.py;
    widgets-->pygame_rect.py;
    widgets-->pygame_text_input.py;
    widgets-->pygame_text.py;

    program_modules-->__init__.py;
    program_modules-->client.py;
    program_modules-->pygame_setup.py;
    
    sea_battle_SPRINT-->static;
    static-->fonts;
    static-->images;
    static-->json;
    static-->sound;

    sea_battle_SPRINT-->venv;

    sea_battle_SPRINT-->.gitignore;
    sea_battle_SPRINT-->requirements.txt;
    sea_battle_SPRINT-->README.MD;

    sea_battle_SPRINT-->main.py;
``` 
____

# Conclusion / Висновок:
Project taught us how to do / Проект навчив нас як це робити:
1. Create server and clients / Створювати серверів і клієнтів
1. Taught how to make multiplayer games /  Навчив робити багатокористувацькі ігри
1. Work with pygame and others lidraries / Працювати з бібліотеками pygame та іншими
1. Work with OOP / Працювати з ООП
____
# Enjoy the game! / Приємної гри!
 