# import basecase from seleniumbase
# pytest -k "test_chatbot_flow" --dashboard --html=report.html to generate the reports
from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.techflows_helpermethods import TechHelpers
class ChatbotFlow(TechHelpers):


# to run one particular test method cmd is: pytest -k "test_chatbot_flow"
#to run and print results on cmd is: pytest -k "test_chatbot_flow" -s


    # def setUp(self):
    #     super().setUp()
    #     self.open("https://www.dazn.com/en-CA/home")
    #     self.signinflow()
    #     print("Run before each test")

    # def tearDown(self):
    #     self.logout()
    #     super().tearDown()



    def test_chatbot_flow(self):
        self.user_signin()
        #self.open_dazn_help_page()
        self.accept_cookies_and_start_chat()
        self.verify_greeting()

        # Flow Step 1
        #self.verify_name_response("shashi")
        self.verify_mainmenu()
        self.main_menu_buttons()
        self.tech_buttons_flows()
        self.can_I_use_deviceflow()
        self.need_more_help()
        self.close_and_end_chat()
        self.user_signout()




