""" Makes new members fields available on the Personal Information form. """


# Plone
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """ Adds jobtitle. """
    
    def get_jobtitle(self):
        return self.context.getProperty('jobtitle', '')
    
    def set_jobtitle(self, value):
        return self.context.setMemberProperties({'jobtitle': value})
    
    phone = property(get_jobtitle, set_jobtitle)