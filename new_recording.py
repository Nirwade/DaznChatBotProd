from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://daznsupport1705599165.zendesk.com/hc/en-gb")
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.assert_element("body.community-enabled header")
        self.assert_element("body.community-enabled main")
        self.click("body.community-enabled main")
        self.click("body.community-enabled main")
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.click("body.community-enabled main")
        self.click("body.community-enabled main")
        self.double_click("body.community-enabled main")
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.click("body.community-enabled main")
        self.click("body.community-enabled main")
