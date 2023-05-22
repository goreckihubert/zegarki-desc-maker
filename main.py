# main.py
from database import WatchDatabase
from watch import Watch


def add_watch_to_database(database):
    print('Dodawanie zegarka do bazy danych:')
    kod_produktu = None
    proba = None
    grawer = None
    dla_kogo = None
    rodzaj = None
    styl = None
    pochodzenie = None
    szkiełko = None
    rodzaj_koperty = None
    szerokosc_koperty = None
    grubosc_koperty = None
    typ_paska_bransolety = None
    kolor_paska_bransolety = None
    wodoszczelnosc = None
    mechanizm = None
    gwarancja = None
    kolor_tarczy = None

    while kod_produktu is None or not kod_produktu:
        kod_produktu = input('Kod produktu: ')
        if not kod_produktu:
            print('Błąd: Kod produktu nie może być pusty.')

    while proba is None:
        proba = input('Próba: ')

    while grawer is None:
        grawer = input('Grawer: ')

    while dla_kogo is None:
        dla_kogo = input('Dla kogo: ')

    while rodzaj is None:
        rodzaj = input('Rodzaj: ')

    while styl is None:
        styl = input('Styl: ')

    while pochodzenie is None:
        pochodzenie = input('Pochodzenie: ')

    while szkiełko is None:
        szkiełko = input('Szkiełko: ')

    while rodzaj_koperty is None:
        rodzaj_koperty = input('Rodzaj koperty: ')

    while szerokosc_koperty is None:
        try:
            szerokosc_koperty = float(input('Szerokość koperty: '))
        except ValueError:
            print('Błąd: Szerokość koperty musi być liczbą.')
            szerokosc_koperty = None

    while grubosc_koperty is None:
        try:
            grubosc_koperty = float(input('Grubość koperty: '))
        except ValueError:
            print('Błąd: Grubość koperty musi być liczbą.')
            grubosc_koperty = None

    while typ_paska_bransolety is None:
        typ_paska_bransolety = input('Typ paska / bransolety: ')

    while kolor_paska_bransolety is None:
        kolor_paska_bransolety = input('Kolor paska / bransolety: ')

    while wodoszczelnosc is None:
        wodoszczelnosc = input('Wodoszczelność: ')

    while mechanizm is None:
        mechanizm = input('Mechanizm: ')

    while gwarancja is None:
        gwarancja = input('Gwarancja: ')

    while kolor_tarczy is None:
        kolor_tarczy = input('Kolor tarczy: ')

    watch = Watch(
        kod_produktu, proba, grawer, dla_kogo, rodzaj, styl, pochodzenie,
        szkiełko, rodzaj_koperty, szerokosc_koperty, grubosc_koperty,
        typ_paska_bransolety, kolor_paska_bransolety, wodoszczelnosc,
        mechanizm, gwarancja, kolor_tarczy
    )

    watch_data = (
        watch.kod_produktu, watch.proba, watch.grawer, watch.dla_kogo, watch.rodzaj, watch.styl, watch.pochodzenie,
        watch.szkiełko, watch.rodzaj_koperty, watch.szerokosc_koperty, watch.grubosc_koperty,
        watch.typ_paska_bransolety, watch.kolor_paska_bransolety, watch.wodoszczelnosc,
        watch.mechanizm, watch.gwarancja, watch.kolor_tarczy
    )

    database.add_watch(watch_data)


def delete_watch_from_database(database):
    print('Usuwanie zegarka z bazy danych:')
    kod_produktu = input('Podaj kod produktu zegarka do usunięcia: ')
    database.delete_watch(kod_produktu)


def display_watches_from_database(database):
    print('Zegarki w bazie danych:')
    database.display_watches()


def modify_watch_attributes(database, watch):
    print('Modyfikowanie atrybutów zegarka:')
    print('Dostępne atrybuty: kod_produktu, proba, grawer, dla_kogo, rodzaj, styl, pochodzenie, szkiełko, rodzaj_koperty, szerokosc_koperty, grubosc_koperty, typ_paska_bransolety, kolor_paska_bransolety, wodoszczelnosc, mechanizm, gwarancja, kolor_tarczy')
    attribute = input('Podaj nazwę atrybutu do modyfikacji: ')
    new_value = input('Podaj nową wartość: ')

    if hasattr(watch, attribute):
        setattr(watch, attribute, new_value)
        print(f"Atrybut {attribute} został zaktualizowany.")
        database.update_watch(watch.kod_produktu, attribute, new_value)
    else:
        print(f"Atrybut {attribute} nie istnieje.")


def main():
    db_file = 'watches.db'
    database = WatchDatabase(db_file)

    while True:
        print('--- MENU ---')
        print('1. Dodaj zegarek do bazy danych')
        print('2. Usuń zegarek z bazy danych')
        print('3. Wyświetl zegarki z bazy danych')
        print('4. Zmodyfikuj atrybut zegarka')
        print('0. Zakończ program')

        choice = input('Wybierz opcję: ')

        if choice == '1':
            add_watch_to_database(database)
        elif choice == '2':
            delete_watch_from_database(database)
        elif choice == '3':
            display_watches_from_database(database)
        elif choice == '4':
            kod_produktu = input('Podaj kod produktu zegarka do modyfikacji: ')
            watch = database.get_watch(kod_produktu)
            if watch:
                modify_watch_attributes(database, watch)
            else:
                print('Zegarek o podanym kodzie produktu nie istnieje.')
        elif choice == '0':
            break
        else:
            print('Nieprawidłowa opcja. Spróbuj ponownie.')

    database.close_connection()


if __name__ == '__main__':
    main()
