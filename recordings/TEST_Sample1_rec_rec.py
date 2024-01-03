from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://www.dazn.com/en-GB/help")
        self.click("button#onetrust-accept-btn-handler")
        self.switch_to_frame("iframe#ada-button-frame")
        self.open("https://dazn.ada.support/embed/button/b0e29e3/index.html")
