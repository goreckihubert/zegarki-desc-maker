# watch.py
class Watch:
    def __init__(
            self, kod_produktu, proba, grawer, dla_kogo, rodzaj, styl, pochodzenie,
            szkiełko, rodzaj_koperty, szerokosc_koperty, grubosc_koperty,
            typ_paska_bransolety, kolor_paska_bransolety, wodoszczelnosc,
            mechanizm, gwarancja, kolor_tarczy
    ):
        self.kod_produktu = kod_produktu
        self.proba = proba
        self.grawer = grawer
        self.dla_kogo = dla_kogo
        self.rodzaj = rodzaj
        self.styl = styl
        self.pochodzenie = pochodzenie
        self.szkiełko = szkiełko
        self.rodzaj_koperty = rodzaj_koperty
        self.szerokosc_koperty = szerokosc_koperty
        self.grubosc_koperty = grubosc_koperty
        self.typ_paska_bransolety = typ_paska_bransolety
        self.kolor_paska_bransolety = kolor_paska_bransolety
        self.wodoszczelnosc = wodoszczelnosc
        self.mechanizm = mechanizm
        self.gwarancja = gwarancja
        self.kolor_tarczy = kolor_tarczy

    def update_attribute(self, attribute, new_value):
        if hasattr(self, attribute):
            setattr(self, attribute, new_value)
            print(f"Atrybut {attribute} został zaktualizowany.")
        else:
            print(f"Atrybut {attribute} nie istnieje.")

    def __str__(self):
        return f"Watch({self.kod_produktu})"

