=========
 Message
=========

Introduction
------------

Message is a collection of projects for building websites.  It is
currently under heavy development.

* Message DB: a versioned datastore for structured content.

* Message Admin: an intuitive, framework-agnostic
  administration. interface

Installation
------------

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


