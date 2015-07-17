from fanstatic import Library, Resource

library = Library('leaflet', 'resources')

leaflet_css = Resource(
    library,
    'leaflet.css',
    minified='leaflet.min.css',
    minifier='cssmin'
)

leaflet = Resource(
    library,
    'leaflet-src.js',
    minified='leaflet.js',
    minifier=None,
    bottom=True,
    depends=(leaflet_css,)
)
