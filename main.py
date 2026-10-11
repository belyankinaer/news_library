from author import Author
from site import Site

first_author = Author("Ваня", "ivan")
second_author = Author("Петя", "petya")
first_site = Site('Новостной сайт')

first_site.run()

first_site.register_author(first_author, '1234')
first_site.register_author(second_author, '5678')

user = first_site.login_author("ivan", "1234")
if user is not None:
    a1 = user.write_article('Очень интересная статья', 'Текст первой')
    first_site.add_article(a1, user)

print('\nНеверный вход:')
user = first_site.login_author("ivan", "wrong")

print('\nВход под Петей:')
user = first_site.login_author("petya", "5678")
if user is not None:
    a2 = user.write_article('Статья Пети', 'Текст второй')
    first_site.add_article(a2, user)

first_site.get_articles()

second_site = Site('Блог про технологи')
second_site.run()

second_site.register_author(first_author, '1234')

user = second_site.login_author("ivan", "1234")
if user is not None:
    a3 = user.write_article('Третья статья', 'Текст третьей')
    second_site.add_article(a3, user)

second_site.get_articles()

first_site.down()
second_site.down()
