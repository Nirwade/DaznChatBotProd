from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException

class PayHelpers(BaseCase):
    signin_button_x = "//span[text()='Sign in']"
    email_button_css = "#email"
    password_button_css = "#password"
    signinsubmit_buttonlocator_x = "//button[@type='submit']"
    signedpg_menu_button_x = "//span[text()='MENU']"
    signedpg_help_button_x = "//span[text()='Help']"
    signout_buttonlocator_x = "//span[text()='Sign out']"
    acptterms_popuplocator_css = "button#onetrust-accept-btn-handler"
    need_help_buttonlocator_css = "span.button__text"
    GreetingMessage1_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi there, I'm Zed, your digital assistant! I'm here to help you with your questions about DAZN\")]"
    GreetingMessage2_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Can you tell me your first name please?\")]"
    GreetingMessage3_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi test, I'm Zed, your digital assistant!\")]"
    GreetingMessage4_locator_x = "// div[contains(text(), 'Please choose one of the options below:')]"
    greatomeet_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    inputfield_locator_x = "//*[@data-testid='MessageInput']"
    greet_text_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    bot_mainmenu_locator_x = "//div[contains(text(), 'How can I help you today?')]"
    updatepayment_paywallbtw_csss = "button:contains('Update payment method/Insufficient funds')"
    yes_i_can_closebtw_x = "//button[@class='sc-ciSkZP dzZdOC' and contains(text(), 'Yes, I can close it')]"
    I_still_cant_see_contentbtw_x ="//button[contains(text(), \"I've done that but I still can't see content in my TV\")]"
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
    #SendMessage_locator_x = "//button[contains(text(), 'Send a message ✉️')"
    EnteremailInputFieldtext_locator_x = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    CaseNumber_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"
    SendMessageButton = "//button[contains(text(), 'Send a message ✉️')]"
    EnterEmail = '//div[@data-testid="AutoMessage" and contains(text(), "Please type the email address you\'d like to use.")]'
    EnterIssueDescrip_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Can you provide a description of your issue?')]"
    CaseNumber_Xpath = "//div[@data-testid='AutoMessage' and contains(text(), 'A case has been created with number')]"



    def user_signin_stag(self):
        self.open("https://stag.dazn.com/en-IT/home")
        self.maximize_window()
        CurrentURL = self.get_current_url()
        self.assertEqual(CurrentURL, "https://stag.dazn.com/en-IT/home", "URL verified")
        # verifying if the en-CA is a part of currentURL
        self.assertTrue("en-IT" in CurrentURL)
        self._print(f'Current URL is {CurrentURL}')
        self.click(self.acptterms_popuplocator_css, timeout=None, delay=20)
        self.click(self.signin_button_x, timeout=None, delay=30)
        Signin_URL = self.get_current_url()
        self._print(f'User sign in URL is {Signin_URL}')
        self.assertTrue("signin" in Signin_URL)
        self.add_text(self.email_button_css, "Shassh020399+TestITNonEng@gmail.com", by="css selector", timeout=None)
        self.add_text(self.password_button_css, "12345a", by="css selector", timeout=None)
        self.click(self.signinsubmit_buttonlocator_x, by="xpath", timeout=None, delay=10)
        Signedin_URL = self.get_current_url()
        self._print(f'User signed in URL is {Signedin_URL}')
        self.assertTrue("signin" in Signedin_URL)
        self.wait_for_element_present(self.signedpg_menu_button_x, timeout=30)
        self.click(self.signedpg_menu_button_x, by="xpath", timeout=None, delay=20)
        self.wait_for_element_present(self.signedpg_help_button_x, timeout=20)
        self.click(self.signedpg_help_button_x, by="xpath", timeout=None, delay=20)
        #self.get_text(self.signedpg_help_button_x, by="xpath")
        self._print(f'After signin the help page URL is {Signedin_URL}')
        self.assertTrue("en-IT" in Signedin_URL)

    def accept_cookies_and_start_chat_stag(self):
        self.switch_to_frame("iframe#ada-button-frame", timeout=20)
        self.wait_for_element(self.need_help_buttonlocator_css, timeout=None)
        self.click(self.need_help_buttonlocator_css, timeout=None, delay=30)
        self._print("Button clicked")
        self.switch_to_default_content()
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self._print("switch successful")

    def verify_greeting_stag(self):
        self.wait_for_element_visible(self.GreetingMessage3_locator_x, by="xpath", timeout=30)
        GreetingMessage1 = self.get_element(self.GreetingMessage3_locator_x, by="xpath", timeout=30)

        # Wait for the element to be visible
        # Assert the text
        expected_greeting_text = "Hi test, I'm Zed, your digital assistant!"
        actual_greeting_text = GreetingMessage1.text
        self._print(actual_greeting_text)
        self.assertEqual(expected_greeting_text, actual_greeting_text, "Greeting verified")
        self.wait_for_element_visible(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        GreetingMessage2= self.get_element(self.GreetingMessage4_locator_x, by="xpath", timeout=None)
        expected_greeting_text1 = "Please choose one of the options below:"
        actual_greeting_text1 = GreetingMessage2.text
        self.wait_for_element_visible(self.updatepayment_paywallbtw_csss, timeout=None)
        self.save_screenshot("Greeting", "PaywallStagScreenshots")

    def paywallflow1_stag(self):
        self.click(self.updatepayment_paywallbtw_csss, timeout=None, delay=10)
        self.wait_for_element_visible(self.yes_i_can_closebtw_x, timeout=None)
        self.save_screenshot("paywallmenu", "PaywallStagScreenshots")
        self.click(self.yes_i_can_closebtw_x, by="xpath", timeout=None, delay=30)
        self.scroll_to_element(self.my_account_link, by="xpath", timeout=30)
        self.wait_for_element_visible(self.my_account_link, by="xpath", timeout=30)
        self.save_screenshot("yesIcancloseflow", "PaywallStagScreenshots")
        self.click(self.my_account_link, timeout=None)
        self._print("Myaccountlink clicked")

        # Wait for a new window to appear and switch to it
        new_window = self.switch_to_newest_window()

        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(30)
        self.assertEqual(new_URL,
                         "https://stag.dazn.com/myaccount/subscription")
        self.assertTrue("myaccount" in new_URL)
        self.save_screenshot("myaccountlink", "PaywallStagScreenshots")
        self.wait(30)

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
        self.click(self.updatepayment_paywallbtw_csss, timeout=None, delay=10)
        self.wait_for_element_visible(self.yes_i_can_closebtw_x, timeout=None)
        self.save_screenshot("paywallmenu", "PaywallStagScreenshots")
        self.click(self.yes_i_can_closebtw_x, by="xpath", timeout=None, delay=30)
        self.scroll_to_element(self.my_account_link, by="xpath", timeout=30)
        self.wait_for_element_visible(self.my_account_link, by="xpath", timeout=30)
        self.save_screenshot("yesIcancloseflow", "PaywallStagScreenshots")
        self.click(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=20)
        self.wait_for_element_visible(self.Im_done_fortodaybtw_x, by="xpath", timeout=20)
        self.save_screenshot("I_still_can't_view_TV", "PaywallStagScreenshots")
        self.click(self.Im_done_fortodaybtw_x, by="xpath", timeout=10)
        self.save_screenshot("closechatflow", "PaywallStagScreenshots")
        self.click(self.CloseChatButton_locator_x, timeout=None, delay=40)
        self._print("Close button clicked")

        # EndChatButton = "//button[contains(text(), 'End Chat')]"
        self.wait_for_element_present(self.EndChatButton_locator_x, by="xpath", timeout=20)
        self.click(self.EndChatButton_locator_x, timeout=None, delay=20)
        self._print("End chat button clicked")

    def paywallflow3_stag(self):
        self.click(self.updatepayment_paywallbtw_csss, timeout=None, delay=10)
        self.wait_for_element_visible(self.it_wont_let_me_watch_x, timeout=None)
        self.click(self.it_wont_let_me_watch_x, by="xpath", timeout=None, delay=20)
        self.save_screenshot("No_wont_letmewatch", "PaywallStagScreenshots")
        self.scroll_to_element(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=20)
        self.click(self.I_still_cant_see_contentbtw_x, by="xpath", timeout=None, delay=20)
        self.wait_for_element_visible(self.I_Need_More_Help_locator_x,by="xpath", timeout=None)
        self.save_screenshot("needmorehelpbuttons", "PaywallStagScreenshots")
        self.click(self.I_Need_More_Help_locator_x, timeout=None, delay=30)
        if self.is_element_visible(self.waiting_agent_locator_x):
            self._print(" waiting for the agent")
            captured_waiting_agent_text = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=30)
            self._print(f"The captured text is: {captured_waiting_agent_text.text}")
            self.save_screenshot("connectingagent", "PaywallStagScreenshots")
        else:
            self._print("waiting for an agent not found")
            # SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessageButton)
            self.save_screenshot("outofhours", "PaywallStagScreenshots")
            self.click(self.SendMessageButton, by="xpath", timeout=None, delay=40)
            self._print("send a message button clicked")
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath",timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=50)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath, by="xpath", timeout=None)
            casenumbertext = self.get_element(CaseNumber_Xpath, by="xpath", timeout=None)
            self._print(f'the case number generated as {casenumbertext.text}')
            self.save_screenshot("caseidcreation", "PaywallStagScreenshots")





