""" Shows icons only for editors. """

# Zope
from Acquisition import aq_inner

# Plone
from plone.memoize.view import memoize
from Products.CMFCore.utils import getToolByName


def toLocalizedTime(self, time, long_format=None, time_only=None):
    """ Convert time to localized time """
    context = aq_inner(self.context)
    util = getToolByName(context, 'translation_service')
    return util.ulocalized_time(time, long_format, time_only, context=context,
                                domain='unknown_domain', request=self.request)