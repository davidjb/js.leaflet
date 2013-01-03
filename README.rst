js.leaflet
***********

Introduction
============

This library packages `Leaflet`_ for `fanstatic`_.

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

Updating this package
---------------------

This process requires installation of the package for development - the
suggested method to do this is via the `Buildout` within this package::

    cd js.leaflet
    python boostrap.py
    ./bin/buildout

For minification of resources to succeed, you require a Java installation as
this process uses the YUI Compressor library (via the ``minify``
and``yuicompressor`` Python packages).

In order to obtain a newer version of of this library, do the following 
(substituting the version number for the newer version)::

    pushd js/leaflet/resources
    wget https://github.com/CloudMade/Leaflet/tarball/v0.4.5 -O leaflet.tgz
    #Overwrites older files with new ones
    tar vxf leaflet.tgz --wildcards '*/dist' --strip=2
    rm leaflet.tgz
    popd
    #Edit changelog, setup.py for versions, etc
    python setup.py minify_leaflet
    git commit -a -m "Updated for release 0.4.5"
    git push

If you're doing this out in your own fork of the GitHub repository, then
send through a pull request so everyone can benefit.
