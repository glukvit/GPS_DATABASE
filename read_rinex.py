import gzip
#from os import linesep
from os import path
## Модуль читает заголовок rinex файла. На вход архивированный ринекс
#header ={}
list_of_headers = [] #Здесь будет список словарей заголовков файлов
def read_rnx(filelist): # Чтение файлов. На вход список всех файлов 
    for every in filelist: # Берем каждый ринекс файл
        header={} #Обнуляем словарь перед каждой итерацией, чтобы не захватить данные из предыдущего файла
        print('Читаю файл', every) 
        line='' # Объявлем пустую строку куда будем читать построчно
        with gzip.open(every, 'r') as file: # Открываем архивированный файл
            while not 'END OF HEADER' in line: # Пока строка не содержит конец заголовка читаем 
                line = file.readline() #Читаем строку
                if isinstance(line, bytes): #Проверяем не байтовая ли строка. Они должны быть все байтовые, но нужно проверить
                    line = line.decode('utf-8') #Если строка байтовая декодируем в стринг
                header_of_file = header_to_dict(every, line,header) #Обрабатываем каждую строку и добавляем в словарь необходимые данные с ключами.
                                                                    # На вход название файла, одна строка с данными и словарь header
        header_of_file['filename'] = every # Дописываем в основной словарь поле с названием станции
        list_of_headers.append(header_of_file) #В список словарей заголовков дописываем очередной словарь с заголовком
    #return (header_of_file)  
    return(list_of_headers)
 #               break
 #       exit()
def header_to_dict(every,line,header): # Обработчик строки. Ищет соответствие в строке и заносит в словарь параметры

    if 'CRINEX VERS' in line:
        header['CRINEX VERS'] = line[0:10].rstrip() #.rstrip() удаляет пробелы с права в строке
        
    elif 'CRINEX PROG' in line:
        header['CRINEX PROG'] = line[0:21].rstrip()
#    elif 'DATE' in line:
#        header['DATE'] = line[40:60].rstrip()
    elif 'MARKER NAME' in line:
        header['MARKER NAME'] = line[0:10].rstrip()
    elif 'MARKER NUMBER' in line:
        header['MARKER NUMBER'] = line[0:10].rstrip()
    elif 'OBSERVER / AGENCY' in line:
        header['OBSERVER'] = line[0:10].rstrip()
        header['AGENCY'] = line[20:60].rstrip()
    elif 'REC # / TYPE / VERS' in line:
        header['REC'] = line[0:10].rstrip()
        header['REC # / TYPE'] = line[20:40].rstrip()
        header['REC # / TYPE / VERS'] = line[40:60].rstrip()
    elif 'ANT # / TYPE' in line: 
        header['ANT'] = line[0:20].rstrip()
        header['ANT # / TYPE'] = line[20:35].rstrip()
        header['DOME'] = line[35:60].rstrip().lstrip() #lstrip() удаляет пробелы слева в строке
    elif 'APPROX POSITION XYZ' in line:
        header['X'] = line[0:15].rstrip().lstrip() 
        header['Y'] = line[15:30].rstrip().lstrip()
        header['Z'] = line[30:60].rstrip().lstrip()
    elif 'ANTENNA: DELTA H/E/N' in line:
        header['H'] = line[0:15].rstrip().lstrip()
        header['E'] = line[15:30].rstrip().lstrip()
        header['N'] = line[30:60].rstrip().lstrip()
    elif 'INTERVAL' in line:
        header['INTERVAL'] = line[0:10].rstrip().lstrip()
    elif 'TIME OF FIRST OBS' in line:
        header['TIME OF FIRST OBS'] =line[0:60].rstrip().lstrip()


    return(header)
    