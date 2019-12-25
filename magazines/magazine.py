
import os
import tempfile
from newspaper import Article
from ebooklib import epub


def generete_epub(article_urls, magazine_title, magazine_key):
    book = epub.EpubBook()

    book.set_identifier(magazine_key)
    book.set_title(magazine_title)
    book.spine = ['nav']

    for index, url in enumerate(article_urls):
        article = Article(url)
        article.download()
        article.parse()

        chapter = epub.EpubHtml(title=article.title,
                                file_name=f'chap_{index}.xhtml')
        chapter.set_content(article.text)
        book.add_item(epub.EpubHtml(content=f'<h1>{article.title}</h1>'))
        book.add_item(chapter)
        book.toc.append(epub.Link(chapter.file_name,
                                  chapter.title, chapter.get_id()))
        book.spine.append(chapter)

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book_path = os.path.join(tempfile.gettempdir(), f'{magazine_key}.epub')

    epub.write_epub(book_path, book)

    return book_path
