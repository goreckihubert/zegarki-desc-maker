from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length


class AddWatchForm(FlaskForm):
    kod_produktu = StringField('Kod produktu', validators=[DataRequired()])
    proba = StringField('Próba', validators=[DataRequired()])
    grawer = TextAreaField('Grawer')
    dla_kogo = StringField('Dla kogo', validators=[DataRequired()])
    rodzaj = StringField('Rodzaj', validators=[DataRequired()])
    styl = StringField('Styl', validators=[DataRequired()])
    pochodzenie = StringField('Pochodzenie', validators=[DataRequired()])
    szkiełko = StringField('Szkiełko', validators=[DataRequired()])
    rodzaj_koperty = StringField('Rodzaj koperty', validators=[DataRequired()])
    szerokosc_koperty = FloatField('Szerokość koperty', validators=[DataRequired()])
    grubosc_koperty = FloatField('Grubość koperty', validators=[DataRequired()])
    typ_paska_bransolety = StringField('Typ paska/bransolety', validators=[DataRequired()])
    kolor_paska_bransolety = StringField('Kolor paska/bransolety', validators=[DataRequired()])
    wodoszczelnosc = StringField('Wodoszczelność', validators=[DataRequired()])
    mechanizm = StringField('Mechanizm', validators=[DataRequired()])
    gwarancja = StringField('Gwarancja', validators=[DataRequired()])
    kolor_tarczy = StringField('Kolor tarczy', validators=[DataRequired()])


class EditWatchForm(FlaskForm):
    grawer = TextAreaField('Grawer')
    dla_kogo = StringField('Dla kogo', validators=[DataRequired()])
    rodzaj = StringField('Rodzaj', validators=[DataRequired()])
    styl = StringField('Styl', validators=[DataRequired()])
    pochodzenie = StringField('Pochodzenie', validators=[DataRequired()])
    szkiełko = StringField('Szkiełko', validators=[DataRequired()])
    rodzaj_koperty = StringField('Rodzaj koperty', validators=[DataRequired()])
    szerokosc_koperty = FloatField('Szerokość koperty', validators=[DataRequired()])
    grubosc_koperty = FloatField('Grubość koperty', validators=[DataRequired()])
    typ_paska_bransolety = StringField('Typ paska/bransolety', validators=[DataRequired()])
    kolor_paska_bransolety = StringField('Kolor paska/bransolety', validators=[DataRequired()])
    wodoszczelnosc = StringField('Wodoszczelność', validators=[DataRequired()])
    mechanizm = StringField('Mechanizm', validators=[DataRequired()])
    gwarancja = StringField('Gwarancja', validators=[DataRequired()])
    kolor_tarczy = StringField('Kolor tarczy', validators=[DataRequired()])
