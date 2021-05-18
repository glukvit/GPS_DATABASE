import os
from dir_list import get_file_list
#Модулю выбирает из входной директории пути к ринекс-файлам находящиеся в поддиректориях. Поддиректории проверяются
#по именам станций которые идут в обработку. На вход основной путь типа /home/gluk/DB_TEST_DATA/data/rinex,
#путь к конфигу со списком используемых станций
filelist = []
def sort_paths(path,names): # На вход  основной путь к директории с ринексами, файл со списком станций
 #   names= read_station_name(cfg_flie) #Читаем из конфига список используемых станций
    dirlist =[] # Сюда сложим список директорий содержащих в названиях имя одной из станций которое есть в конфиге. 
    for root, dirs, files in os.walk(path): # Пробегаемся по директории с ринексами
        for dir in dirs: # Берем названия поддиректорий в основном пути к ринексам
                if dir in names: #Если путь директории содержит название одной из станций то
                    dirlist.append(os.path.join(root,dir)) # добавляем его список путей 
    dirlist =sorted(dirlist) 
    for every in dirlist: #Получаем пути файлов из списка
        cur_dir_filelist = get_file_list(every) # Подаем на вход модуля get_file_list каждый элемент списка
        for item in cur_dir_filelist: #cur_dir_filelist это список списков чтобы сделать обычный список:
            filelist.append(item) 
    print(filelist)
    return(filelist)

# def read_station_name(cfg_file): #Чтение конфига и создание списка из имен станций
#     with open(cfg_file, 'r') as file:
#         names =  file.read()
#     return(names)
