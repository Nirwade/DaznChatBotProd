from page_objects.PPV_Reckoning_helpers import PPVF


class PPVFlow(PPVF):
    def test_ppvfinale_FightCard(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.ppv_prod()

    def test_ppvfinale_PPVFAQ(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.ppv_prod1()

    def test_ppvfinale_ForgotpwdLogin_Issue(self):
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.ppv_prod2()

    def test_ppvfinale_DayofReckoning_NeedHelp(self):
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.ppv_prod3()
        self.Need_HelpFlow1()

    def test_nonsigneduser_somethingelse(self):
        self.open("https://www.dazn.com/en-GB/help")
        self.maximize_window()
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.accept_cookies_and_start_chat1_prod()
        self.Non_signinuserJouney()
        self.ppv_prod3()
        self.Non_signinuserJouney1()
