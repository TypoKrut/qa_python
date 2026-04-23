import pytest
from main import BooksCollector


def _check_genre_result(collector, book, expected_genre):

        if expected_genre is None:
            return book not in collector.books_genre
        else:
            return collector.get_book_genre(book) == expected_genre
        

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize('book,genre,expected_genre', [
        ('Алхимик', 'Фантастика', 'Фантастика'),
        ('Алхимик', 'Поэзия', ''),
        ('Несуществующая', 'Фантастика', None)
    ])

    def test_set_books_genre_set_genre(self, book, genre, expected_genre):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.set_book_genre(book, genre)

        assert _check_genre_result(collector, book, expected_genre)
    

    def test_get_book_genre_get_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.set_book_genre('Алхимик', 'Фантастика')

        assert collector.get_book_genre('Алхимик') == 'Фантастика'


    def test_get_books_with_specific_genre_get_books(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.set_book_genre('Алхимик', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Алхимик']


    def test_get_books_genre_get_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Алхимик', 'Фантастика')

        assert collector.get_books_genre() == {'Алхимик': 'Фантастика', 'Смешарики': ''}


    @pytest.mark.parametrize('books_data,expected', [
        ([('Смешарики', 'Мультфильмы'), ('Гуливер', 'Комедии')], ['Смешарики', 'Гуливер']),
        ([('Оно', 'Ужасы'), ('Шерлок', 'Детективы')], [])
    ])


    def test_get_books_for_children_get_for_children(self, books_data, expected):

        collector = BooksCollector()

        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == expected
    

    def test_add_book_in_favorites_add_book(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.add_book_in_favorites('Алхимик')

        assert collector.get_list_of_favorites_books() == ['Алхимик']
       

    def test_delete_book_from_favorites_delete_book(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.add_book_in_favorites('Алхимик')
        collector.delete_book_from_favorites('Алхимик')

        assert len(collector.favorites) == 0


    def test_get_list_of_favorites_books_get_list(self):

        collector = BooksCollector()

        collector.add_new_book('Алхимик')
        collector.add_new_book('Смешарики')
        collector.add_book_in_favorites('Алхимик')
        collector.add_book_in_favorites('Смешарики')

        assert collector.get_list_of_favorites_books() == ['Алхимик', 'Смешарики']
