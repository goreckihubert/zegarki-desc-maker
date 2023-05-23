from flask import render_template, redirect, url_for
from app import app, db
from app.forms import AddWatchForm, EditWatchForm
from app.models import Watch


@app.route('/')
def index():
    watches = Watch.query.all()
    return render_template('index.html', watches=watches)


@app.route('/add_watch', methods=['GET', 'POST'])
def add_watch():
    form = AddWatchForm()
    if form.validate_on_submit():
        watch = Watch(
            kod_produktu=form.kod_produktu.data,
            proba=form.proba.data,
            grawer=form.grawer.data,
            dla_kogo=form.dla_kogo.data,
            rodzaj=form.rodzaj.data,
            styl=form.styl.data,
            pochodzenie=form.pochodzenie.data,
            szkiełko=form.szkiełko.data,
            rodzaj_koperty=form.rodzaj_koperty.data,
            szerokosc_koperty=form.szerokosc_koperty.data,
            grubosc_koperty=form.grubosc_koperty.data,
            typ_paska_bransolety=form.typ_paska_bransolety.data,
            kolor_paska_bransolety=form.kolor_paska_bransolety.data,
            wodoszczelnosc=form.wodoszczelnosc.data,
            mechanizm=form.mechanizm.data,
            gwarancja=form.gwarancja.data,
            kolor_tarczy=form.kolor_tarczy.data
        )
        db.session.add(watch)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_watch.html', form=form)


@app.route('/edit_watch/<kod_produktu>', methods=['GET', 'POST'])
def edit_watch(kod_produktu):
    watch = Watch.query.get_or_404(kod_produktu)
    form = EditWatchForm(obj=watch)
    if form.validate_on_submit():
        form.populate_obj(watch)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_watch.html', form=form, kod_produktu=kod_produktu)


@app.route('/delete_watch/<kod_produktu>', methods=['POST'])
def delete_watch(kod_produktu):
    watch = Watch.query.get_or_404(kod_produktu)
    db.session.delete(watch)
    db.session.commit()
    return redirect(url_for('index'))
