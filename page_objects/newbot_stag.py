from seleniumbase import BaseCase
from seleniumbase.config import settings
from selenium.common.exceptions import NoSuchElementException

import os



class NewBot(BaseCase):
    initial_greet_x = "//div[contains(text(), 'How can I help you today? You can either pick a topic below, or type your query into the message box.')]"
    dazn_button_x = "//button[@class=\"sc-ciSkZP dzZdOC\" and text()=\"DAZN\"]"
    nfl_button_x = "//button[contains(text(), 'NFL Game Pass')]"
    dazn_shop_button_x = "//button[contains(text(), 'DAZN Shop')]"
    courtside_btw = "//button[contains(text(), 'Courtside 1891')]"
    signin_zenpage_link = "//a[contains(@class, 'sign-in')]"
    email_field = "//input[contains(@id, 'email')]"
    password_filed = "//input[contains(@id, 'password')]"
    web_signin_user_btw = "button[data-test-id=\"signIn__BUTTON\"]"
    acptterms_popuplocator_css = "button#onetrust-accept-btn-handler"
    bottom_help_page_link = "//a[@target=\"_blank\" and @rel=\"noopener\" and contains(@class, 'footer-link-item__link___23unL') and contains(@class, 'footer-link-item__footer-item-title___1GGRT') and contains(@class, 'footer-link-item__normal___1kibz') and @href=\"/help\"]"
    TechnicalQuestions_btw = "//button[contains(text(), 'Technical Questions')]"
    Streaming_Issues_btw = "//button[contains(text(), 'Streaming Issues')]"
    About_Dazn_btw = "//button[contains(text(), 'About DAZN')]"
    Manage_your_subscription_btw = "//button[contains(text(), 'Manage your subscription')]"
    Payments_btw = "//button[contains(text(), 'Payments')]"
    PayWallBtw = "//button[contains(text(), 'Update payment method/Insufficient funds')]"
    Signin_issues = "//button[contains(text(), 'Sign-in issues')]"
    Handoff_to_support = "// button[contains(text(), 'Handoff to Support > DACH')]"
    Located_content_btw ="// button[contains(text(), 'Locked content issues')]"
    Dazn_app_btw = "// button[contains(text(), 'DAZN app support')]"
    Manag_devices_btw ="// button[contains(text(), 'Manage my devices')]"
    Android_device_btw = "// button[contains(text(), 'Android Device')]"
    Apple_device_btw = "// button[contains(text(), 'Apple Device')]"
    Smart_Tv = "// button[contains(text(), 'Smart TV')]"
    Game_console = "// button[contains(text(), 'Game console')]"
    Web_browser ="// button[contains(text(), 'Web browser')]"
    Other_btw="// button[contains(text(), 'Other')]"
    I_NeedMoreHelp_btw = "//button[contains(text(), 'I need more help')]"
    Live_stream_btw = "//span[contains(text(), 'Live stream')]"
    OnDemand_video_btw = "//span[contains(text(), 'On-demand video')]"
    Streaming_multiple_devices = "//span[contains(text(), 'Streaming on multiple devices')]"
    stream_itsotherdevice = "//span[contains(text(), \"No, it's another device\")]"
    stream_yes = "//span[contains(text(), 'Yes')]"
    signin_blocker_msg = "//p[contains(text(), \"Before we can go any further, you'll need to sign in.\")]"
    internet_met_requirements = "//p[contains(text(), \"Does your internet speed meet the above requirements?\")]"
    mydevice_and_app_are_btw = "//button[contains(text(), \"My device and app are both already updated\")]"
    updated_but_help_btw = "//button[contains(text(), \"Updating did not help\")]"
    working_now = "//button[contains(text(), \"It's working now\")]"
    yes_btw = "//button[contains(text(), \"Yes\")]"
    no_btw = "//button[contains(text(), \"No\")]"
    stream_no = "//span[contains(text(), 'No')]"
    isthereanythingelsebtw = "//div[contains(text(), \"Is there anything else we can help you with?\")]"
    is_device_supported_btw = "//button[contains(text(), \"Is my device supported?\")]"
    subscription_plans_btw = "//button[contains(text(), \"Our subscription plans\")]"
    accepted_payments_btw = "//button[contains(text(), \"Accepted payment methods\")]"
    supported_device_btw = "//button[contains(text(), \"Supported Devices\")]"
    main_menu_btw = "//button[contains(text(), \"Main menu\")]"
    interested_in_sub_plans = "//p[contains(text(), \"Would you be interested in our subscription plans?\")]"
    buy_plan = "//button[contains(text(), \"I want to buy a plan\")]"
    talk_to_someone = "//button[contains(text(), \"I want to talk to someone\")]"
    no_create_accn = "//button[contains(text(), \"No, I will create an account\")]"
    Update_Payments_btw = "//button[contains(text(), \"Update payment details\")]"
    Refund_btw = "//button[contains(text(), \"Refund\")]"
    Gift_codes = "//button[contains(text(), \"Gift codes\")]"
    Yes_I_got_it = "//span[contains(text(), \"Yes, I've got it\")]"
    I_need_help_finding = "//span[contains(text(), \"No, I need help finding it\")]"
    need_more_help = "//div[contains(text(), 'Need more help')]"
    I_want_to_talk_to = "//button[contains(text(), 'I want to talk to someone')]"
    I_want_to_buy_gift = "//button[contains(text(), 'I want to buy a gift code')]"
    ForgotUsername = "/button[contains(text(), 'Forgot username')]"
    ForgotPassword ="//button[contains(text(), 'Forgot password')]"
    DanzShop_btw = "//button[contains(text(), \"DAZN Shop\")]"
    Official_Merchandise = "//button[contains(text(), \"Official Merchandise\")]"
    Order_Status = "//button[contains(text(), \"Order Status\")]"
    Get_help = "// button[contains(text(), \"Get Help\")]"
    windows_device = "//span[contains(text(), 'Desktop - Windows')]"
    remove_device = "//button[contains(text(), 'Remove a device')]"
    signout_device = "//button[contains(text(), 'Sign out of all devices')]"
    contact_suport_btw = "//button[contains(text(), 'Contact Support')]"
    support_text_btw = "//div[starts-with(text(), 'Please wait while we connect you to our Customer Service Specialists. You’ll be notified here when the agent responds.')]"
    signmeout_btw = "//button[starts-with(text(), 'Yes, sign me out')]"







    def get_password_from_environment1(self):
        password = os.environ.get('DAZN_PASSWORD')
        print(f"Environment variable DAZN_PASSWORD: {password}")
        if not password:
            raise ValueError("Password not found in environment variable.")
        return password

    def signin(self):
        self.open("https://stag.dazn.com/en-DE/signin")
        self.maximize_window()
        # self.wait_for_element_present(self.signin_zenpage_link, timeout=9)
        # self.click(self.signin_zenpage_link, timeout=4)
        # self.wait(8)

        self.wait_for_element_present(self.email_field, timeout=None)
        self.type(self.email_field, "Shassh020399+TestGDE@gmail.com", timeout=None)
        self.click(self.acptterms_popuplocator_css, timeout=3)
        self.wait(10)
        self.type(self.password_filed,self.get_password_from_environment1(), timeout=None)
        self.click(self.web_signin_user_btw, timeout=5)
        self.wait(10)
        self.scroll_to_bottom()
        self.wait(10)
        self.wait_for_element_present(self.bottom_help_page_link, timeout=None)
        self.click(self.bottom_help_page_link, timeout=None)
        self.wait(10)

    def start_chart(self):
        self.switch_to_frame("iframe#ada-button-frame")
        self.wait_for_element_present("//button[@id='ada-chat-button']", timeout=None)
        self.click("//button[@id='ada-chat-button']")
        self.switch_to_default_content()
        self.switch_to_frame("ada-chat-frame", timeout=None)
        self._print("switch successful")
        self.wait(20)

    def verify_initial_greet(self):
        self.wait_for_element_present(self.initial_greet_x, timeout=None)
        self.wait_for_element_present(self.dazn_button_x, timeout=None)
        self.wait_for_element_present(self.nfl_button_x, timeout=None)
        self.wait_for_element_present(self.dazn_shop_button_x, timeout=None)
        self.save_screenshot("initial_greet", "New Bot")



    def nfl_flow(self):
        self.wait_for_element_present(self.nfl_button_x, timeout=None)
        self.click(self.nfl_button_x, timeout=None)
        self.save_screenshot("nfl_menuflow", "New Bot")

    def dazn_shop_flow(self):
        self.wait_for_element_present(self.dazn_shop_button_x, timeout=None)
        self.click(self.dazn_shop_button_x, timeout=None)
        self.wait(10)
        self.save_screenshot("dazn_shop_menuflow", "New Bot")

    def courtside1891(self):
        self.wait_for_element_present(self.courtside_btw, timeout=None)
        self.click(self.courtside_btw, timeout=None)
        self.save_screenshot("dazn_courtside", "New Bot")

    def Danzflow(self):
        self.wait_for_element_present(self.dazn_button_x, timeout=None)
        self.click(self.dazn_button_x, timeout=None)
        self.save_screenshot("dazn_menuflow", "New Bot")

    def Technical_questions(self):
        self.wait_for_element_present(self.TechnicalQuestions_btw, timeout=None)
        self.click(self.TechnicalQuestions_btw, timeout=None)
        self.save_screenshot("Technical_questions", "New Bot")

    def Manage_devices(self):
        self.wait_for_element_present(self.Manag_devices_btw, timeout=None)
        self.click(self.Manag_devices_btw, timeout=None)
        self.wait_for_element_present(self.windows_device, timeout=None)
        self.click(self.windows_device, timeout=None)
        self.save_screenshot("Manage_devices", "New Bot")

    def remove_dev(self):
        self.wait_for_element_present(self.remove_device, timeout=None)
        self.click(self.remove_device, timeout=None)
        self.wait_for_element_present(self.windows_device, timeout=None)
        self.click(self.windows_device, timeout=None)
        self.wait_for_element_present(self.contact_suport_btw, timeout=None)
        self.save_screenshot("remove_dev", "New Bot")

    def remov_dev1(self):
        self.wait_for_element_present(self.yes_btw,timeout=None)
        self.click(self.yes_btw, timeout=9)
        self.save_screenshot("remov_dev1", "New Bot")

    def remov_dev2(self):
        self.wait_for_element_present(self.no_btw,timeout=None)
        self.click(self.no_btw, timeout=9)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("remov_dev2", "New Bot")

    def remov_dev3(self):
        self.wait_for_element_present(self.main_menu_btw, timeout=None)
        self.click(self.main_menu_btw, timeout=None)
        self.wait_for_element_present(self.courtside_btw, timeout=None)
        self.save_screenshot("remov_dev3", "New Bot")

    def remov_dev4(self):
        self.wait_for_element_present(self.contact_suport_btw, timeout=None)
        self.click(self.contact_suport_btw, timeout=None)
        self.wait_for_element_present(self.support_text_btw, timeout=None)
        self.save_screenshot("remov_dev4", "New Bot")

    def signout_devices(self):
        self.wait_for_element_present(self.signout_device, timeout=None)
        self.click(self.signout_device, timeout=None)
        self.wait_for_element_present(self.main_menu_btw, timeout=None)
        self.save_screenshot("signout_devices", "New Bot")

    def signout1(self):
        self.wait_for_element_present(self.signmeout_btw, timeout=None)
        self.click(self.yes_btw, timeout=9)
        self.save_screenshot("signout1", "New Bot")

    def signout2(self):
        self.wait_for_element_present(self.no_btw, timeout=None)
        self.click(self.no_btw, timeout=0)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("signout2", "New Bot")

    def signout3(self):
        self.wait_for_element_present(self.main_menu_btw, timeout=None)
        self.click(self.main_menu_btw, timeout=None)
        self.wait_for_element_present(self.courtside_btw, timeout=None)
        self.save_screenshot("signout3", "New Bot")

    def signout4(self):
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.I_NeedMoreHelp_btw, timeout=None)
        self.wait_for_element_present(self.support_text_btw, timeout=None)
        self.save_screenshot("signout4", "New Bot")

    def signout5(self):
        self.wait_for_element_present(self.main_menu_btw, timeout=None)
        self.click(self.main_menu_btw, timeout=None)
        self.wait_for_element_present(self.support_text_btw, timeout=None)
        self.save_screenshot("signout5", "New Bot")








    def Manage_Sub(self):
        self.wait_for_element_present(self.Manage_your_subscription_btw, timeout=None)
        self.click(self.Manage_your_subscription_btw, timeout=None)
        self.save_screenshot("Manage_Sub", "New Bot")

    def payments(self):
        self.wait_for_element_present(self.Payments_btw, timeout=None)
        self.click(self.Payments_btw, timeout=None)
        self.wait_for_element_present(self.main_menu_btw, timeout=None)
        self.save_screenshot("Payments", "New Bot")

    def about_dazn(self):
        self.wait_for_element_present(self.About_Dazn_btw, timeout=None)
        self.click(self.About_Dazn_btw, timeout=None)
        self.wait_for_element_present(self.main_menu_btw, timeout=None)

    def SignIn(self):
        self.wait_for_element_present(self.Signin_issues, timeout=None)
        self.click(self.Signin_issues, timeout=None)
        self.save_screenshot("SignIn", "New Bot")

    def paywallflow(self):
        self.wait_for_element_present(self.PayWallBtw, timeout=None)
        self.click(self.PayWallBtw, timeout=None)
        self.save_screenshot("paywallflow", "New Bot")


    def is_device_supported(self):
        self.wait_for_element_present(self.is_device_supported_btw, timeout=None)
        self.click(self.is_device_supported_btw, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("about_dazn", "New Bot")

    def Supported_devices(self):
        self.wait_for_element_present(self.supported_device_btw, timeout=None)
        self.click(self.supported_device_btw, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Supported_devices", "New Bot")

    def Subscription_plans1(self):
        self.wait_for_element_present(self.subscription_plans_btw, timeout=None)
        self.click(self.subscription_plans_btw, timeout=None)
        self.wait_for_element_present(self.interested_in_sub_plans, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.buy_plan, timeout=None)
        self.click(self.buy_plan, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.click(self.yes_btw, timeout=None)
        self.save_screenshot("Subscription_plans", "New Bot")

    def Subscription_plans2(self):
        self.wait_for_element_present(self.subscription_plans_btw, timeout=None)
        self.click(self.subscription_plans_btw, timeout=None)
        self.wait_for_element_present(self.interested_in_sub_plans, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.buy_plan, timeout=None)
        self.click(self.buy_plan, timeout=None)
        self.wait_for_element_present(self.no_create_accn, timeout=None)
        self.click(self.no_create_accn, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Subscription_plans2", "New Bot")

    def Accepted_payments1(self):
        self.wait_for_element_present(self.accepted_payments_btw,timeout=None)
        self.click(self.accepted_payments_btw, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.buy_plan, timeout=None)
        self.click(self.buy_plan, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.click(self.yes_btw, timeout=None)
        self.save_screenshot("Accepted_payments", "New Bot")

    def Accepted_payments2(self):
        self.wait_for_element_present(self.accepted_payments_btw, timeout=None)
        self.click(self.accepted_payments_btw, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.buy_plan, timeout=None)
        self.click(self.buy_plan, timeout=None)
        self.wait_for_element_present(self.no_create_accn, timeout=None)
        self.click(self.no_create_accn, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Accepted_payments", "New Bot")

    def Accepted_payments3(self):
        self.wait_for_element_present(self.accepted_payments_btw, timeout=None)
        self.click(self.accepted_payments_btw, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_no, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Accepted_payments3", "New Bot")



    def update_payments(self):
        self.wait_for_element_present(self.Update_Payments_btw, timeout=None)
        self.click(self.Update_Payments_btw, timeout=None)
        #blocker
        self.save_screenshot("Update_Payments", "New Bot")

    def refundflow1(self):
        self.wait_for_element_present(self.Refund_btw, timeout=None)
        self.click(self.Refund_btw, timeout=None)
        self.wait_for_element_present(self.Yes_I_got_it, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.Yes_I_got_it, timeout=None)
        #blocker
        self.save_screenshot("Refund1", "New Bot")

    def refundflow2(self):
        self.wait_for_element_present(self.Refund_btw, timeout=None)
        self.click(self.Refund_btw, timeout=None)
        self.wait_for_element_present(self.Yes_I_got_it, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.I_NeedMoreHelp_btw, timeout=None)
        #blocker
        self.save_screenshot("Refund2", "New Bot")

    def giftcodesflow(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.click(self.yes_btw, timeout=None)
        #blocker
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcodes", "New Bot")

    def giftcodeflow1(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes, timeout=None)
        self.wait_for_element_present(self.no_btw, timeout=None)
        self.click(self.no_btw, timeout=None)
        self.wait_for_element_present(self.stream_yes,timeout=None)
        self.wait_for_element_present(self.stream_no,timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcode1", "New Bot")

    def giftcodeflow2(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes, timeout=None)
        self.wait_for_element_present(self.no_btw, timeout=None)
        self.click(self.no_btw, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.stream_no, timeout=None)
        self.click(self.stream_no, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcode2", "New Bot")

    def giftcodeflow3(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.I_NeedMoreHelp_btw, timeout=None)
        self.wait_for_element_present(self.I_want_to_talk_to, timeout=None)
        self.wait_for_element_present(self.I_want_to_buy_gift, timeout=None)
        self.click(self.I_want_to_buy_gift, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.stream_no, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcode3", "New Bot")

    def giftcodeflow4(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.I_NeedMoreHelp_btw, timeout=None)
        self.wait_for_element_present(self.I_want_to_talk_to, timeout=None)
        self.wait_for_element_present(self.I_want_to_buy_gift, timeout=None)
        self.click(self.I_want_to_buy_gift, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.stream_no, timeout=None)
        self.click(self.stream_no, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcode4", "New Bot")

    def giftcodeflow5(self):
        self.wait_for_element_present(self.Gift_codes, timeout=None)
        self.click(self.Gift_codes,timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.click(self.I_NeedMoreHelp_btw, timeout=None)
        self.wait_for_element_present(self.I_want_to_talk_to, timeout=None)
        self.wait_for_element_present(self.I_want_to_buy_gift, timeout=None)
        self.click(self.I_want_to_talk_to, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Giftcode5", "New Bot")

    def signinflows(self):
        self.wait_for_element_present(self.Signin_issues, timeout=None)
        self.click(self.Signin_issues, timeout=None)
        self.wait_for_element_present(self.ForgotUsername,timeout=None)
        self.click(self.ForgotUsername, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.save_screenshot("Signin_flows", "New Bot")

    def signinflows1(self):
        self.wait_for_element_present(self.Signin_issues, timeout=None)
        self.click(self.Signin_issues, timeout=None)
        self.wait_for_element_present(self.ForgotUsername,timeout=None)
        self.click(self.ForgotUsername, timeout=None)
        self.wait_for_element_present(self.stream_no, timeout=None)
        self.click(self.stream_no, timeout=None)
        self.wait_for_element_present(self.no_btw,timeout=None)
        self.save_screenshot("Signin_flows1", "New Bot")

    def signinflows2(self):
        self.wait_for_element_present(self.Signin_issues, timeout=None)
        self.click(self.Signin_issues, timeout=None)
        self.wait_for_element_present(self.ForgotPassword, timeout=None)
        self.click(self.ForgotPassword, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.click(self.yes_btw, timeout=None)
        #blocker for dummy test account goes to handoff
        self.save_screenshot("Signin_flows2", "New Bot")

    def signinflows3(self):
        self.wait_for_element_present(self.Signin_issues, timeout=None)
        self.click(self.Signin_issues, timeout=None)
        self.wait_for_element_present(self.ForgotPassword, timeout=None)
        self.click(self.ForgotPassword, timeout=None)
        self.wait_for_element_present(self.no_btw, timeout=None)
        self.click(self.no_btw, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("Signin_flows3", "New Bot")

    def DanzShop(self):
        self.wait_for_element_present(self.DanzShop_btw, timeout=None)
        self.click(self.DanzShop_btw, timeout=None)
        self.wait_for_element_present(self.Order_Status, timeout=None)
        self.save_screenshot("DanzShop", "New Bot")

    def order_status(self):
        self.wait_for_element_present(self.Order_Status, timeout=None)
        self.click(self.Order_Status, timeout=None)
        self.wait(7)
        self.save_screenshot("Order_Status1", "New Bot")

    def official_merchandise(self):
        self.wait_for_element_present(self.Official_Merchandise, timeout=None)
        self.click(self.Official_Merchandise, timeout=None)
        self.wait(7)
        self.save_screenshot("Official_Merchandise", "New Bot")

    def get_help(self):
        self.wait_for_element_present(self.Get_help, timeout=None)
        self.click(self.Get_help, timeout=None)
        self.wait(7)
        self.save_screenshot("Get_Help", "New Bot")

    def streaming_issues(self):
        self.wait_for_element_present(self.Streaming_Issues_btw, timeout=None)
        self.click(self.Streaming_Issues_btw, timeout=None)
        self.wait_for_element_present(self.Streaming_multiple_devices, timeout=None)
        self.save_screenshot("Streaming_issues", "New Bot")

    def live_stream(self):
        self.wait_for_element_present(self.Live_stream_btw, timeout=None)
        self.click(self.Live_stream_btw, timeout=None)
        self.wait_for_element_present(self.Streaming_multiple_devices, timeout=None)
        self.save_screenshot("Live_stream", "New Bot")

    def OnDemand_video(self):
        self.wait_for_element_present(self.OnDemand_video_btw, timeout=None)
        self.click(self.OnDemand_video_btw, timeout=None)
        self.wait_for_element_present(self.Streaming_multiple_devices, timeout=None)
        self.save_screenshot("OnDemand_video", "New Bot")

    def stream_multidevice(self):
        self.wait_for_element_present(self.Streaming_multiple_devices, timeout=None)
        self.click(self.Streaming_multiple_devices, timeout=None)
        self.wait_for_element_present(self.stream_itsotherdevice, timeout=None)
        self.save_screenshot("steam_multidevice", "New Bot")

    def stream_flows1(self):
        self.wait_for_element_present(self.stream_itsotherdevice, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes,timeout=None)
        self.wait_for_element_present(self.internet_met_requirements, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.mydevice_and_app_are_btw, timeout=None)
        self.wait_for_element_present(self.working_now, timeout=None)
        self.click(self.working_now, timeout=None)
        self.wait_for_element_present(self.yes_btw, timeout=None)
        self.save_screenshot("stream_flows1", "New Bot")

    def stream_flows2(self):
        self.wait_for_element_present(self.stream_itsotherdevice, timeout=None)
        self.click(self.stream_itsotherdevice, timeout=None)
        self.wait_for_element_present(self.signin_blocker_msg, timeout=None)
        self.save_screenshot("stream_flows2", "New Bot")

    def stream_flow3(self):
        self.wait_for_element_present(self.stream_itsotherdevice, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.internet_met_requirements, timeout=None)
        self.click(self.stream_no, timeout=None)
        self.wait_for_element_present(self.isthereanythingelsebtw, timeout=None)
        self.save_screenshot("stream_flows3", "New Bot")

    def stream_flows4(self):
        self.wait_for_element_present(self.stream_itsotherdevice, timeout=None)
        self.wait_for_element_present(self.stream_yes, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.internet_met_requirements, timeout=None)
        self.click(self.stream_yes, timeout=None)
        self.wait_for_element_present(self.mydevice_and_app_are_btw, timeout=None)
        self.wait_for_element_present(self.updated_but_help_btw, timeout=None)
        self.click(self.updated_but_help_btw, timeout=None)
        self.wait(10)
        self.save_screenshot("stream_flows4", "New Bot")
        #self.right_click(selector, by="css selector", timeout=None)













    def Handoff_to_support(self):
        self.wait_for_element_present(self.Handoff_to_support, timeout=None)
        self.click(self.Handoff_to_support, timeout=None)
        self.save_screenshot("Handoff_to_support", "New Bot")

    def locked_content(self):
        self.wait_for_element_present(self.Located_content_btw, timeout=None)
        self.click(self.Located_content_btw, timeout=None)
        self.save_screenshot("locked_content", "New Bot")

    def Dazn_app(self):
        self.wait_for_element_present(self.Dazn_app_btw, timeout=None)
        self.click(self.Dazn_app_btw, timeout=None)
        self.save_screenshot("Dazn_app", "New Bot")

    def Android_device(self):
        self.wait_for_element_present(self.Android_device_btw, timeout=None)
        self.click(self.Android_device_btw, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Android_device", "New Bot")

    def Apple_device(self):
        self.wait_for_element_present(self.Apple_device_btw, timeout=None)
        self.click(self.Apple_device_btw, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Apple_device", "New Bot")

    def Smart_Tv(self):
        self.wait_for_element_present(self.Smart_Tv, timeout=None)
        self.click(self.Smart_Tv, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Smart_Tv", "New Bot")

    def Game_console(self):
        self.wait_for_element_present(self.Game_console, timeout=None)
        self.click(self.Game_console, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Game_console", "New Bot")

    def Web_browser(self):
        self.wait_for_element_present(self.Web_browser, timeout=None)
        self.click(self.Web_browser, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Web_browser", "New Bot")

    def Other(self):
        self.wait_for_element_present(self.Other_btw, timeout=None)
        self.click(self.Other_btw, timeout=None)
        self.wait_for_element_present(self.I_NeedMoreHelp_btw, timeout=None)
        self.save_screenshot("Other", "New Bot")












