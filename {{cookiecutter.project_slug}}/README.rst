{{ "=" * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|length }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Supported Python Versions

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Build Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest
        :alt: Documentation Status


{{ cookiecutter.project_short_description}}

* Free software: MIT license
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.org.

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `ulope/cookiecutter-pycli`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`ulope/cookiecutter-pycli`: https://github.com/ulope/cookiecutter-pycli
