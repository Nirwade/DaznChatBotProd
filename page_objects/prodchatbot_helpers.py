from seleniumbase import BaseCase
from seleniumbase.config import settings
from selenium.common.exceptions import NoSuchElementException

import os

class ProdBot(BaseCase):
    signin_button_x = "//span[contains(text(), \"Sign in\")]"
    email_button_css = "#email"
    password_button_css = "#password"
    signinsubmit_buttonlocator_x = "//button[@type='submit']"
    signedpg_menu_button_x = "//span[text()='MENU']"
    signedpg_help_button_x = "//span[text()='Help']"
    signout_buttonlocator_x = "//span[text()='Sign out']"
    acptterms_popuplocator_css = "button#onetrust-accept-btn-handler"
    need_help_buttonlocator_css = "//span[contains(text(), 'Need help?')]"
    GreetingMessage1_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi there, I'm Zed, your digital assistant! I'm here to help you with your questions about DAZN\")]"
    GreetingMessage2_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Can you tell me your first name please?\")]"
    GreetingMessage3_locator_x = "//div[contains(text(), \"Hi rahul, I'm Zed, your digital assistant!\")]"
    GreetingMessage4_locator_x = "// div[contains(text(), 'Please choose one of the options below:')]"
    greatomeet_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    updatepayment_paywallbtw_csss = "button:contains('Update payment method/Insufficient funds')"
    inputfield_locator_x = "//*[@data-testid='MessageInput']"
    greet_text_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    bot_mainmenu_locator_x = "//div[contains(text(), 'How can I help you today?')]"
    PDayReckoningBtw_x = "//button[contains(text(), 'PPV - Day of Reckoning')]"
    Fightcardbtw_x = "//button[contains(text(), 'PPV Day of Reckoning - Fight card')]"
    PPVFAQBtw_x= "//button[contains(text(), 'PPV FAQs')]"
    #PPVFAQLink_x = "//div[contains(text(), 'PPV FAQ')]"
    PPVonSkyBtw_x = "//button[contains(text(), 'PPV on SKY')]"
    PWDLoginBtw_x ="//button[contains(text(), 'Password/Login Issues')]"
    SomethingElseBtw_x = "//button[contains(text(), 'Something Else')]"
    Fightercardlink_x = "(//div[@class='sc-hQYpqk cBjVdg' and contains(text(), 'Fight card')])[1]"
    PPVFAQLink_x = "(//div[contains(text(), 'PPV FAQ')])[2]"
    main_menuchatbtw_x = "//button[contains(text(), 'Main menu')]"
    Forgotpwd_link_x= "//div[contains(text(), 'Forgot Password')]"
    yesThanksbtw_x = "//button[contains(text(), 'Yes thanks')]"
    newclosemsg_x= "// div[contains(text(), \"Closing the chat is as easy as clicking the '❌' above. Have a fantastic day ahead!\")]"
    skipbtw_x = "//button[contains(text(), 'Skip')]"
    beforehwdNsigneduser_x = "//div[contains(text(), \"What's your first name?\")]"
    CaseNumber_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    SendMessageButton = "//button[contains(text(), 'Send a message ✉️')]"
    EnterEmail = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    EnterIssueDescrip_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Can you provide a description of your issue?')]"
    CaseNumber_Xpath = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    waiting_agent_locator_x = "//h1[contains(text(), 'Waiting for an agent')]"
    cancel_chat_x = "//button[contains(text(), 'Cancel')]"
    greetfirstname_x = "(//div[contains(text(), 'Can you tell me your first name please?')])[1]"
    greet_please_select_text_x = "//div[contains(text(), 'Please choose one of the options below:')]"
    usernameconfirmbeforehanoff_x = "(//div[contains(text(), \"What's your first name?\")])[1]"
    Greetnonsignin_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi there, I'm Zed, your digital assistant! I'm here to help you with your questions about DAZN\")]"
    TypeEmailadress_x = "//div[contains(text(), \"Please type the email address you'd like to use.\")]"
    nameconfirmsendmsg_x = "(//div[contains(text(), 'Can you tell me your name please?')])[1]"
    Dazn_button_x1 = "//button[@class='sc-ciSkZP dzZdOC' and normalize-space(text())='DAZN']"
    Paywall_button_x= "//button[contains(text(), \"'Update payment method/Insufficient funds' message\")]"
    Paywall_yes_close_x = "//button[contains(text(), 'Yes, I can close it')]"
    Paywall_myaccount_link_x = "//div[contains(text(), 'MyAccount')]"
    Paywall_okthanks_x = "//button[contains(text(), 'Okay thanks')]"
    mainmenubtw_x = "//button[contains(text(), 'Main menu')]"
    AboutDaznbtw_css = 'button:contains("About DAZN")'
    AbtDznSchedule_css = 'a[data-testid="AutoLink"] > div > div > div'
    AbtDznHowIPay_css = 'button:contains("How do I pay?")'
    AgreePopUp_x = '//button[text()="AGREE"]'
    AbtDznHowIPayLink_x = "//div[text()='🔗 How do I pay?']"
    AbtDznCanIUseDevice_css = 'button:contains("Can I use my device ?")'
    AbtDznSupportDeviceLink_x = "//div[text()='🔗 DAZN supported devices']"
    AbtDznHowDoIJoin_css = 'button:contains("How do I join DAZN ?")'
    AbtDznSmartTV_css = "//span[text()='Smart TV']"
    AbtDznSmartTVLink_x = "//div[text()='🔗 Watching DAZN on a Smart TV']"
    AccesDazn_css = 'button:contains("Accessing DAZN")'
    AccesDaznIcantLogin_css = 'button:contains("I can\'t log in")'
    AccesDaznTypeEmail_x = "(//div[contains(text(), \"Can you please type the email\")])[2]"
    AccessDaznCheckDiffEmail_x = "//p[contains(text(), \"Do you want to check a different email address?\")]"
    AccessDaznYesBtw_x = 'button:contains("Yes")'
    AccessDaznNoBtw_x = 'button: contains("No")'
    AccessDaznEmailNotInRecords_x = "(//div[contains(text(), \"Dang, that email address isn't in my records.\")])"
    AccessDaznGoodnews_x = "(//div[contains(text(), \"Good news , I've found your email address in our database!\")])[1]"
    AccessDaznIneedHelpSignup_css = 'button:contains("I need help to sign up")'
    AccessDaznIcantFindEmail_x = "(//div[contains(text(), \"Hmm...I can't find your email address in our system.\")])[3]"
    AccesDaznAppleDeviceLink_x = "//div[contains(text(), '🔗 How to watch DAZN on iPhone & iPad')]"
    AccessDaznAppleDevice_css = 'button:contains("Apple device")'
    NeedToSignBeforeProcced_x = "//p[contains(text(), \"OK, before we can go any further, you'll need to sign in.\")]"
    PaymentsBilling_locator_css = 'button:contains("Payments and billing")'
    PaymentBillingForDazn_css = 'button:contains("Payments and billing for DAZN")'
    PaymentBillingChangeAcnDetails_css = 'button:contains("Change account details")'
    PaymentBillingReactivateAcn_css = 'button:contains("Reactivate account")'
    PaymentBillingUpdatePayment_css= 'button:contains("Update payment details")'
    PaymentsBillingRefund_css = 'button:contains("Refund")'
    PaymentsBillingRefundDazn_css = 'button:contains("Refund DAZN Subscription")'
    PaymentsBillingCancel_css = 'button:contains("Cancel DAZN Subscription")'
    PaymentsBillingGiftCodes_css = 'button:contains("Gift codes")'
    PaymentsBillingGiftCodesDazn_css = 'button:contains("DAZN Gift code")'
    PaymentsBillingGiftNeedHelp_css = 'button:contains("I need help with a gift code")'
    NeverMindBtw_css = 'button:contains("Never mind")'
    updatepayment_paywallbtw_csss = "button:contains('Update payment method/Insufficient funds')"
    yes_i_can_closebtw_x = "//button[@class='sc-ciSkZP dzZdOC' and contains(text(), 'Yes, I can close it')]"
    I_still_cant_see_contentbtw_x = "//button[contains(text(), \"I've done that but I still can't see content in my TV\")]"
    okay_thanksbtw_css = "button:contains('Okay thanks')"
    main_menuchatbtw_x = "//div[contains(text(), 'Main Menu')]"
    Im_done_fortodaybtw_x = "//button[contains(text(), \"I'm done for today\")]"
    it_wont_let_me_watch_x = "//button[contains(text(), \"No, it won't let me watch\")]"
    my_account_link = "//div[contains(text(), 'MyAccount')]"
    CloseChatButton_locator_x = "//button[@data-testid='CloseButton']"
    EndChatButton_locator_x = "//button[contains(text(), 'End Chat')]"
    I_Need_More_Help_locator_x = "//button[contains(text(), 'I need more help')]"
    waiting_agent_locator_x = "//h1[text()='Waiting for an agent']"
    web_case_element_locator_x = "//div[contains(text(), \"I'm sorry, we're out of the office right now, but we'll be back to help every day from 10:00-23:00.\")]"
    # SendMessage_locator_x = "//button[contains(text(), 'Send a message ✉️')"
    EnteremailInputFieldtext_locator_x = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    CaseNumber_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    SendMessageButton = "//button[contains(text(), 'Send a message ✉️')]"
    EnterEmail = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    EnterIssueDescrip_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Can you provide a description of your issue?')]"
    CaseNumber_Xpath = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    signout_buttonlocator_x = "//span[text()='Sign out']"
    acptterms_popuplocator_css = "//button[@id='onetrust-accept-btn-handler']"
    need_help_buttonlocator_css = "span.button__text"
    GreetingMessage1_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi there, I'm Zed, your digital assistant! I'm here to help you with your questions about DAZN\")]"
    GreetingMessage2_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Can you tell me your first name please?\")]"
    #GreetingMessage3_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi Nerwadi, I'm Zed, your digital assistant!\")]"
    greatomeet_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    inputfield_locator_x = "//*[@data-testid='MessageInput']"
    greet_text_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    bot_mainmenu_locator_x = "//div[contains(text(), 'How can I help you today?')]"
    TechQuestions_locator_x = "//button[contains(text(), 'Technical questions')]"
    AccessDazn_locator_x = "//button[contains(text(), 'Accessing DAZN')]"
    AboutDAZN_locator_x = "//button[contains(text(), 'About DAZN')]"
    PaymentsBilling_locator_css = 'button:contains("Payments and billing")'
    Can_I_useDevice_locator_x = "//button[contains(text(), 'Can I use my device?')]"
    DAZN_app_support_locator_x = "//button[contains(text(), 'DAZN app support')]"
    Streaming_issues_locator_x = "//button[contains(text(), 'Streaming issues')]"
    Manage_devices_locator_x = "//button[contains(text(), 'Manage your devices')]"
    Pay_Per_View_locator_x = "//button[contains(text(), 'Pay Per View Device Streaming')]"
    CanIUseDeviceText1_locator_x = "//div[contains(text(), 'So, the good news is DAZN works with 96% of all devices')]"
    CanIUseDeviceText2_locator_x = "//div[contains(text(), 'But if you want to make sure,')]"
    SupportedDeviceLink_locator_x = "//div[text()='🔗 DAZN supported devices']"
    I_Need_More_Help_locator_x = "//button[contains(text(), 'I need more help')]"
    waiting_agent_locator_x = "//h1[text()='Waiting for an agent']"
    CloseChatButton_locator_x = "//button[@data-testid='CloseButton']"
    EndChatButton_locator_x = "//button[contains(text(), 'End Chat')]"
    web_case_element_locator_x = "//div[contains(text(), \"I'm sorry, we're out of the office right now, but we'll be back to help every day from 10:00-23:00.\")]"
    SendMessage_locator_x = "//button[contains(text(), 'Send a message ✉️')"
    EnteremailInputFieldtext_locator_x = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    CaseNumber_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
    EnterEmail = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    EnterIssueDescrip_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Can you provide a description of your issue?')]"
    CaseNumber_Xpath = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    Courtside_btw = "//button[contains(text(), \"Courtside 1891\")]"
    daznSubincludethis = "//button[contains(text(), \"Does my DAZN subscription include this?\")]"
    Howmuchsubcourtyard = "//button[contains(text(), \"How much is the subscription plan for Courtside?\")]"
    blackouts_btw = "//button[contains(text(), \"Blackouts\")]"
    fiba_yesbtw = "//button[contains(text(), \"Yes\")]"
    fiba_nobtw = "//button[contains(text(), \"No\")]"
    fiba_purchaselink = "//div[contains(text(), \"Purchase Link\")]"
    blackoutslink = "//div[contains(@class, 'sc-hQYpqk') and contains(@class, 'cBjVdg') and text()='Blackouts']"





    def get_password_from_environment(self):
        password = os.environ.get('DAZN_PASSWORD')
        print(f"Environment variable DAZN_PASSWORD: {password}")
        if not password:
            raise ValueError("Password not found in environment variable.")
        return password

    def user_signin1_prod(self):
        #self.open("https://www.dazn.com/en-GB/home")
        #self.maximize_window()
        CurrentURL = self.get_current_url()
        self._print(f'Current URL is {CurrentURL}')
        #self.click(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.signin_button_x, timeout=None)
        self.wait(20)
        self.type(self.email_button_css, "rahul.varikela@dazn.com", by="css selector", timeout=None)
        self.type(self.password_button_css, self.get_password_from_environment(), timeout=None)
        self.click(self.signinsubmit_buttonlocator_x, by="xpath", timeout=None)
        self.wait_for_element_present(self.signedpg_menu_button_x, timeout=None)
        self.click(self.signedpg_menu_button_x, by="xpath", timeout=None)
        self.wait_for_element_present(self.signedpg_help_button_x, timeout=None)
        self.click(self.signedpg_help_button_x, by="xpath", timeout=None)
        aftersigninurl= self.get_current_url()
        self._print(f'urlafterusersignin is -- {aftersigninurl}')



    def accept_cookies_and_start_chat1_prod(self):
        self.switch_to_frame("iframe#ada-button-frame", timeout=None)
        self.wait_for_element_visible(self.need_help_buttonlocator_css, timeout=None)
        self.save_screenshot("Needhelpbtw", "PPV")
        self.click(self.need_help_buttonlocator_css, timeout=None)
        self._print("Button clicked")
        self.switch_to_default_content()
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self._print("switch successful")

    def verify_greeting1_prod(self):
        self.wait_for_element_visible(self.GreetingMessage3_locator_x, by="xpath", timeout=None)
        GreetingMessage1 = self.get_element(self.GreetingMessage3_locator_x, by="xpath", timeout=None)
        expected_greeting_text = "Hi rahul, I'm Zed, your digital assistant!"
        actual_greeting_text = GreetingMessage1.text
        self._print(GreetingMessage1.text)
        self.assertEqual(expected_greeting_text, actual_greeting_text, "Greeting verified")
        # self.wait_for_element_visible(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        # GreetingMessage2 = self.get_element(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        # self._print(GreetingMessage2.text)
        #expected_greeting_text1 = "Please choose one of the options below:"
        #actual_greeting_text1 = GreetingMessage2.text
        #self.assert_exact_text("Please choose one of the options below:", "GreetingMessage4_locator_x")
        self.save_screenshot("GreetingMsg", "PPV")



    def ppv_prod(self):
        self.wait_for_element_visible(self.PDayReckoningBtw_x, timeout=None)
        self.save_screenshot("Greeting", "PPV")
        self.click(self.PDayReckoningBtw_x, timeout=None)
        self.wait_for_element_present(self.SomethingElseBtw_x, timeout=None)
        self.save_screenshot("PPV Menu", "PPV")
        self.click(self.Fightcardbtw_x, timeout=None)
        self.wait_for_element_present(self.Fightercardlink_x, timeout=None)
        self.save_screenshot("FigherCard", "PPV")
        self.click(self.Fightercardlink_x, timeout=None)
        self._print("Figherlink clicked")
        self.switch_to_newest_window()
        new_URL1 = self.get_current_url()
        self._print(f"the new url is {new_URL1}")
        self.wait(10)
        self.assertEqual(new_URL1,
                         "https://www.dazn.com/help/articles/day-of-reckoning")
        self.assertTrue("day-of-reckoning" in new_URL1)
        self.save_screenshot("Fightercardlink", "PPV")
        self.wait(10)

        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self.wait_for_element_visible(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("Fightercard", "PPV")
        self.click(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("mainmenuclick", "PPV")
        self.wait_for_element_visible(self.PDayReckoningBtw_x, timeout=None)
        self.save_screenshot("menu view after click on menubtw", "PPV")

    def ppv_prod1(self):
        self.wait_for_element_visible(self.PDayReckoningBtw_x, timeout=None)
        self.click(self.PDayReckoningBtw_x, timeout=None)
        self.wait_for_element_present(self.PPVFAQBtw_x, timeout=None)
        self.click(self.PPVFAQBtw_x, timeout=None)
        self.wait_for_element_visible(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("PPVFAQFlow", "PPV")
        self.click(self.PPVFAQLink_x, timeout=None)
        self._print("PPVFaqLink clicked")

        # Wait for a new window to appear and switch to it
        new_window = self.switch_to_newest_window()

        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(10)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/help/articles/pay-per-view-faqs")
        self.assertTrue("pay-per-view-faqs" in new_URL)
        self.save_screenshot("Fightercard", "PPV")
        self.wait(10)

        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self.wait_for_element_visible(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("PPVFaqFlow", "PPV")
        self.click(self.main_menuchatbtw_x, timeout=None)


    def ppv_prod2(self):
        self.wait_for_element_visible(self.PDayReckoningBtw_x, timeout=None)
        self.click(self.PDayReckoningBtw_x, timeout=None)
        self.wait_for_element_present(self.PWDLoginBtw_x, timeout=None)
        self.click(self.PWDLoginBtw_x, timeout=None)
        self.wait_for_element_visible(self.Forgotpwd_link_x, timeout=None)
        self.click(self.Forgotpwd_link_x, timeout=None)
        self._print("forgotpwdlink clicked")

        # Wait for a new window to appear and switch to it
        new_window = self.switch_to_newest_window()

        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(10)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/signin/forgot-password")
        self.assertTrue("forgot-password" in new_URL)
        self.save_screenshot("PWDlink", "PPV")
        self.wait(10)

        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self.wait_for_element_visible(self.yesThanksbtw_x, timeout=None)
        self.save_screenshot("PWDFlow", "PPV")
        self.click(self.yesThanksbtw_x, timeout=None)
        self.wait_for_element_present(self.newclosemsg_x, timeout=None)
        self.save_screenshot("Closeformat", "PPV")

    def ppv_prod3(self):
        self.wait_for_element_visible(self.PDayReckoningBtw_x, timeout=None)
        self.click(self.PDayReckoningBtw_x, timeout=None)

    def Need_HelpFlow1(self):
        self.wait_for_element_present(self.SomethingElseBtw_x, timeout=None)
        self.click(self.SomethingElseBtw_x, timeout=None)
        self.wait(15)

        if self.is_element_present(self.waiting_agent_locator_x):
            self._print(" waiting for the agent")
            self.save_screenshot("connectingagent", "PPV")
            self.click(self.cancel_chat_x, timeout=None)
            self._print("Cancelled chat")
            #captured_waiting_agent = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=None)
            self.assert_exact_text("Waiting for an agent", self.waiting_agent_locator_x, timeout=None)
            #self._print(f"The captured text is: {captured_waiting_agent.text}")

        else:
            self._print("waiting for an agent not found")
            # SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessageButton, timeout=None)
            self.save_screenshot("outofhours", "PaywallStagScreenshots")
            self.click(self.SendMessageButton, by="xpath", timeout=None)
            self._print("send a message button clicked")
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath",timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=None)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath, by="xpath", timeout=None)
            casenumbertext = self.get_element(CaseNumber_Xpath, by="xpath", timeout=None)
            self._print(f'the case number generated as {casenumbertext.text}')
            self.save_screenshot("caseidcreation", "PaywallStagScreenshots")

    def Non_signinuserJouney(self):
        self.wait_for_element_visible(self.Greetnonsignin_x, timeout=None)
        self.wait_for_element_visible(self.greetfirstname_x, timeout=None)
        self.save_screenshot("firstnameconfirm", "PPV")
        self.click(self.skipbtw_x, timeout=None)
        self.wait_for_element_present(self.greet_please_select_text_x, timeout=None)
        self.save_screenshot("skipmenu", "PPV")

    def Non_signinuserJouney1(self):
        self.wait_for_element_present(self.SomethingElseBtw_x, timeout=None)
        self.click(self.SomethingElseBtw_x, timeout=None)
        nonsigninusernameverify= self.get_element(self.usernameconfirmbeforehanoff_x, by= "xpath", timeout=None)
        self._print(nonsigninusernameverify.text)
        self.save_screenshot("name_confirm_before_handoff", "PPV")
        self.type(self.inputfield_locator_x, "shash", timeout=None)
        self.submit(self.inputfield_locator_x)
        self.wait(15)

        if self.is_element_present(self.waiting_agent_locator_x):
            self._print(" waiting for the agent")
            self.save_screenshot("connectingagent", "PPV")
            self.click(self.cancel_chat_x, timeout=None)
            self._print("Cancelled chat")
            #captured_waiting_agent = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=None)
            self.assert_exact_text("Waiting for an agent", self.waiting_agent_locator_x, timeout=None)
            #self._print(f"The captured text is: {captured_waiting_agent.text}")

        else:
            self._print("waiting for an agent not found")
            # SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessageButton, timeout=None)
            self.save_screenshot("outofhours", "PaywallStagScreenshots")
            self.click(self.SendMessageButton, by="xpath", timeout=None)
            self._print("send a message button clicked")
            self.wait_for_element_present(self.TypeEmailadress_x, timeout=None)
            self.type(self.inputfield_locator_x, "dhshha@gmail.com", timeout=None)
            self.submit(self.inputfield_locator_x)
            self.wait_for_element_present(self.nameconfirmsendmsg_x, timeout=None)
            self.type(self.inputfield_locator_x, "shh", timeout=None)
            self.submit(self.inputfield_locator_x)
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath",timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=None)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath, by="xpath", timeout=None)
            casenumbertext = self.get_element(CaseNumber_Xpath, by="xpath", timeout=None)
            self._print(f'the case number generated as {casenumbertext.text}')
            self.save_screenshot("caseidcreation", "PaywallStagScreenshots")


    def Paywall_NonSignedin_journey(self):
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        self.wait_for_element_visible(self.Paywall_button_x, timeout=None)
        self.save_screenshot("paywallbutton", "PaywallProdScreenshots")
        self.click(self.Paywall_button_x, timeout=None)
        self.wait_for_element_visible(self.Paywall_yes_close_x, timeout=None)
        self.click(self.Paywall_yes_close_x, timeout=None)
        self.scroll_to_element(self.Paywall_myaccount_link_x, timeout=30)
        self.wait_for_element_visible(self.Paywall_myaccount_link_x, by="xpath", timeout=None)
        self.save_screenshot("yesIcancloseflow", "PaywallProdScreenshots")
        self.click(self.Paywall_myaccount_link_x, timeout=None)
        self._print("Myaccountlink clicked")
        self.switch_to_newest_window()

        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(10)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/myaccount/subscription")
        self.assertTrue("myaccount" in new_URL)
        self.save_screenshot("Accountlink", "PaywallProdScreenshots")
        self.wait(10)
        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self.wait_for_element_visible(self.Paywall_okthanks_x, timeout=None)
        self.click(self.Paywall_okthanks_x, timeout=None)
        self.save_screenshot("closebuttons", "PaywallProdScreenshots")
        self.wait_for_element_visible(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)
        self.save_screenshot("mainmenuclick", "PaywallProdScreenshots")

    def LinkValidator(self):
        self.switch_to_newest_window()
        new_URL1 = self.get_current_url()
        self._print(f"the new url is {new_URL1}")
        self.wait(10)
        self.save_screenshot("URLPage", "fiba")
        self.wait(10)
        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)

    def AboutDazn(self):
        self.wait_for_element_present(self.AboutDaznbtw_css, timeout=None)
        self.click(self.AboutDaznbtw_css, timeout=None)
        self.wait_for_element_present(self.AbtDznSchedule_css, timeout=None)
        self.save_screenshot("schedulelinks", "AbtDazn")
        self.click(self.AbtDznSchedule_css, timeout=None)
        self.LinkValidator()
        self.wait_for_element_present(self.AbtDznHowIPay_css, timeout=None)
        self.click(self.AbtDznHowIPay_css, timeout=None)
        self.wait_for_element_present(self.AbtDznHowIPayLink_x, timeout=None)
        self.click(self.AbtDznHowIPayLink_x, timeout=None)
        self.LinkValidator()
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        self.wait_for_element_present(self.AboutDaznbtw_css, timeout=None)
        self.click(self.AboutDaznbtw_css, timeout=None)
        self.wait_for_element_present(self.AbtDznCanIUseDevice_css, timeout=None)
        self.click(self.AbtDznCanIUseDevice_css, timeout=None)
        self.wait_for_element_present(self.AbtDznSupportDeviceLink_x, timeout=None)
        self.click(self.AbtDznSupportDeviceLink_x, timeout=None)
        self.LinkValidator()
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        self.wait_for_element_present(self.AboutDaznbtw_css, timeout=None)
        self.click(self.AboutDaznbtw_css, timeout=None)
        self.wait_for_element_present(self.AbtDznHowDoIJoin_css, timeout=None)
        self.click(self.AbtDznHowDoIJoin_css, timeout=None)
        self.wait_for_element_present(self.AbtDznSmartTV_css, timeout=None)
        self.click(self.AbtDznSmartTV_css, timeout=None)
        self.wait_for_element_present(self.AbtDznSmartTVLink_x, timeout=None)
        self.click(self.AbtDznSmartTVLink_x, timeout=None)
        self.LinkValidator()
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)

    def AccessingDaznIcantLogin(self):
        self.wait_for_element_present(self.AccesDazn_css, timeout=None)
        self.click(self.AccesDazn_css, timeout=None)
        self.wait_for_element_present(self.AccesDaznIcantLogin_css, timeout=None)
        self.click(self.AccesDaznIcantLogin_css, timeout=None)
        self.wait_for_element_present(self.AccesDaznTypeEmail_x, timeout=None)
        self.type(self.inputfield_locator_x, "gkdsjsj@gmail.com")
        self.submit(self.inputfield_locator_x)
        self.wait_for_element_present(self.AccessDaznCheckDiffEmail_x, timeout=None)
        self.click(self.AccessDaznYesBtw_x, timeout=None)
        self.wait_for_element_present(self.AccessDaznCheckDiffEmail_x, timeout=None)
        self.type(self.inputfield_locator_x, "gkdsjsj@gmail.com")
        self.submit(self.inputfield_locator_x)

        self.wait_for_element_present(self.AccessDaznEmailNotInRecords_x, timeout=None)
        self.wait(10)
        # From here it goes to handoff signed in user --
        # in case of non-signed user journey confirm name before handoff

    def AccessingDaznIcantLogin1(self):
        self.wait_for_element_present(self.AccesDazn_css, timeout=None)
        self.click(self.AccesDazn_css, timeout=None)
        self.wait_for_element_present(self.AccesDaznIcantLogin_css, timeout=None)
        self.click(self.AccesDaznIcantLogin_css, timeout=None)
        self.wait_for_element_present(self.AccesDaznTypeEmail_x, timeout=None)
        self.type(self.inputfield_locator_x, "nerwadi.shashikala@dazn.com")
        self.submit(self.inputfield_locator_x)
        #self.wait_for_element_visible(self.AccessDaznGoodnews_x, timeout=None)
        self.wait_for_element_present(self.AccessDaznYesBtw_x, timeout=None)
        self.click(self.AccessDaznYesBtw_x, timeout=None)
        self.save_screenshot("AccessingDazn", "AccessingDazn")
        self.wait_for_element_present(self.AccessDaznYesBtw_x, timeout=None)
        self.click(self.AccessDaznYesBtw_x, timeout=None)
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)

    def AccessingDaznIneedHelpSignup(self):
        self.wait_for_element_present(self.AccesDazn_css, timeout=None)
        self.click(self.AccesDazn_css, timeout=None)
        self.wait_for_element_present(self.AccessDaznIneedHelpSignup_css, timeout=None)
        self.click(self.AccessDaznIneedHelpSignup_css, timeout=None)
        self.type(self.inputfield_locator_x, "nerwadi.shashikala@dazn.com")
        self.submit(self.inputfield_locator_x)
        #self.wait_for_element_present(self.AccessDaznGoodnews_x, timeout=None)
        self.save_screenshot("AccessingDazn", "AccessingDazn")
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)
        self.wait_for_element_visible(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)
        self.wait_for_element_present(self.AccesDazn_css, timeout=None)
        self.click(self.AccesDazn_css, timeout=None)
        self.wait_for_element_present(self.AccessDaznIneedHelpSignup_css, timeout=None)
        self.click(self.AccessDaznIneedHelpSignup_css, timeout=None)
        self.type(self.inputfield_locator_x, "nirwadi.shashikala@dazn.com")
        self.submit(self.inputfield_locator_x)
        self.wait_for_element_present(self.AccessDaznIcantFindEmail_x, timeout=None)
        self.save_screenshot("AccessingDazn", "AccessingDazn")
        # From here it goes to handoff signed in user --
        # in case of non-signed user journey confirm name before handoff

    def AccessingDaznHowDoIJoinDzn(self):
        self.wait_for_element_present(self.AccesDazn_css, timeout=None)
        self.click(self.AccesDazn_css, timeout=None)
        self.wait_for_element_present(self.AbtDznHowDoIJoin_css, timeout=None)
        self.click(self.AbtDznHowDoIJoin_css, timeout=None)
        self.wait_for_element_present(self.AccessDaznAppleDevice_css, timeout=None)
        self.click(self.AccessDaznAppleDevice_css, timeout=None)
        self.wait_for_element_present(self.AccesDaznAppleDeviceLink_x, timeout=None)
        self.click(self.AccesDaznAppleDeviceLink_x, timeout=None)
        self.LinkValidator()
        self.wait_for_element_present(self.mainmenubtw_x, timeout=None)
        self.click(self.mainmenubtw_x, timeout=None)

    def PaymentsBillingNonSignedUserRefund(self):
        self.wait_for_element_present(self.PaymentsBilling_locator_css, timeout=None)
        self.click(self.PaymentsBilling_locator_css, timeout=None)
        self.wait_for_element_present(self.PaymentBillingForDazn_css, timeout=None)
        self.click(self.PaymentBillingForDazn_css, timeout=None)
        self.wait_for_element_present(self.PaymentsBillingRefund_css, timeout=None)
        self.click(self.PaymentsBillingRefund_css, timeout=None)
        self.wait_for_element_present(self.PaymentsBillingRefundDazn_css, timeout=None)
        self.click(self.PaymentsBillingRefundDazn_css, timeout=None)
        self.wait_for_element_present(self.NeedToSignBeforeProcced_x, timeout=None)
        self.assert_exact_text("OK, before we can go any further, you'll need to sign in.", self.NeedToSignBeforeProcced_x, timeout=None)
        self.wait_for_element_present(self.NeverMindBtw_css, timeout=None)
        self.click(self.NeverMindBtw_css, timeout=None)
        self.wait_for_element_present(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)

    def PaymentsBillingNonSignedUserChangeAcn(self):
        self.wait_for_element_present(self.PaymentsBilling_locator_css, timeout=None)
        self.click(self.PaymentsBilling_locator_css, timeout=None)
        self.wait_for_element_present(self.PaymentBillingForDazn_css, timeout=None)
        self.click(self.PaymentBillingForDazn_css, timeout=None)
        self.wait_for_element_present(self.PaymentBillingChangeAcnDetails_css, timeout=None)
        self.click(self.PaymentBillingChangeAcnDetails_css, timeout=None)
        self.wait_for_element_present(self.NeedToSignBeforeProcced_x, timeout=None)
        self.assert_exact_text("OK, before we can go any further, you'll need to sign in.",
                               self.NeedToSignBeforeProcced_x, timeout=None)
        self.wait_for_element_present(self.NeverMindBtw_css, timeout=None)
        self.click(self.NeverMindBtw_css, timeout=None)
        self.wait_for_element_present(self.Dazn_button_x1, timeout=None)
        self.click(self.Dazn_button_x1, timeout=None)

    def PaymentsBillingNonSignedUserUpdateAcn(self):
        self.wait_for_element_present(self.PaymentsBilling_locator_css, timeout=None)
        self.click(self.PaymentsBilling_locator_css, timeout=None)
        self.wait_for_element_present(self.PaymentBillingForDazn_css, timeout=None)
        self.click(self.PaymentBillingForDazn_css, timeout=None)
        self.wait_for_element_present(self.PaymentBillingUpdatePayment_css, timeout=None)
        self.click(self.PaymentBillingUpdatePayment_css, timeout=None)
        self.wait_for_element_present(self.NeedToSignBeforeProcced_x, timeout=None)
        self.assert_exact_text("OK, before we can go any further, you'll need to sign in.",
                               self.NeedToSignBeforeProcced_x, timeout=None)
        self.wait_for_element_present(self.NeverMindBtw_css, timeout=None)
        self.click(self.NeverMindBtw_css, timeout=None)

    def paywallflow1_stag(self):
        self.click(self.updatepayment_paywallbtw_csss, timeout=None)
        self.wait_for_element_visible(self.yes_i_can_closebtw_x, timeout=None)
        self.save_screenshot("paywallmenu", "PaywallStagScreenshots")
        self.click(self.yes_i_can_closebtw_x, by="xpath", timeout=None)
        self.scroll_to_element(self.my_account_link, by="xpath", timeout=None)
        self.wait_for_element_visible(self.my_account_link, by="xpath", timeout=None)
        self.save_screenshot("yesIcancloseflow", "PaywallStagScreenshots")
        self.click(self.my_account_link, timeout=None)
        self._print("Myaccountlink clicked")
        self.switch_to_newest_window()
        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(10)
        self.assertEqual(new_URL,
                         "https://stag.dazn.com/myaccount/subscription")
        self.assertTrue("myaccount" in new_URL)
        self.save_screenshot("myaccountlink", "PaywallStagScreenshots")
        self.wait(10)
        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        # self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self.click(self.okay_thanksbtw_css, timeout=None)
        self.wait_for_element_visible(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("closebuttons", "PaywallStagScreenshots")
        self.click(self.main_menuchatbtw_x, timeout=None)
        self.save_screenshot("mainmenuclick", "PaywallStagScreenshots")

    def paywallflow2_stag(self):
        self.click(self.updatepayment_paywallbtw_csss, timeout=None, delay=None)
        self.wait_for_element_visible(self.yes_i_can_closebtw_x, timeout=None)
        self.save_screenshot("paywallmenu", "PaywallStagScreenshots")
        self.click(self.yes_i_can_closebtw_x, by="xpath", timeout=None)
        self.scroll_to_element(self.my_account_link, by="xpath", timeout=None)
        self.wait_for_element_visible(self.my_account_link, by="xpath", timeout=None)
        self.save_screenshot("yesIcancloseflow", "PaywallStagScreenshots")
        self.click(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=None)
        self.wait_for_element_visible(self.Im_done_fortodaybtw_x, by="xpath", timeout=None)
        self.save_screenshot("I_still_can't_view_TV", "PaywallStagScreenshots")
        self.click(self.Im_done_fortodaybtw_x, by="xpath", timeout=None)
        self.save_screenshot("closechatflow", "PaywallStagScreenshots")
        self.click(self.CloseChatButton_locator_x, timeout=None, delay=None)
        self._print("Close button clicked")

        # EndChatButton = "//button[contains(text(), 'End Chat')]"
        self.wait_for_element_present(self.EndChatButton_locator_x, by="xpath", timeout=None)
        self.click(self.EndChatButton_locator_x, timeout=None, delay=None)
        self._print("End chat button clicked")

    def paywallflow3_stag(self):
        self.click(self.updatepayment_paywallbtw_csss, timeout=None, delay=None)
        self.wait_for_element_visible(self.it_wont_let_me_watch_x, timeout=None)
        self.click(self.it_wont_let_me_watch_x, by="xpath", timeout=None, delay=None)
        self.save_screenshot("No_wont_letmewatch", "PaywallStagScreenshots")
        self.scroll_to_element(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=None)
        self.click(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=None, delay=None)
        self.wait_for_element_visible(self.I_Need_More_Help_locator_x,by="xpath", timeout=None)
        self.save_screenshot("needmorehelpbuttons", "PaywallStagScreenshots")
        self.click(self.I_Need_More_Help_locator_x, timeout=None, delay=None)
        if self.is_element_visible(self.waiting_agent_locator_x):
            self._print(" waiting for the agent")
            captured_waiting_agent_text = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=None)
            self._print(f"The captured text is: {captured_waiting_agent_text.text}")
            self.save_screenshot("connectingagent", "PaywallStagScreenshots")
        else:
            self._print("waiting for an agent not found")
            # SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessageButton)
            self.save_screenshot("outofhours", "PaywallStagScreenshots")
            self.click(self.SendMessageButton, by="xpath", timeout=None, delay=None)
            self._print("send a message button clicked")
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath",timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=None)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath, by="xpath", timeout=None)
            casenumbertext = self.get_element(CaseNumber_Xpath, by="xpath", timeout=None)
            self._print(f'the case number generated as {casenumbertext.text}')
            self.save_screenshot("caseidcreation", "PaywallStagScreenshots")

    def close_and_end_chat(self):
        #CloseChatButton = "//button[@data-testid='CloseButton']"
        self.wait_for_element_present(self.CloseChatButton_locator_x, by="xpath", timeout=None)
        self.click(self.CloseChatButton_locator_x, timeout=None, delay=None)
        self._print("Close button clicked")

        #EndChatButton = "//button[contains(text(), 'End Chat')]"
        self.wait_for_element_present(self.EndChatButton_locator_x, by="xpath", timeout=None)
        self.click(self.EndChatButton_locator_x, timeout=None, delay=None)
        self._print("End chat button clicked")
    def user_signout(self):
        self.wait_for_element_present(self.signedpg_menu_button_x)
        self.click(self.signedpg_menu_button_x, by="xpath", timeout=None)
        self.wait_for_element_present(self.signout_buttonlocator_x)
        self.click(self.signout_buttonlocator_x, by="xpath", timeout=None, delay=None)
        Signin_URL = self.get_current_url()
        self._print(f'After logout the URL is {Signin_URL}')
        self._print("Signed out successfully")

    def main_menu_buttons(self):
        # # define xpath of all 4 buttons
        # TechQuestions = "//button[contains(text(), 'Technical questions')]"
        # AccessDazn = "//button[contains(text(), 'Accessing DAZN')]"
        # AboutDAZN = "//button[contains(text(), 'About DAZN')]"
        # PaymentsBilling = "//button[contains(text(), 'Payments and billing')]"


        self.wait_for_element_present(self.TechQuestions_locator_x,by="xpath",timeout=None)
        tech_questions = self.get_element(self.TechQuestions_locator_x, by="xpath", timeout=None)
        self._print(f"Tech button name verified with {tech_questions.text}")

        self.wait_for_element_present(self.AccessDazn_locator_x, by="xpath", timeout=None)
        access_dazn = self.get_element(self.AccessDazn_locator_x, by="xpath", timeout=None)
        self._print(f"Access Dazn name verified with {access_dazn.text}")

        self.wait_for_element_present(self.AboutDAZN_locator_x, by="xpath", timeout=None)
        about_dazn = self.get_element(self.AboutDAZN_locator_x, by="xpath", timeout=None)
        self._print(f"About Dazn name verified with {about_dazn.text}")

        self.wait_for_element_present(self.PaymentsBilling_locator_css, by="xpath", timeout=None)
        payments_billing = self.get_element(self.PaymentsBilling_locator_css, by="xpath", timeout=None)
        self._print(f"Payments and billing name verified with {payments_billing.text}")
        #Use self.savescreenshot to verify the content here

        self.click(self.TechQuestions_locator_x, by="xpath", timeout=None, delay=None)
        self._print("Tech button clicked")

    def tech_buttons_flows(self):
        # verify and define the xpath for Tech buttons flows
        #Can_I_useDevice = "//button[contains(text(), 'Can I use my device?')]"
        # DAZN_app_support = "//button[contains(text(), 'DAZN app support')]"
        # Streaming_issues = "//button[contains(text(), 'Streaming issues')]"
        # Manage_devices = "//button[contains(text(), 'Manage your devices')]"
        # Pay_Per_View = "//button[contains(text(), 'Pay Per View Device Streaming')]"

        self.wait_for_element_present(self.Can_I_useDevice_locator_x, by="xpath", timeout=None)
        Can_I_useDevice = self.get_element(self.Can_I_useDevice_locator_x, by="xpath", timeout=None)
        self._print(f"Can I use my device? name verified with {Can_I_useDevice.text}")

        self.wait_for_element_present(self.DAZN_app_support_locator_x, by="xpath", timeout=None)
        DAZN_app_support = self.get_element(self.DAZN_app_support_locator_x, by="xpath", timeout=None)
        self._print(f"DAZN app support name verified with {DAZN_app_support.text}")

        self.wait_for_element_present(self.Streaming_issues_locator_x, by="xpath", timeout=None)
        Streaming_issues = self.get_element(self.Streaming_issues_locator_x, by="xpath", timeout=None)
        self._print(f"Streaming issue name verified with {Streaming_issues.text}")

        self.wait_for_element_present(self.Manage_devices_locator_x, by="xpath", timeout=None)
        Manage_devices = self.get_element(self.Manage_devices_locator_x, by="xpath", timeout=None)
        self._print(f"Manage your devices name verified with {Manage_devices.text}")

        self.wait_for_element_present(self.Pay_Per_View_locator_x, by="xpath", timeout=None)
        Pay_Per_View = self.get_element(self.Pay_Per_View_locator_x, by="xpath", timeout=None)
        self._print(f"Manage your devices name verified with {Pay_Per_View.text}")
        # Use self.savescreenshot to verify the content here

    def can_I_use_deviceflow(self):

        self.wait_for_element_present(self.Can_I_useDevice_locator_x, by="xpath", timeout=None)
        self.click(self.Can_I_useDevice_locator_x, timeout=None, delay=None)
        #print(self.get_text(f' -- button clicked{self.Can_I_useDevice_locator_x}'))
        CanIUseDeviceText1= self.get_element(self.CanIUseDeviceText1_locator_x, by="xpath",timeout=None)
        self.assertEqual("So, the good news is DAZN works with 96% of all devices, so we should have you covered.",CanIUseDeviceText1.text, "CanIUseDeviceText1 verified")
        self._print(CanIUseDeviceText1.text)
        self.wait_for_element_present(self.CanIUseDeviceText2_locator_x, by="xpath", timeout=None)
        CanIUseDeviceText2 = self.get_element(
            self.CanIUseDeviceText2_locator_x, by="xpath",
            timeout=None)
        self.assertEqual("But if you want to make sure, check out this article 👇",
                         CanIUseDeviceText2.text, "CanIUseDeviceText2 verified")
        self._print(CanIUseDeviceText2.text)
        # Store the original window handle
        original_window_url = self.get_current_url()
        self._print(f'Original window is {original_window_url}')

        self.wait_for_element_present(self.SupportedDeviceLink_locator_x, by="xpath", timeout=None)
        self.click(self.SupportedDeviceLink_locator_x, by="xpath", timeout=None, delay=None)
        self._print("SupportedDeviceLink clicked")
        self.switch_to_newest_window()
        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(10)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/en-CA/help/articles/supported-devices-homepage-canada?itm_source=dazn&itm_medium=chatbot_link&itm_cpg=chatbot_articles")
        self.assertTrue("www.dazn.com/en-CA/help/articles" in new_URL)
        self.wait(10)

        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        #self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)

    def need_more_help(self):
        #I_Need_More_Help = "//button[contains(text(), 'I need more help')]"
        self.wait_for_element_present(self.I_Need_More_Help_locator_x, by="xpath", timeout=None)
        self.click(self.I_Need_More_Help_locator_x, timeout=None, delay=None)
        if self.is_element_visible(self.waiting_agent_locator_x):
            self._print(" waiting for the agent")
            captured_waiting_agent_text = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=None)
            self._print(f"The captured text is: {captured_waiting_agent_text.text}")
        else:
            self._print("waiting for an agent not found")
            # SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessageButton)
            self.save_screenshot("outofhours", "PaywallStagScreenshots")
            self.click(self.SendMessageButton, by="xpath", timeout=None, delay=None)
            self._print("send a message button clicked")
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath",
                                                                  timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=None)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath, by="xpath", timeout=None)
            casenumbertext = self.get_element(CaseNumber_Xpath, by="xpath", timeout=None)
            self._print(f'the case number generated as {casenumbertext.text}')
    def Courtside(self):
        self.wait_for_element_present(self.Courtside_btw, timeout=None)
        self.click(self.Courtside_btw, timeout=None)
        self.wait_for_element_present(self.daznSubincludethis, timeout=None)
        self.wait_for_element_present(self.Howmuchsubcourtyard,timeout=None)
        self.wait_for_element_present(self.blackouts_btw, timeout=None)
        self.save_screenshot("fibamenu", "fiba")

    def courtdaznsub(self):
        self.wait_for_element_present(self.daznSubincludethis, timeout=None)
        self.click(self.daznSubincludethis, timeout=None)
        self.wait_for_element_present(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_nobtw, timeout=None)
        self.click(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_purchaselink,timeout=None)
        self.click(self.fiba_purchaselink,timeout=None)
        self.save_screenshot("courtdaznsub", "fiba")
        # use link validator to verify

    def courtdaznsub1(self):
        self.wait_for_element_present(self.daznSubincludethis, timeout=None)
        self.click(self.daznSubincludethis, timeout=None)
        self.wait_for_element_present(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_nobtw, timeout=None)
        self.click(self.fiba_nobtw, timeout=None)
        self.wait_for_element_present(self.need_help_buttonlocator_css, timeout=None)
        self.save_screenshot("courtdaznsub1", "fiba")
        # use link validator to verify


    def courthowmuch(self):
        self.wait_for_element_present(self.Howmuchsubcourtyard,timeout=None)
        self.click(self.Howmuchsubcourtyard,timeout=None)
        self.wait_for_element_present(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_nobtw, timeout=None)
        self.save_screenshot("courthowmuch", "fiba")
        self.click(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_purchaselink, timeout=None)
        self.click(self.fiba_purchaselink, timeout=None)
        self.save_screenshot("courthowmuch", "fiba")
        # use link validator to verify

    def courthowmuch1(self):
        self.wait_for_element_present(self.Howmuchsubcourtyard,timeout=None)
        self.click(self.Howmuchsubcourtyard,timeout=None)
        self.wait_for_element_present(self.fiba_yesbtw, timeout=None)
        self.wait_for_element_present(self.fiba_nobtw, timeout=None)
        self.save_screenshot("courthowmuch", "fiba")
        self.click(self.fiba_nobtw, timeout=None)
        self.wait_for_element_present(self.need_help_buttonlocator_css, timeout=None)
        self.save_screenshot("courtdaznsub1", "fiba")

    def blackouts(self):
        self.wait_for_element_present(self.blackouts_btw, timeout=None)
        self.click(self.blackouts_btw, timeout=None)
        self.wait_for_element_present(self.blackoutslink, timeout=None)
        self.click(self.blackoutslink, timeout=None)
        # use link validator to verify
        self.save_screenshot("blackouts", "fiba")





























































