django-cms-fragments
====================

django-cms-fragments is a plugin for django-cms.
With this plugin you can include several fragments of js, css and html in the
context of a cms page.
Fragments can be added by uploading a file, providing an external url(for js and css),
or writing inline code.

The plugin basically adds jss and js to the page, using sekizai tags.
It relies on the fact that django-cms requires "js" and "css" blocks to work.
The html fragments are rendered within the plugin template.

**This package is in an alpha stage, don't use it in production.**

I created the project because i didn't want to have to modify my cms installation
by adding templates or app_hooks for displaying rich visualizations such as
Openlayers Maps or jQplot charts.
Another use of the plugin is overriding some css in a particular cms page.

Installation
------------

* Install via pip:

    pip install django-cms-fragments

* Add 'cms_fragments' to your INSTALLED_APPS
* Use 'django.contrib.staticfiles', or copy the static subfolder of django-cms-fragments
  to your static folder

=====
Usage
=====

Fragments
---------



FragmentsBlocks
---------------

TBW
A "fragment block is"


Regions
---------------

TBW
Regions must be declared in your settings.py, with the CMS_FRAGMENTS_REGIONS setting.





To use the plugin, you must create some Fragment or FragmentCollection instances with the Django admin.
FragmentCollections are a collection of Fragments.
Once you have one or more Fragments or FragmentCollections in the DB, you can choose which one to put in a
plugin, with the usual django-cms interface.
...

Implemented Features
--------------------

current version:0.0.5

* FragmentRegions an FragmentBlock
* FragmentCollection and Fragment models, with admin integration
* FragmentPlugin and FragmentCollectionPlugin for django-cms
* css fragments from files, url or inline code
* js fragments from files, url or inline code
* html fragments from files or inline code
* integration with ace editor
* ordering of elements in a FragmentCollection
* ...

RoadMap/Planned Features
------------------------

planned version:0.1.0

* example fixtures for FragmentCollection and Fragment models
* live examples
* drag and drop ordering in admin
* write docs
* separate models for css, js and HTML fragments


Release Notes
-------------

version 0.0.5:

* Introduced FragmentRegions

version 0.0.4:

* Using ace editor instead of editarea
* Partial documentation at readthedocs.org

Compatibility
-------------

The app is being developed for Django >= 1.3.1. I'm not checking compatibility with other
Django versions right now.

Credits
-------

The project borrows from the following other codebases:

* ace editor by ajax.org. The ace license is included in the folder cms_fragments/static/acsjs/LICENSE

