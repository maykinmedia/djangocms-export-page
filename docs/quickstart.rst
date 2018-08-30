==========
Quickstart
==========


Installation
============

Install from PyPI with pip:

.. code-block:: bash

    pip install djangocms-export-page


Usage
=====

In your Django settings:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'djangocms_export_page',
        ...
    ]



CMS Page
--------

CMS Page don't need any extra configuration to work.

If a Plugin has a ForeignKey that would behave like children,
add the following to the CMSPlugin model class:

.. code-block:: python

    _export_page = {
        'children': 'items'
    }

where `items` is a iterable attribute of the model class.

And for on the ForeignKey Django model class:

.. code-block:: python

    _export_page = {
        'fields': ['name', ... ]
    }


Django Model
------------

If you need to export a Django model included in a AppHook,
add the following to the model class:

.. code-block:: python

    _export_page = {
        'sections': [{
            'name': 'Meta',
            'fields': ['title', ... ]
        }, {
            'name': 'Body',
            'fields': ['content']
        }],
    }

It's better to put the PlaceholderField (here `content`) in a separate section.
