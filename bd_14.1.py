import sqlite3

connection = sqlite3.connect("not_telegram.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL  
)
''')

cursor.execute("DELETE FROM Users")
connection.commit()

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",
                                                                f"example{i}@gmail.com", str(i) +"0", 1000))


cursor.execute("SELECT * FROM Users")
result = cursor.fetchall()

for i in range(len(result)+1):
    if (i+1) % 2 == 0 or i == 1:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(len(result)+1):
    if (i+2) % 3 == 0 or i == 1:
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
result_end = cursor.fetchall()
for res in result_end:
    print(f"Имя: {res[0]} | Почта: {res[1]}| Возраст: {res[2]} | Баланс: {res[3]}")
    
connection.commit()
connection.close()

