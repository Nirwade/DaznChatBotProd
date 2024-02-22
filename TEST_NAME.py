from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_base(self):
        if self.recorder_ext and not self.xvfb:
            import pdb; pdb.set_trace()
