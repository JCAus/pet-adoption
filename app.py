from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import Add_Pet_Form, Edit_Pet_Form


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def list_pets():
    """Show all the pets up for adoption"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route('/pets/<int:pet_id>')
def show_pet(pet_id):
    """Show a specific pets profile"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_profile.html", pet=pet)

@app.route('/add_pet', methods=["GET", "POST"])
def add_pet():
    """Add a pet to the adoption list"""
    form = Add_Pet_Form()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} has been added!")
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pets profile"""
    pet = Pet.query.get_or_404(pet_id)
    form = Edit_Pet_Form(obj=pet)
    

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been updated!")

        return redirect('/')
    else:
        return render_template("edit_pet.html", form=form, pet=pet)

    


