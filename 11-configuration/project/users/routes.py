from . import users_blueprint
from flask import render_template, flash


# ------
# Routes
# ------

@users_blueprint.route('/about')
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template('users/about.html', company_name='saidulislam.com', pname='Saidul (c)')