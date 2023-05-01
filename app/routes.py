from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import *
from app.models import *
from simsearch import SimSearch

file_server = 'https://file.aichain.online/'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    simsearch = SimSearch()
    form = SearchForm()
    if form.validate_on_submit():
        results = simsearch.similar_search(form.search.data)
        showcases = [Showcase.query.filter_by(id=id).one() for id in results]
    else:
        showcases = Showcase.query.all()
    for showcase in showcases:
        showcase.description_short = showcase.description[:50] + ' ...'
    return render_template('marketplace_showcase.html', title='Market', showcases=showcases, form=form, file_prefix = file_server)
