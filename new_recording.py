from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://stag.dazn.com/en-IT/help")
        self.click("button#onetrust-accept-btn-handler")
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
        self.open("https://stag.dazn.com/en-IT/help")
        self.switch_to_frame("iframe#ada-button-frame")
        self.switch_to_parent_frame()
        self.switch_to_frame("iframe#ada-button-frame")
