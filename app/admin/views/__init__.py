from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from app.admin.views.forms import BookForm, AuthorForm, GenreForm
from app.models import Book, Author, Genre

admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')


@admin.before_request
@login_required
def interceptor():
    pass


@admin.route('/')
def dashboard():
    _author = Author.query.all()
    _book = Book.query.all()
    _genre = Genre.query.all()
    _by_year = Book.query.group_by()
    return render_template('admin/dashboard.html', _author=_author, _book=_book, _genre=_genre)


@admin.route('/books', methods=['GET', 'POST'])
def book():
    _book = Book.query.all()

    return render_template('admin/book.html', title='book', book=_book)


@admin.route('/book/create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        _book = Book()
        form.populate_obj(_book)
        _book.save()
        return redirect(url_for('admin.book'))
    return render_template('admin/create-book.html', title='Create book', form=form)


@admin.route('/book/update/<int:pk>', methods=['GET', 'POST'])
def update_book(pk):
    _ = Book.query.get_or_404(pk)
    form = BookForm(obj=_)
    if form.validate_on_submit():
        form.populate_obj(_)
        _.save(message='Updated')
        return redirect(url_for('admin.book'))
    return render_template('admin/update-book.html', title='Update book', form=form)


@admin.route('/book/delete/<int:pk>', methods=['GET', 'POST'])
def delete_book(pk):
    _ = Book.query.get_or_404(pk)
    _.delete()
    return redirect(url_for('admin.book'))


##Authors

@admin.route('/author', methods=['GET', 'POST'])
def author():
    _author = Author.query.all()
    return render_template('admin/author.html', title='author', author=_author)


@admin.route('/author/create', methods=['GET', 'POST'])
def create_author():
    form = AuthorForm()
    if form.validate_on_submit():
        _ = Author()
        form.populate_obj(_)
        _.save()
        return redirect(url_for('admin.author'))
    return render_template('admin/create-author.html', title='Create author', form=form)


@admin.route('/author/update/<int:pk>', methods=['GET', 'POST'])
def update_author(pk):
    _ = Author.query.get_or_404(pk)
    form = AuthorForm(obj=_)
    if form.validate_on_submit():
        form.populate_obj(_)
        _.save(message='Updated')
        return redirect(url_for('admin.author'))
    return render_template('admin/update-author.html', title='Update author', form=form)


@admin.route('/author/delete/<int:pk>', methods=['GET', 'POST'])
def delete_author(pk):
    _ = Author.query.get_or_404(pk)
    _.delete()
    return redirect(url_for('admin.author'))


##Genre

@admin.route('/genre', methods=['GET', 'POST'])
def genre():
    _genre = Genre.query.all()
    return render_template('admin/genre.html', title='genre', genre=_genre)


@admin.route('/genre/create', methods=['GET', 'POST'])
def create_genre():
    form = GenreForm()
    if form.validate_on_submit():
        _ = Genre()
        form.populate_obj(_)
        _.save()
        return redirect(url_for('admin.genre'))
    return render_template('admin/create-genre.html', title='Create genre', form=form)


@admin.route('/genre/update/<int:pk>', methods=['GET', 'POST'])
def update_genre(pk):
    _ = Genre.query.get_or_404(pk)
    form = GenreForm(obj=_)
    if form.validate_on_submit():
        form.populate_obj(_)
        _.save(message='Updated')
        return redirect(url_for('admin.genre'))
    return render_template('admin/update-genre.html', title='Update genre', form=form)


@admin.route('/genre/delete/<int:pk>', methods=['GET', 'POST'])
def delete_genre(pk):
    _ = Genre.query.get_or_404(pk)
    _.delete()
    return redirect(url_for('admin.genre'))
