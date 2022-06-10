import sqlite3

# создание таблицы и курсора
with sqlite3.connect("Data_HighRise.PNG") as data_generator:
    sql = data_generator.cursor()

# создание столбцов
sql.execute("""CREATE TABLE IF NOT EXISTS data_highRise (
    num INTEGER PRIMARY KEY AUTOINCREMENT,
    night TEXT,
    creation TEXT,
    picture TEXT
)""")

# добавление записей в таблицу
data_num = input('1')
data_night = input('2')
data_creation = input('3')
data_picture = input('4')


# поверка на существование записи
try:
    sql.execute("SELECT * FROM data_highRise")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO data_highRise VALUES (?, ?, ?, ?)", (data_num, data_night,
                                                                       data_creation, data_picture))
        print("Регистрация прошла успешно ! ")
    else:
        print("Такая запись уже существует ! ")
# обработка ошибки
except sqlite3.Error as e:
    print("Error: ", e)
finally:
    sql.close()
    data_creation.close()
