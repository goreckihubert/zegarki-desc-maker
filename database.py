# database.py
import sqlite3

from watch import Watch


class WatchDatabase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS watches (
            kod_produktu TEXT PRIMARY KEY,
            proba TEXT,
            grawer TEXT,
            dla_kogo TEXT,
            rodzaj TEXT,
            styl TEXT,
            pochodzenie TEXT,
            szkiełko TEXT,
            rodzaj_koperty TEXT,
            szerokosc_koperty REAL,
            grubosc_koperty REAL,
            typ_paska_bransolety TEXT,
            kolor_paska_bransolety TEXT,
            wodoszczelnosc TEXT,
            mechanizm TEXT,
            gwarancja TEXT,
            kolor_tarczy TEXT
        )'''
        self.cursor.execute(query)
        self.connection.commit()

    def add_watch(self, watch_data):
        query = '''INSERT INTO watches (
            kod_produktu, proba, grawer, dla_kogo, rodzaj, styl, pochodzenie,
            szkiełko, rodzaj_koperty, szerokosc_koperty, grubosc_koperty,
            typ_paska_bransolety, kolor_paska_bransolety, wodoszczelnosc,
            mechanizm, gwarancja, kolor_tarczy
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(query, watch_data)
        self.connection.commit()

    def delete_watch(self, kod_produktu):
        query = 'DELETE FROM watches WHERE kod_produktu = ?'
        self.cursor.execute(query, (kod_produktu,))
        self.connection.commit()

    def display_watches(self):
        query = 'SELECT * FROM watches'
        self.cursor.execute(query)
        watches = self.cursor.fetchall()
        for watch in watches:
            print(watch)

    def close_connection(self):
        self.connection.close()

    def get_watch(self, kod_produktu):
        query = 'SELECT * FROM watches WHERE kod_produktu = ?'
        self.cursor.execute(query, (kod_produktu,))
        watch_data = self.cursor.fetchone()

        if watch_data:
            # Przekazujemy dane z bazy do konstruktora klasy Watch
            watch = Watch(*watch_data)
            return watch
        else:
            return None
