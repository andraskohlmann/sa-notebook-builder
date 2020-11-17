import os
from unittest.mock import ANY

import nbconvert
import nbformat

from sa_notebook_builder.builder import Builder


def run_notebook(path):
    nb = nbformat.read(path, as_version=4)
    ep = nbconvert.preprocessors.ExecutePreprocessor()
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})


def test_builder_creates_ipynb_file(tmpdir):
    b = Builder()
    b.render(os.path.join(tmpdir, 'empty.ipynb'))

    assert os.path.isfile(os.path.join(tmpdir, 'empty.ipynb'))


def test_builder_creates_legit_ipynb(tmpdir):
    b = Builder()
    b.render(os.path.join(tmpdir, 'empty.ipynb'))

    run_notebook(os.path.join(tmpdir, 'empty.ipynb'))


def test_add_markdown_adds_markdown(tmpdir):
    b = Builder()
    md = """
        # Title
        ## Subtitle
        Text
    """
    filename = os.path.join(tmpdir, 'md.ipynb')

    b.add_markdown(md)
    b.render(filename)

    rendered_nb = nbformat.read(filename, as_version=4)
    assert len(rendered_nb.cells) == 1

    expected_cell = {
        "cell_type": "markdown",
        "metadata": ANY,
        "source": md,
    }
    assert rendered_nb.cells[0] == expected_cell
