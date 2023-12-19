from page_objects.paywall_helpermethods import PayHelpers

class PaywallFlow(PayHelpers):

    def test_paywall_stag(self):
        self.user_signin_stag()
        self.accept_cookies_and_start_chat_stag()
        self.verify_greeting_stag()
        self.paywallflow1_stag()

    def test_paywall_stag1(self):
        self.user_signin_stag()
        self.accept_cookies_and_start_chat_stag()
        self.verify_greeting_stag()
        self.paywallflow2_stag()

    def test_paywall_stag2(self):
        self.user_signin_stag()
        self.accept_cookies_and_start_chat_stag()
        self.verify_greeting_stag()
        self.paywallflow3_stag()






