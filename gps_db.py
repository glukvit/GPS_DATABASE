from read_rinex import read_rnx
from sort_path import sort_paths
from db_session import db_session
#import psycopg2

#path_to_test_date = '/home/gluk/DB_TEST_DATA'
path_to_test_date = '/home/gluk/DB_TEST_DATA/data/rinex'
path_to_station_names_cfg = '/home/gluk/bin/PROJECTS/GPS_DATABASE/stations.cfg' # Список именами станций которые заносятся в базу

def main():
    names = read_station_name(path_to_station_names_cfg)
    filelist = sort_paths(path_to_test_date,names) #Получаем список директорий где лежат файлы. Путь к каталогу с файлами, 
                                                             #путь к конфиг-файлу где лежит список имен станций для обработки.
    header = read_rnx(filelist) # Модуль read_rnx читает список файлов и возвращает список словарей. Каждый словарь шапка файла.
    db_session(header) #Передаем список словарей на загрузку в базу
 #   print(header)

def read_station_name(path_to_station_names_cfg): #Чтение конфига и создание списка из имен станций
    with open(path_to_station_names_cfg, 'r') as file:
        names =  file.read()
    return(names)

if __name__ == "__main__":
    main()


