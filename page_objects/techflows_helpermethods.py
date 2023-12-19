from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException

class TechHelpers(BaseCase):
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
    GreetingMessage3_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi Nerwadi, I'm Zed, your digital assistant!\")]"
    greatomeet_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    inputfield_locator_x = "//*[@data-testid='MessageInput']"
    greet_text_locator_x = "//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]"
    bot_mainmenu_locator_x = "//div[contains(text(), 'How can I help you today?')]"
    TechQuestions_locator_x = "//button[contains(text(), 'Technical questions')]"
    AccessDazn_locator_x = "//button[contains(text(), 'Accessing DAZN')]"
    AboutDAZN_locator_x = "//button[contains(text(), 'About DAZN')]"
    PaymentsBilling_locator_x = "//button[contains(text(), 'Payments and billing')]"
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

    def user_signin(self):
        self.open("https://www.dazn.com/en-CA/home")
        self.maximize_window()
        CurrentURL = self.get_current_url()
        self.assertEqual(CurrentURL, "https://www.dazn.com/en-CA/home", "URL verified")
        # verifying if the en-CA is a part of currentURL
        self.assertTrue("en-CA" in CurrentURL)
        self._print(f'Current URL is {CurrentURL}')
        self.click(self.signin_button_x, timeout=None, delay=30)
        Signin_URL = self.get_current_url()
        self._print(f'User sign in URL is {Signin_URL}')
        self.assertTrue("signin" in Signin_URL)
        self.add_text(self.email_button_css, "nerwadi.shashikala@dazn.com", by="css selector", timeout=None)
        self.add_text(self.password_button_css, "DAZN2022@Sh", by="css selector", timeout=None)
        self.click(self.signinsubmit_buttonlocator_x, by="xpath", timeout=None, delay=30)
        Signedin_URL = self.get_current_url()
        self._print(f'User signed in URL is {Signedin_URL}')
        self.assertTrue("signin" in Signedin_URL)
        self.wait_for_element_present(self.signedpg_menu_button_x, timeout=30)
        self.click(self.signedpg_menu_button_x, by="xpath", timeout=None, delay=20)
        self.wait_for_element_present(self.signedpg_help_button_x, timeout=20)
        self.click(self.signedpg_help_button_x, by="xpath", timeout=None, delay=20)
        #self.get_text(self.signedpg_help_button_x, by="xpath")
        self._print(f'After signin the help page URL is {Signedin_URL}')
        self.assertTrue("en-CA" in Signedin_URL)






    # def open_dazn_help_page(self):
    #     CurrentURL = self.get_current_url()
    #     self._print(f'Current URL is {CurrentURL}')
    #     self.assertEqual(CurrentURL, "https://www.dazn.com/help", "URL verified")
    #     # verifying if the en-CA is a part of currentURL
    #     self.assertTrue("en-CA" in CurrentURL)
    #     self._print(f'Current URL is {CurrentURL}')
    def accept_cookies_and_start_chat(self):
        self.click(self.acptterms_popuplocator_css, timeout=None, delay=30)
        self.switch_to_frame("iframe#ada-button-frame")
        self.click(self.need_help_buttonlocator_css, timeout=None, delay=30)
        self._print("Button clicked")
        self.switch_to_default_content()
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self._print("switch successful")
    def verify_greeting(self):
        #GreetingMessage1_locator = "//div[@data-testid='AutoMessage' and contains(text(), \"Hi there, I'm Zed, your digital assistant! I'm here to help you with your questions about DAZN\")]"
        self.wait_for_element_visible(self.GreetingMessage3_locator_x, by="xpath", timeout=None)
        GreetingMessage1 = self.get_element(self.GreetingMessage3_locator_x, by="xpath", timeout=None)

        # Wait for the element to be visible


        # Assert the text
        expected_greeting_text = "Hi Nerwadi, I'm Zed, your digital assistant!"
        actual_greeting_text = GreetingMessage1.text
        self._print(actual_greeting_text)
        self.assertEqual(expected_greeting_text, actual_greeting_text, "Greeting verified")
        self.save_screenshot("Greeting", "TechflowsScreenshots")


    #def verify_name_response(self, message):
        #GreetingMessage2 = self.wait_for_text_visible("Can you tell me your first name please?",
        #selector="//div[@data-testid='AutoMessage' and contains(text(), \"Can you tell me your first name please?\")]",
         #by="xpath", timeout=50)
        #self.assertEqual(
         #   "Can you tell me your first name please?",
          #  GreetingMessage2.text, "First name verified")
        #self._print(GreetingMessage2.text)

        # inputfield = self.wait_for_element_present("//*[@data-testid='MessageInput']", timeout=50)
        # # the new send keys method also takes selector and message
        # # wait for the element to be visible then sends the message
        # inputfield.send_keys(message)
        # inputfield.submit()

        # bot_response = self.wait_for_text_visible("Great to meet you shashi.", selector="//div[@data-testid='AutoMessage' and contains(text(), 'Great to meet you shashi.')]", by="xpath", timeout=None)
        # response_text = bot_response.text
        # self._print(f"Actual Response: {response_text}")
        # self.assertEqual("Great to meet you shashi.", response_text, "Response verified")
        # self._print(f"User name verified with {response_text}")
    def verify_mainmenu(self):
        mainmenu = self.wait_for_element_present(self.bot_mainmenu_locator_x, by="xpath", timeout=40)
        Mainmenutext = mainmenu.text
        self._print(Mainmenutext)
        self.assertEqual(
            "How can I help you today? You can either pick a topic below, or type your query into the message box.",
            Mainmenutext, "menu text verified")
        self._print(f" Menu text verified with {Mainmenutext}")
    def main_menu_buttons(self):
        # # define xpath of all 4 buttons
        # TechQuestions = "//button[contains(text(), 'Technical questions')]"
        # AccessDazn = "//button[contains(text(), 'Accessing DAZN')]"
        # AboutDAZN = "//button[contains(text(), 'About DAZN')]"
        # PaymentsBilling = "//button[contains(text(), 'Payments and billing')]"

        Tech_Questions = self.get_element(self.TechQuestions_locator_x, by="xpath", timeout=None)
        self._print(Tech_Questions.text)
        self.assertEqual("Technical questions", Tech_Questions.text, "button name verifed")
        self._print(f"Tech button name verified with {Tech_Questions.text}")

        Access_Dazn = self.get_element(self.AccessDazn_locator_x, by="xpath", timeout=50)
        self._print(Access_Dazn.text)
        self.assertEqual("Accessing DAZN",Access_Dazn.text, "button name verifed")
        self._print(Access_Dazn.text)
        self._print(f"Access Dazn name verified with {Access_Dazn.text}")

        About_Dazn = self.get_element(self.AboutDAZN_locator_x, by="xpath", timeout=50)
        self._print(About_Dazn.text)
        self.assertEqual("About DAZN", About_Dazn.text, "button name verifed")
        self._print(f"About Dazn name verified with {About_Dazn.text}")

        Payments_Billing = self.get_element(self.PaymentsBilling_locator_x, by="xpath", timeout=50)
        self._print(Payments_Billing.text)
        self.assertEqual("Payments and billing", Payments_Billing.text, "button name verified")
        self._print(f"Payments and billing name verified with {Payments_Billing.text}")

        self.click(self.TechQuestions_locator_x, by="xpath", timeout=None, delay=50)
        self._print("Tech button clicked")

    def tech_buttons_flows(self):
        # verify and define the xpath for Tech buttons flows
        #Can_I_useDevice = "//button[contains(text(), 'Can I use my device?')]"
        # DAZN_app_support = "//button[contains(text(), 'DAZN app support')]"
        # Streaming_issues = "//button[contains(text(), 'Streaming issues')]"
        # Manage_devices = "//button[contains(text(), 'Manage your devices')]"
        # Pay_Per_View = "//button[contains(text(), 'Pay Per View Device Streaming')]"

        Can_I_useDevice = self.get_element(self.Can_I_useDevice_locator_x, by="xpath", timeout=50)
        self._print(Can_I_useDevice.text)
        self.assertEqual("Can I use my device?", Can_I_useDevice.text, "button name verifed")
        self._print(f"Can I use my device? name verified with {Can_I_useDevice.text}")

        DAZN_app_support = self.get_element(self.DAZN_app_support_locator_x, by="xpath", timeout=50)
        self._print(DAZN_app_support.text)
        self.assertEqual("DAZN app support", DAZN_app_support.text, "button name verifed")
        self._print(f"DAZN app support name verified with {DAZN_app_support.text}")

        Streaming_issues = self.get_element(self.Streaming_issues_locator_x, by="xpath", timeout=50)
        self._print(Streaming_issues.text)
        self.assertEqual("Streaming issues", Streaming_issues.text, "button name verifed")
        self._print(f"Streaming issue name verified with {Streaming_issues.text}")

        Manage_devices = self.get_element(self.Manage_devices_locator_x, by="xpath", timeout=50)
        self._print(Manage_devices.text)
        self.assertEqual("Manage your devices", Manage_devices.text, "button name verifed")
        self._print(f"Manage your devices name verified with {Manage_devices.text}")

        Pay_Per_View = self.get_element(self.Pay_Per_View_locator_x, by="xpath", timeout=50)
        self._print(Pay_Per_View.text)
        self.assertEqual("Pay Per View Device Streaming", Pay_Per_View.text, "button name verifed")
        self._print(f"Manage your devices name verified with {Pay_Per_View.text}")

    def can_I_use_deviceflow(self):

        self.click(self.Can_I_useDevice_locator_x, timeout=None, delay=50)
        #print(self.get_text(f' -- button clicked{self.Can_I_useDevice_locator_x}'))
        CanIUseDeviceText1= self.get_element(self.CanIUseDeviceText1_locator_x, by="xpath",timeout=20)
        self.assertEqual("So, the good news is DAZN works with 96% of all devices, so we should have you covered.",CanIUseDeviceText1.text, "CanIUseDeviceText1 verified")
        self._print(CanIUseDeviceText1.text)
        CanIUseDeviceText2 = self.get_element(
            self.CanIUseDeviceText2_locator_x, by="xpath",
            timeout=50)
        self.assertEqual("But if you want to make sure, check out this article 👇",
                         CanIUseDeviceText2.text, "CanIUseDeviceText2 verified")
        self._print(CanIUseDeviceText2.text)

        # Store the original window handle
        original_window_url = self.get_current_url()
        self._print(f'Original window is {original_window_url}')

        SupportedDeviceLink = self.SupportedDeviceLink_locator_x
        self.click(SupportedDeviceLink, by="xpath", timeout=None, delay=20)
        self._print("SupportedDeviceLink clicked")

        # Wait for a new window to appear and switch to it
        new_window = self.switch_to_newest_window()

        # Verify the new window URL
        new_URL = self.get_current_url()
        self._print(f"the new url is {new_URL}")
        self.wait(30)
        self.assertEqual(new_URL,
                         "https://www.dazn.com/en-CA/help/articles/supported-devices-homepage-canada?itm_source=dazn&itm_medium=chatbot_link&itm_cpg=chatbot_articles")
        self.assertTrue("www.dazn.com/en-CA/help/articles" in new_URL)
        self.wait(30)

        self._print("switching back to orginal window")
        # Switch back to the original window
        self.switch_to_default_window()
        #self.switch_to_window(original_window_url, timeout=None)
        self._print("switched to orginal window")
        self.switch_to_frame("ada-chat-frame", timeout=None)

    def need_more_help(self):
        #I_Need_More_Help = "//button[contains(text(), 'I need more help')]"
        self.wait_for_element_present(self.I_Need_More_Help_locator_x, by="xpath", timeout=None)
        self.click(self.I_Need_More_Help_locator_x, timeout=None, delay=40)
        try:
            captured_waiting_agent_text = self.wait_for_element_present(self.waiting_agent_locator_x, timeout=30)
            print(f"The captured text is: {captured_waiting_agent_text.text}")
        except NoSuchElementException:
            web_to_case_element = self.wait_for_element_present(self.web_case_element_locator_x)
            print(f"Web-to-case message {web_to_case_element.text}")
            #SendMessageButton = "//button[contains(text(), 'Send a message ✉️')"
            self.wait_for_element_present(self.SendMessage_locator_x)
            self.click(self.SendMessage_locator_x, by="xpath", timeout=None, delay=40)
            self._print("send a message button clicked")
            EnterInputField_Xpath = self.wait_for_element_present(self.EnterIssueDescrip_locator_x, by="xpath", timeout=None)
            self._print(EnterInputField_Xpath.text)
            inputfield = self.wait_for_element_present(self.inputfield_locator_x, timeout=50)
            # the new send keys method also takes selector and message
            # wait for the element to be visible then sends the message
            inputfield.send_keys("testing")
            inputfield.submit()
            CaseNumber_Xpath = self.CaseNumber_locator_x
            self.wait_for_element_present(CaseNumber_Xpath,by="xpath", timeout=None)
            self.click(CaseNumber_Xpath, by="xpath", timeout=None, delay=40)
            self._print(f'the case number generated as {CaseNumber_Xpath}')




    def close_and_end_chat(self):
        #CloseChatButton = "//button[@data-testid='CloseButton']"
        self.click(self.CloseChatButton_locator_x, timeout=None, delay=40)
        self._print("Close button clicked")

        #EndChatButton = "//button[contains(text(), 'End Chat')]"
        self.wait_for_element_present(self.EndChatButton_locator_x, by="xpath", timeout=20)
        self.click(self.EndChatButton_locator_x, timeout=None, delay=20)
        self._print("End chat button clicked")
    def user_signout(self):
        self.wait_for_element_present(self.signedpg_menu_button_x)
        self.click(self.signedpg_menu_button_x, by="xpath", timeout=None)
        self.click(self.signout_buttonlocator_x, by="xpath", timeout=None, delay=20)
        Signin_URL = self.get_current_url()
        self._print(f'After logout the URL is {Signin_URL}')
        self._print("Signed out successfully")
