Papis-dmenu
===========

|Pypi| |RTD| |Python| |TRAVIS|

::

    If you use this plugin and you would like to
    MAINTAIN it, send us an email, we're looking for an active maintainer.


This project implements a picker based on
`dmenu <https://tools.suckless.org/dmenu/>`_
for papis.

Usage
-----

Just use it as a
`picktool <https://papis.readthedocs.io/en/latest/configuration.html#config-settings-picktool>`_

::

  papis --set picktool dmenu open

Installation
------------

There is a version in PyPi

::

  pip3 install papis-dmenu

or

::

  sudo pip3 install papis-dmenu

TODO
----
- [ ] Gradually type the project
- [ ] Implement some more tests
- [ ] Document a bit


.. |TRAVIS| image:: https://travis-ci.org/papis/papis-dmenu.svg?branch=master
   :target: https://travis-ci.org/papis/papis-dmenu
.. |Python| image:: https://img.shields.io/badge/Python-3%2B-blue.svg
   :target: https://www.python.org
.. |Pypi| image:: https://badge.fury.io/py/papis-dmenu.svg
   :target: https://badge.fury.io/py/papis-dmenu
.. |RTD| image:: https://readthedocs.org/projects/papis-dmenu/badge/?version=latest
   :target: http://papis-dmenu.readthedocs.io/en/latest/?badge=latest
