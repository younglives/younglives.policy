from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from younglives.policy.config import PROJECTNAME


class TestCase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import Products.OrderableReferenceField
        self.loadZCML(package=Products.OrderableReferenceField)
        import younglives.content
        self.loadZCML(package=younglives.content)
        import younglives.homepage
        self.loadZCML(package=younglives.homepage)

        # Install product and call its initialize() function
        z2.installProduct(app, PROJECTNAME)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, '%s:default' % PROJECTNAME)

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, PROJECTNAME)

FIXTURE = TestCase()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="fixture:Integration")
