from page_objects.newbot_stag import NewBot

class ZenBotStag(NewBot):

    # def test_Daznflow(self):
    #     self.signin()
    #     self.start_chart()
    #     self.verify_initial_greet()
    #     self.Danzflow()
    #
    #
    # def test_nfl_flow(self):
    #     self.signin()
    #     self.start_chart()
    #     self.verify_initial_greet()
    #     self.nfl_flow()

    def test_dazn_shop_flow(self):
        self.signin()
        self.start_chart()
        self.verify_initial_greet()
        self.DanzShop()
        self.order_status()

    def test_dazn_shop_flow1(self):
        self.signin()
        self.start_chart()
        self.verify_initial_greet()
        self.DanzShop()
        self.official_merchandise()

    def test_dazn_shop_flow3(self):
        self.signin()
        self.start_chart()
        self.verify_initial_greet()
        self.DanzShop()
        self.get_help()






