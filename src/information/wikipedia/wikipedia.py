import wikipediaapi
from testVocab import run_time_text


def get_summary(url):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(url)
    print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True

    page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
    print("Page - Exists: %s" % page_missing.exists())
    # Page - Exists: False

    print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %s" % page_py.summary[0:200])

    # Page - Summary: Python is a widely used high-level programming language for