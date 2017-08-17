from flask import render_template, request, redirect, url_for, session, flash
from app import app
from app.shoppinglistapp import ShoppingListApp
from app.crudfeatures import User
from app.crudfeatures import ShoppingList
from app.crudfeatures import ShoppingListItem

application = ShoppingListApp()


@app.route('/')
@app.route('/home')
def index():
    """
    This method returns the home page of the application
    :return:
    """
    return render_template('startpage.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    This method shows the user the sign up page. It also signs up a user
    if all the required attributes are present and then redirects the
    user to their shopping list
    :return:
    """
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['username'] and request.form['password'] \
                and request.form['password-confirmation']:

            if request.form['password'] == request.form['password-confirmation']:
                user = User(request.form['username'], request.form['password'], request.form['name'])
                if application.register_user(user):
                    flash("You have successfully signed up. Please Login")
                    return redirect(url_for('login'))
                return render_template('signup.html', error="You are already signed up, please login")
            error = 'The passwords do not match'

    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This method logins in an already existing user if their username and password
    match those already stored.
    It also shows errors to the user if their password is wrong or they do not
    already have an account.
    :return:
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            if application.does_user_exist(request.form['username']):
                if application.login_user(request.form['username'], request.form['password']):
                    session['username'] = request.form['username']
                    return redirect(url_for('homepage'))
                return render_template('LoginPage.html', error="Incorrect password")
            return render_template('LoginPage.html', error="No account found, please sign up first")
        error = "Invalid credentials, try again"
    return render_template('LoginPage.html', error=error)


@app.route('/shopping/list', methods=['GET', 'POST'])
def shoppinglists():
    """
    This method shows the user shopping lists.
    When its a Post request a shopping list is created
    and attached to the user. Then redirected back
    :return:
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('LoginPage'))
    if request.method == 'POST':
        name = request.form['name']
        if user.create_bucket(ShoppingList(application.generate_random_key(), name)):
            flash("You have successfully added a shopping list")
            return redirect(url_for('homepage'))
        error = "Could not create the Shopping List, it already exists"
    return render_template('homepage.html', error=error, shoppinglists=user.get_shoppinglist(), user=user)


@app.route('/edit/shoppinglist/<shoppinglist_id>', methods=['GET', 'POST'])
def editshoppinglist(shoppinglist_id):
    """
    This route enables a user to edit their shopping lists
    :param shoppinglist_id:
    :return:
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('LoginPage'))
    shoppinglist = user.get_shoppinglist(shoppinglist_id)
    if not shoppinglist:
        return redirect(url_for('homepage'))
    if request.method == 'POST':
        if request.form['name']:
            if user.update_shoppinglist(shoppinglist_id, request.form['name']):
                flash("You have successfully updated your Shopping list")
                return redirect(url_for('homepage'))
        error = "Please provide the shopping list name"
    return render_template('editshoppinglist.html', error=error, bucket=shoppinglist, user=user)


@app.route('/delete/shoppinglist/<shoppinglist_id>', methods=['GET', 'POST'])
def deleteshoppinglist(shoppinglist_id):
    """
    This route enables a user to delete a shopping list
    :param shoppinglist_id:
    :return:
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('LoginPage'))
    shoppinglist = user.get_shoppinglist(shoppinglist_id)
    if not shoppinglist:
        return redirect(url_for('homepage'))

    if request.method == 'POST':
        if user.delete_shoppinglist(shoppinglist_id):
            flash("You have successfully deleted a shopping list")
            return redirect(url_for('homepage'))
        error = "Could not delete the shopping list"
    return render_template('deleteshoppinglist.html', error=error, shoppinglist=shoppinglist, user=user)


@app.route('/shoppinglist/items/<shoppinglist_id>', methods=['GET', 'POST'])
def shoppinglistitems(shoppinglist_id):
    """
    Route to show and create shopping list items.
    :param shoppinglist_id:
    :return:
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('LoginPage'))
    shoppinglist = user.get_shoppinglist(shoppinglist_id)
    if not shoppinglist:
        return redirect(url_for('homepage'))

    if request.method == 'POST':
        if request.form['name']:
            if shoppinglist.create_item(
                    ShoppingListItem(application.generate_random_key(), request.form['name'])):
                flash("You have successfully added an Item to the shoppinglist")
                return redirect(url_for('shoppinglistitem', shoppinglist_id=shoppinglist.id))
        error = "Item cannot be created"
    return render_template('shoppinglistitem.html', error=error, shoppinglist=shoppinglist, user=user)


@app.route('/shopping/item/<shoppinglist_id>/<item_id>', methods=['GET', 'POST'])
def edititem(shoppinglist_id, item_id):
    """
    Route to edit an item specified by the Id
    :param shoppinglist_id:
    :param item_id:
    :return:
    """
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    shoppinglist = user.get_shoppinglist(shoppinglist_id)
    item = shoppinglist.get_item(item_id)
    if not shoppinglist and not item:
        return redirect(url_for('homepage'))

    if request.method == 'POST':
        if request.form['name'] and request.form['quantity']:
            if shoppinglist.update_item(item_id, request.form['name'], request.form['quantity']):
                flash("You have successfully updated your Item in the Bucket")
                return redirect(url_for('shoppinglistitem', shoppinglist_id=shoppinglist.id))
    return render_template('editshoppinglistitem.html', shoppinglist=shoppinglist, item=item, user=user)


@app.route('/shoppinglist/item/delete/<shoppinglist_id>/<item_id>', methods=['GET', 'POST'])
def deleteitem(shoppinglist_id, item_id):
    """
    Route to delete an item from a shopping list specified by the Id.
    :param shoppinglist_id:
    :param item_id:
    :return:
    """
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    shoppinglist = user.get_shoppinglist(shoppinglist_id)
    item = shoppinglist.get_item(item_id)
    if not shoppinglist and not item:
        return redirect(url_for('homepage'))

    if request.method == 'POST':
        if shoppinglist.delete_item(item_id):
            flash('You have successfully deleted an Item from the shopping list')
            return redirect(url_for('shoppinglistitem', shoppinglist_id=shoppinglist.id))
    return render_template('deleteitem.html', user=user, shoppinglist=shoppinglist, item=item)


@app.route('/logout')
def logout():
    """
    This methods clears the user session and logs the user out
    :return:
    """
    session.pop('username', None)
    return redirect(url_for('login'))
