""" Generic setup profiles setuphandlers. """


# Python
import string, logging

# Zope
from zope.interface import alsoProvides
from zope.component import getUtility, getMultiAdapter

# Plone
from plone.portlets.interfaces import IPortletManager, \
    IPortletAssignmentMapping, ILocalPortletAssignmentManager
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.app.portlets.portlets import navigation
from Products.CMFPlone.utils import _createObjectByType
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.lib import constraintypes
from Products.PortalTransforms.transforms.pdf_to_text import pdf_to_text 
#from Products.TinyMCE.interfaces.utility import ITinyMCE

# local
from younglives.policy.site_structure import STRUCTURE


logger = logging.getLogger('younglives.policy-setup')


def defaultStep(context):
    if not context.readDataFile('younglives.policy-default.txt'):
        return
    
    setupPortalTransformations(context)
    
    
def importStep(context):
    if not context.readDataFile('younglives.policy-import.txt'):
        return
    
    site = context.getSite()
    
    clearUpSite(site)
    for item in STRUCTURE: 
        createFolder(site,item)
    
    

def clearUpSite(context):
    """ Removes default portal content.  """
    
    existing = context.objectIds()    
    
    # Hide members area
    if 'Members' in existing:
        folder = context['Members']
        folder.setExcludeFromNav(True)
        folder.reindexObject()
        
    logger.info('clearUpSite: hides Members')
           
    if 'news' in existing:
        context.manage_delObjects(['news'])
        
    if 'events' in existing:
        context.manage_delObjects(['events'])
    
    # Remove front page
    if 'front-page' in existing:
        context.manage_delObjects(['front-page'])
        
    logger.info('clearUpSite: removes news, events, front-page')
    
    
def setupPortalTransformations(context): 
    """ Adds pdf-to-text transformation for pdf indexing. """
    
    site = context.getSite()
    pt = getToolByName(site, 'portal_transforms')
    pt.registerTransform(pdf_to_text())
    logger.info("setupPortalTransformations: pdf_to_text registered")
    

#===============================================================================
# helper methods 
#===============================================================================
    
def createFolder(context,item):
    if item['id'] not in context.objectIds():
        _createObjectByType(item['type'], context, 
            id=item['id'],
            title=item['title'])
    
        obj = context[item['id']]
    else:
        return
        #obj = context[item['id']]
    
    ## interfaces
    mark_ifs = item.get('interfaces')
    if mark_ifs:
        for mark_if in mark_ifs:
            alsoProvides(obj, mark_if)      

    ## portlets
    portlets = item.get('portlets')
    if portlets:
        rightcol = getUtility(IPortletManager, 
                              name = u'plone.rightcolumn')
        right = getMultiAdapter((obj, rightcol,), 
                                IPortletAssignmentMapping, 
                                context = obj)
    
        for portlet in portlets:
            if portlet.__name__ not in right:
                portlet_obj = portlet.Assignment()
                right[portlet.__name__] = portlet_obj
    
    ## navigation
    nav = item.get('navigation')
    if nav:
        leftcol = getUtility(IPortletManager, name = u'plone.leftcolumn')
        left = getMultiAdapter((obj, leftcol,), 
                                IPortletAssignmentMapping, 
                                context = obj)
    
        if navigation.__name__ not in left:
            navigation_obj = navigation.Assignment(**nav)
            left[navigation.__name__] = navigation_obj
                

    block = item.get('block-portlets')
    if block is not None:
        rightcol = getUtility(IPortletManager, 
                              name = u'plone.rightcolumn')

        assignable = getMultiAdapter((obj, rightcol), ILocalPortletAssignmentManager)
        assignable.setBlacklistStatus(CONTEXT_CATEGORY, block)
            
    ## local constraints
    allowed_types = item.get('allowed_types')
    if allowed_types is not None:
        obj.setConstrainTypesMode(constraintypes.ENABLED)
        obj.setLocallyAllowedTypes(allowed_types)
        obj.setImmediatelyAddableTypes(allowed_types)
     
    ## workflow transition    
    transition = item.get('transition')
    if transition:
        workflow = obj.portal_workflow
        workflow.doActionFor(obj, transition)
        
    obj.processForm() # finishes creation
        
    subfolder = item.get('subfolder')
    
    logger.info("createFolder: %s [%s]" % (obj.title,obj.id))
    
    if subfolder:
        for item in subfolder:
            createFolder(obj, item)