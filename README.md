# mike-demo

Demo repository to setup mike.

<!-- vscode-markdown-toc -->
* 1. [Install](#Install)
* 2. [Snippets](#Snippets)
* 3. [Publishing Documentation](#PublishingDocumentation)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

---

##  1. <a name='Install'></a>Install

```console
# Install packages
poetry install

# Install pre-commit
pre-commit install
```

##  2. <a name='Snippets'></a>Snippets

```console
# Build a version and push to gh-pages branch
mike build <VERSION-TAG> <ALIAS> -p

# Set default version (Important to-be specified before `mike serve`)
mike set-default <VERSION-TAG>

# Serve the documentation locally
mike serve
```

## How-To

```console
# Create initial documentation
mkdocs new .

# Create first version and push
mike deploy 0.1.0 latest -p

# Set default version to "latest"
mike set-default latest

# Do some stuff
# ...

# Create new version, update the "latest" alias and push
mike deploy 0.2.0 latest --update-aliases -p
```

##  3. <a name='PublishingDocumentation'></a>Publishing Documentation

The documentation can be found [here](https://schernhe.github.io/mike-demo/0.1.0/). Note that the URL follows the schema `.../mike-demo/<VERSION>/` and is not accessible without the version name.

## Notes for Setting up Mike

- Mike does not create a new MKDocs project. This needs to-be setup manually.
- Mike does not include the material extras. This needs to-be added manually.
- MKDocs themes need to-be integrated with Mike (css / js).


## Credits
- https://github.com/jimporter/mike
- https://github.com/squidfunk/mkdocs-material-example-versioning
