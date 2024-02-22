from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://daznsupport1705599165.zendesk.com/hc/en-gb")
        self.switch_to_frame("iframe#ada-button-frame")
