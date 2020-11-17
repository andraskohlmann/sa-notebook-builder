import os

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
