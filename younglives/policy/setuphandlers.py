import logging
from zope.app.component.hooks import getSite
from zope.interface import alsoProvides, noLongerProvides

from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

from younglives.content.interfaces.content import IGalleryContainerAware
from younglives.content.interfaces.content import IQuoteAware

def importVarious(context):
    """
    Import various settings."""
    # Only run step if a flag file is present
    if context.readDataFile('younglives.policy.txt') is None:
        return
    site = context.getSite()
    out = StringIO()

    catalog = getToolByName(getSite(), 'portal_catalog')
    items = catalog.searchResults({'object_provides':'IGalleryContainerAware.__identifier__',})
    for item in items:
        object = item.getObject()
        noLongerProvides(object, IGalleryContainerAware)
        object.reindexObject()
    items = catalog.searchResults({'object_provides':'IQuoteAware.__identifier__',})
    for item in items:
        object = item.getObject()
        noLongerProvides(object, IQuoteAware)
        object.reindexObject()
