#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from page_objects.prodchatbot_helpers import ProdBot



class BotFlow(ProdBot):
    # def test_ppvfinale_FightCard(self):
    #     self.open("https://www.dazn.com/en-GB/home")
    #     self.user_signin1_prod()
    #     self.accept_cookies_and_start_chat1_prod()
    #     self.verify_greeting1_prod()
    #     self.ppv_prod()
    #
    # def test_ppvfinale_PPVFAQ(self):
    #     self.open("https://www.dazn.com/en-GB/home")
    #     self.user_signin1_prod()
    #     self.accept_cookies_and_start_chat1_prod()
    #     self.verify_greeting1_prod()
    #     self.ppv_prod1()
    #
    # def test_ppvfinale_ForgotpwdLogin_Issue(self):
    #     self.open("https://www.dazn.com/en-GB/help")
    #     self.user_signin1_prod()
    #     self.accept_cookies_and_start_chat1_prod()
    #     self.verify_greeting1_prod()
    #     self.ppv_prod2()
    #
    # def test_ppvfinale_DayofReckoning_NeedHelp(self):
    #     self.open("https://www.dazn.com/en-GB/help")
    #     self.user_signin1_prod()
    #     self.accept_cookies_and_start_chat1_prod()
    #     self.verify_greeting1_prod()
    #     self.ppv_prod3()
    #     self.Need_HelpFlow1()
    #
    # def test_nonsigneduser_somethingelse(self):
    #     self.open("https://www.dazn.com/en-GB/help")
    #     self.click(self.acptterms_popuplocator_css, timeout=None)
    #     self.accept_cookies_and_start_chat1_prod()
    #     self.Non_signinuserJouney()
    #     self.ppv_prod3()
    #     self.Non_signinuserJouney1()



    def test_paywallNonSignedUser(self):
        self.open("https://www.dazn.com/en-SG/help")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.accept_cookies_and_start_chat1_prod()
        # self.verify_greeting1_prod()
        # self.accept_cookies_and_start_chat1_prod()
        self.Non_signinuserJouney()
        self.Paywall_NonSignedin_journey()

    def test_aboutdzn(self):
        self.open("https://www.dazn.com/en-GB/help")
        self.maximize_window()
        self.click(self.acptterms_popuplocator_css, timeout=10)
        self.accept_cookies_and_start_chat1_prod()
        self.Non_signinuserJouney()
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        self.AboutDazn()


    def test_paymentsflow(self):
        self.open("https://www.dazn.com/en-GB/help")
        self.maximize_window()
        self.click(self.acptterms_popuplocator_css, timeout=10)
        self.accept_cookies_and_start_chat1_prod()
        self.Non_signinuserJouney()
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        #self.AccessingDaznIcantLogin1()
        self.PaymentsBillingNonSignedUserRefund()
        #self.PaymentsBillingNonSignedUserChangeAcn()
        #self.PaymentsBillingNonSignedUserUpdateAcn()

    def test_reuse(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.maximize_window()
        self.click(self.acptterms_popuplocator_css, timeout=10)
        self.wait(15)
        self.get_password_from_environment()
        self.user_signin1_prod()
        #self.accept_cookies_and_start_chat1_prod()
        # self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        # self.verify_greeting1_prod()
        # self.wait_for_element_present(self.AboutDaznbtw_css, timeout=None)
        # self.click(self.AboutDaznbtw_css, timeout=None)
        # self.wait_for_element_present(self.AbtDznSchedule_css, timeout=None)
        # self.save_screenshot("schedulelinks", "AbtDazn")
        # self.click(self.AbtDznSchedule_css, timeout=None)
        # self.LinkValidator()
        # self.wait_for_element_present(self.AbtDznHowIPay_css, timeout=None)
        # self.click(self.AbtDznHowIPay_css, timeout=None)
        # self.wait_for_element_present(self.AbtDznHowIPayLink_x, timeout=None)
        # self.click(self.AbtDznHowIPayLink_x, timeout=None)
        # self.need_more_help()

    def test_fiba(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()


    def test_fiba1(self):
        self.open("https://www.dazn.com/en-IT/home")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.Courtside()
        self.courtdaznsub()
        self.LinkValidator()

    def test_fiba2(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.Courtside()
        self.courtdaznsub1()

    def test_fiba3(self):
        self.open("https://www.dazn.com/en-IT/home")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.Courtside()
        self.courthowmuch()
        self.LinkValidator()

    def test_fiba4(self):
        self.open("https://www.dazn.com/en-IT/home")
        self.maximize_window()
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.Courtside()
        self.courthowmuch1()

    def test_fiba5(self):
        self.open("https://www.dazn.com/en-IT/home")
        self.maximize_window()
        self.wait(10)
        self.wait_for_element_present(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=10)
        self.user_signin1_prod()
        self.accept_cookies_and_start_chat1_prod()
        self.verify_greeting1_prod()
        self.Courtside()
        self.blackouts()
        self.LinkValidator()


















