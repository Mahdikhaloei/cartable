from utils.testcases import AppAPITestCase


class UserViewSetTestCase(AppAPITestCase):
    def setUp(self):
        super().setUp()
        self.user_me_url = "/api/v1/users/me/"
