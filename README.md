# qa_python
1. Тест на добавление 2 новых книг в словарь без указания жанра:
test_add_new_book_add_two_books
2. Тест на невозможность добавления книги с именем более 40 символов:
test_add_book_genre_len_more_than_40
3. Тест на невозможность добавления 2 книг с одинаковым именем:
test_add_same_book_twice 
4. Тест на установку жанра книги, если книга есть в books_genre и ее жанр входит в список genre:
test_set_book_genre
5. Тест на вывод списка книг с определенным жанром:
test_get_books_with_specific_genre
6. Тест на получение списка книг, подходящих для детей:
test_get_books_for_children
7. Тест на получение списка книг, не подходящих для детей:
test_get_books_not_for_children
8. Тест на добавление книги в избранное:
test_add_book_in_favorites
9. Тест на удаление книги из избранного:
test_delete_book_from_favorites