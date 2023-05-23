from app import db


class Watch(db.Model):
    __tablename__ = 'watches'

    id = db.Column(db.Integer, primary_key=True)
    kod_produktu = db.Column(db.String(50), unique=True, nullable=False)
    proba = db.Column(db.String(10), nullable=False)
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

    def __repr__(self):
        return f'<Watch {self.kod_produktu}>'
