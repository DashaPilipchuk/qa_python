from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_book_genre_len_more_than_40(self):
        collector = BooksCollector()
        book_name = 'Жареные зеленые помидоры в кафе "Полустанок"'
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_same_book_twice(self):
        collector = BooksCollector()
        book_name = 'Маленький принц'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', 'Комедии')
        books_specific_genre = collector.get_books_with_specific_genre('Комедии')
        assert 'Форест Гамп' in books_specific_genre

    def test_get_books_for_children(self):
        collector = BooksCollector()
        book_name = 'Паровозик'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert book_name in books_for_children

    def test_get_books_not_for_children(self):
        collector = BooksCollector()
        book_name = 'Оно'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert book_name not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Детство'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Юность'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()






