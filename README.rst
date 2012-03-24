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

**This package is in an alpha stage, don't use it in production. I will hopefully
provide a more stable version very soon.**

I created the project because i didn't want to have to modify my cms installation
by adding templates or app_hooks for displaying rich visualizations such as
Openlayers Maps or jQplot charts.
Another use of the plugin is overriding some css in a particular cms page.


Implemented Features
--------------------

current version:0.0.2

* FragmentCollection and Fragment models, with admin integration
* FragmentPlugin and FragmentCollectionPlugin for django-cms
* css fragments from files, url or inline code
* js fragments from files, url or inline code
* html fragments from files or inline code
* integration with EditArea by Christophe Dolivet
* ordering of elements in a FragmentCollection


RoadMap/Planned Features
------------------------

planned version:0.1.0

* example fixtures for FragmentCollection and Fragment models
* live examples
* drag and drop ordering in admin
* better integration of EditArea
* write docs


Installation
------------

* Install via pip:

    pip install django-cms-fragments


* Add 'cms_fragments' to your INSTALLED_APPS
* Use 'django.contrib.staticfiles', or copy the static subfolder of django-cms-fragments
  to your static folder

...


Usage
-----

To use the plugin, you must create some Fragment or FragmentCollection instances with the Django admin.
FragmentCollections are a collection of Fragments.
Once you have one or more Fragments or FragmentCollections in the DB, you can choose which one to put in a
plugin, with the usual django-cms interface.
...


Compatibility
-------------

The app is being developed for Django >= 1.3.1. I'm not checking compatibility with other
Django versions right now.


Credits
-------

The project borrows from the following other codebases:

* Django-EditArea copyright (c) Aditya Bhargava
* EditArea copyright (c) Christophe Dolivet

