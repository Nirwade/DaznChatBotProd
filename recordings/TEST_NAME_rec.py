from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_base(self):
        self.open("https://stag.dazn.com/")
        self.click("div#root > div > div > div")
        self.click("button#onetrust-accept-btn-handler")
        self.click("button#HEADER_SIGN_IN")
        self.type("input#email", "Shassh020399+TestGDE@gmail.com")
        self.type("input#password", "12345a")
        self.click('button[data-test-id="signIn__BUTTON"]')
        self.click('a:contains("HELP")')
        self.open("https://daznsupport1705599165.zendesk.com/hc/en-de")
        self.switch_to_frame("iframe#ada-button-frame")
