django-cms-jsapp
=================

django-cms-jsapp is a plugin for django-cms.
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

* JsApp and JsAppFile models, with admin integration
* css fragments from files, url or inline code
* js fragments from files, url or inline code
* html fragments from files or inline code
* integration with EditArea by Christophe Dolivet
* ordering of elements in a JsApp


RoadMap/Planned Features
------------------------

planned version:0.1.0

* example fixtures for JsApp and JsAppFile models
* live examples
* drag and drop ordering in admin
* better integration of EditArea
* write docs


Installation
------------

* Add 'cms_jsapp' to your INSTALLED_APPS
* Use 'django.contrib.staticfiles', or copy the static subfolder of django-cms-jsapp
  to your static folder

...


Usage
-----

To use the plugin, you must create some JsApp instances with the Django admin.
JsApps are a collection of JsAppFiles.
Once you have one or more JsApps in the DB, you can choose which one to put in a
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

