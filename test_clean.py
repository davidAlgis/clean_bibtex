import pytest
from clean_bibtex import extract_citations, clean_bib_file


def test_extract_citations():
  tex_content = r"""
    This is a sample text with citations \cite{ref1, ref2} and \citeA{ref3}.
    Another citation \cite{ref4} and an empty one \cite{}.
    """
  expected_citations = {'ref1', 'ref2', 'ref3', 'ref4'}
  assert extract_citations(tex_content) == expected_citations


def test_clean_bib_file():
  bib_content = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    @article{ref2,
      author = {Author Two},
      title = {Title Two},
      journal = {Journal Two},
      year = {2022},
    }
    """
  citations = {'ref1'}
  expected_cleaned_bib = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    """
  assert clean_bib_file(bib_content,
                        citations).strip() == expected_cleaned_bib.strip()


def test_clean_bib_file_no_citations():
  bib_content = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    """
  citations = set()
  expected_cleaned_bib = ""
  assert clean_bib_file(bib_content,
                        citations).strip() == expected_cleaned_bib.strip()


def test_clean_bib_file_all_citations():
  bib_content = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    @article{ref2,
      author = {Author Two},
      title = {Title Two},
      journal = {Journal Two},
      year = {2022},
    }
    """
  citations = {'ref1', 'ref2'}
  expected_cleaned_bib = bib_content.strip()
  assert clean_bib_file(bib_content, citations).strip() == expected_cleaned_bib


def test_clean_bib_file_mixed_citations():
  bib_content = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    @article{ref2,
      author = {Author Two},
      title = {Title Two},
      journal = {Journal Two},
      year = {2022},
    }
    @article{ref3,
      author = {Author Three},
      title = {Title Three},
      journal = {Journal Three},
      year = {2023},
    }
    """
  citations = {'ref1', 'ref3'}
  expected_cleaned_bib = """
    @article{ref1,
      author = {Author One},
      title = {Title One},
      journal = {Journal One},
      year = {2021},
    }
    @article{ref3,
      author = {Author Three},
      title = {Title Three},
      journal = {Journal Three},
      year = {2023},
    }
    """
  assert clean_bib_file(bib_content,
                        citations).strip() == expected_cleaned_bib.strip()
