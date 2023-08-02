# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Sistemas UFU'
copyright = '2023, CTIC'
author = 'CTIC-UFU'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

new_supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# construct it this way so that if Sphinx adds default support for additional images, such
# as HEIC, then what we do is add any of those to the end. We start with the ones
# we want to support in this order, then subtract them from the defaults to identify
# any remaining items that we append to the end of the list

additional_default_supported_images = list(set(StandaloneHTMLBuilder.supported_image_types) - set(new_supported_image_types))
StandaloneHTMLBuilder.supported_image_types = new_supported_image_types + additional_default_supported_images