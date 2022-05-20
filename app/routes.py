from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, CreateForm, DeleteForm
from app.models import Note



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    notes = Note.query.all()
    return render_template('index.html', title='Home', user=user, notes=notes)
    
@app.route('/get_list')
def get_list():
	notes = Note.query.all()
	notes_str = ''
	for note in notes:
		notes_str += note.name + '<///>'
	return notes_str
 
@app.route('/<note_name>')
def note(note_name):
	note = Note.query.filter_by(name=note_name).first_or_404()
	return render_template('note.html', title=note.name, name=note.name, text=note.text)

@app.route('/<note_name>/get')
def note_get(note_name):
	note = Note.query.filter_by(name=note_name).first_or_404()
	return note.name + 5 * '<///>' + note.text

@app.route('/edit_note/<note_name>', methods=['GET', 'POST'])
def edit(note_name):
	note = Note.query.filter_by(name=note_name).first_or_404()
	name1 = request.args.get('new_name', '')
	text1 = request.args.get('new_text', '')
	if name1 != '' and text1 != '':
		note.name = name1
		note.text = text1
		db.session.commit()
		return
	form = CreateForm()
	form2 = DeleteForm()
	if (form2.submit2.data and form2.validate()) or (request.args.get('deleted','') == 'yes'):
		db.session.delete(note)
		db.session.commit()
		return redirect(url_for('index'))
	if form.submit.data and form.validate():
		note.name = form.name.data
		note.text = form.text.data
		db.session.commit()
		return redirect('/'+note.name)
	elif request.method == 'GET':
		form.name.data = note.name
		form.text.data = note.text
	return render_template('editnote.html', title='Edit',form=form, name=note.name, text=note.text, form2=form2)

@app.route('/create_note', methods=['GET', 'POST'])
def create():
	name1 = request.args.get('name', '')
	text1 = request.args.get('text', '')
	if name1 != '' and text1 != '':
		note = Note(name=name1, text=text1)
		db.session.add(note)
		db.session.commit()
		return
	form = CreateForm()
	if form.validate_on_submit():
		note = Note(name=form.name.data, text=form.text.data)
		db.session.add(note)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('create.html', title='Create Note', form=form) 

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

