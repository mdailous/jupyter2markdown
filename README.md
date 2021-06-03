# Jupyter Notebook to Markdown Converter

Python 3 script to convert a Jupyter Notebook file (`.ipynb`) file to a Markdown formatted file.

**NOTE**: Currently, only the Jupyter Notebook cell types `Markdown` and `Code` are implemented because those are the only cell types I use. If there is a need for any other cell types, update the code and submit a pull request, or [open an issue](https://github.com/mdailous/jupyter2markdown/issues/new) with the label set to `enhancement`.

### Requirements

- Python 3.4+.

### Usage

Converting a Jupyter Notebook to Markdown format is as simple as executing the following command:
```
python3 jn2md.py ~/notebooks/mynotebook.ipynb
```

Then sit back and let the magic happen. The generated markdown file is created with the same base name and placed in the same directory as the Jupyter notebook file. If something isn't working quite right, debug output can be enabled using the `--debug` switch. Inline help has been implemented using the `-h` flag.