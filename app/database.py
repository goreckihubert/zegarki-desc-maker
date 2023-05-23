from app import db


class Watch(db.Model):
    __tablename__ = 'watches'

    id = db.Column(db.Integer, primary_key=True)
    kod_produktu = db.Column(db.String(50), unique=True, nullable=False)
    proba = db.Column(db.String(20))
    grawer = db.Column(db.String(100))
    dla_kogo = db.Column(db.String(50))
    rodzaj = db.Column(db.String(50))
    styl = db.Column(db.String(50))
    pochodzenie = db.Column(db.String(50))
    szkiełko = db.Column(db.String(50))
    rodzaj_koperty = db.Column(db.String(50))
    szerokosc_koperty = db.Column(db.Float)
    grubosc_koperty = db.Column(db.Float)
    typ_paska_bransolety = db.Column(db.String(50))
    kolor_paska_bransolety = db.Column(db.String(50))
    wodoszczelnosc = db.Column(db.String(50))
    mechanizm = db.Column(db.String(50))
    gwarancja = db.Column(db.String(50))
    kolor_tarczy = db.Column(db.String(50))

    def __init__(self, kod_produktu, proba, grawer, dla_kogo, rodzaj, styl, pochodzenie,
                 szkiełko, rodzaj_koperty, szerokosc_koperty, grubosc_koperty,
                 typ_paska_bransolety, kolor_paska_bransolety, wodoszczelnosc,
                 mechanizm, gwarancja, kolor_tarczy):
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
