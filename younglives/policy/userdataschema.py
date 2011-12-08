""" Adding fields to members data schema. """


# Zope
from zope import schema
from zope.interface import implements

# Plone
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

# local
from younglives.policy.i18n import younglivesMessageFactory as _


# overrides default schema provider
class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema
    

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Adds jobtitle. """
    
    phone = schema.TextLine(title = _(u'user_jobtitle_label', default=u'Job Title'),
        description = _(u'member_jobtitle_description',
                        default=u"Enter your Job Title."),
        required = False)