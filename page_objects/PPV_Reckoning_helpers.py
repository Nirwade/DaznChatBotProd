from seleniumbase import BaseCase
import os

class PPVF(BaseCase):
    signin_button_x = "//span[text()='Sign in']"
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

    def get_password_from_environment(self):
        password = os.environ.get('DAZN_PASSWORD')
        print(f"Environment variable DAZN_PASSWORD: {password}")
        if not password:
            raise ValueError("Password not found in environment variable.")
        return password

    def user_signin1_prod(self):
        self.open("https://www.dazn.com/en-GB/home")
        self.maximize_window()
        CurrentURL = self.get_current_url()
        self._print(f'Current URL is {CurrentURL}')
        self.click(self.acptterms_popuplocator_css, timeout=None)
        self.click(self.signin_button_x, timeout=None)
        self.type(self.email_button_css, "rahul.varikela@dazn.com", by="css selector", timeout=None)
        password = self.get_password_from_environment()
        self.type(self.password_button_css, password, by="css selector", timeout=None)
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
        #self.assert_exact_text("Hi Nerwadi, I'm Zed, your digital assistant!", "GreetingMessage3_locator_x", timeout=20)
        self.assertEqual(expected_greeting_text, actual_greeting_text, "Greeting verified")
        self.wait_for_element_visible(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        GreetingMessage2 = self.get_element(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        self._print(GreetingMessage2.text)
        expected_greeting_text1 = "Please choose one of the options below:"
        actual_greeting_text1 = GreetingMessage2.text
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
        self.wait(15)
        self.assertEqual(new_URL1,
                         "https://www.dazn.com/help/articles/day-of-reckoning")
        self.assertTrue("day-of-reckoning" in new_URL1)
        self.save_screenshot("Fightercardlink", "PPV")
        self.wait(15)

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
        self.wait(15)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/help/articles/pay-per-view-faqs")
        self.assertTrue("pay-per-view-faqs" in new_URL)
        self.save_screenshot("Fightercard", "PPV")
        self.wait(15)

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
        self.wait(15)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/signin/forgot-password")
        self.assertTrue("forgot-password" in new_URL)
        self.save_screenshot("PWDlink", "PPV")
        self.wait(15)

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








