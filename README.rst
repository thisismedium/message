=========
 Message
=========

Introduction
------------

Message is a collection of projects for building websites.

* ``Message DB``_: a versioned datastore for structured content.

* ``Message Admin``_: an intuitive, framework-agnostic
  administration. interface

.. _``Message DB``: https://github.com/thisismedium/message-db
.. _``Message Admin``: https://github.com/thisismedium/message-admin

Develop
-------

Message is currently under active development.

We recommend installing Message into a virtual environment.  If you do
not want to use ``virtualenv``, skip this step.  To set up an empty
environment::

  sudo easy_install virtualenv
  virtualenv --no-site-packages message-dev
  . message-dev/bin/activate

To install Message, clone this repository and execute the ``run``
script::

  git clone git://github.com/thisismedium/message.git
  cd message
  ./bin/run

Using Message
-------------

With the server running, visit http://localhost:5280/ in a browser.


