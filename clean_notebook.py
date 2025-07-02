import nbformat

nb = nbformat.read("ViT_from_scratch.ipynb", as_version=nbformat.NO_CONVERT)

nb.metadata.pop("widgets", None)

nbformat.write(nb, "notebook.ipynb")
