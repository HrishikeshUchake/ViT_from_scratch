import nbformat

nb = nbformat.read("fixed_maybe.ipynb", as_version=nbformat.NO_CONVERT)

nb.metadata.pop("widgets", None)

nbformat.write(nb, "notebook.ipynb")
