js.leaflet
***********

Introduction
============

This library packages the `Leaflet`_ JavaScript mapping library for
`fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`Leaflet`: http://leafletjs.com/

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.leaflet``) are published to some URL.  As a bonus, this
library also packages up minified versions of the original CSS resources.

Packaging
=========

The packaging is stored on GitHub at
https://github.com/davidjb/js.leaflet. If you happen to come across a bug
that corresponds to *packaging*, then please report it here. Pull requests are
more than welcome if you're fixing something yourself -- the more help the
better!

Any other bugs that relate to the library itself should be directed to the
original developers.

Development of this package
---------------------------

This process requires installation of the package for development - the
suggested method to do this is via the `Buildout` within this package::

    cd js.leaflet
    python boostrap.py
    ./bin/buildout

Running tests
-------------

After running the `Buildout` within this package, do this:

    ./bin/tox

...and watch the magic unfold.

Updating this package
---------------------

In order to obtain a newer version of this library, do the following 
(substituting the version number for the newer version)::

    pushd js/leaflet/resources
    wget https://github.com/Leaflet/Leaflet/archive/v0.6.2.tar.gz -O leaflet.tgz
    #Overwrites older files with new ones
    tar vxf leaflet.tgz --wildcards '*/dist' --strip=2
    rm leaflet.tgz
    popd
    #Edit changelog, setup.py for versions, etc here
    ./bin/fanstatic_compile -v js
    git add js
    git commit -a -m "Updated for release 0.6.2"
    git push

If you're doing this out in your own fork of the GitHub repository, then
send through a pull request so everyone can benefit from the updated 
library.
