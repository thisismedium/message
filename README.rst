=========
 Message
=========

Message is a collection of projects for building websites.

* `Message DB`_: a versioned datastore for structured content.

* `Message Admin`_: an intuitive, framework-agnostic
  administration interface

.. _`Message DB`: http://github.com/thisismedium/message-db
.. _`Message Admin`: http://github.com/thisismedium/message-admin

Develop
-------

Message is currently under active development.

To install Message, clone this repository and execute the ``run``
script::

  sudo easy_install virtualenv
  git clone git://github.com/thisismedium/message.git
  ./message/bin/run

The first time you ``run`` Message, it will create a virtualenv,
install third-party dependencies, and link in related projects.  The
layout looks like this::

  admin       # The message-admin project
  db          # The message-db project
  mdev        # A Message virtualenv
  more        # Related github projects
  .py         # Python packages that are linked into site-packages

Using Message
-------------

With the server running, visit http://localhost:5280/ in a browser.
