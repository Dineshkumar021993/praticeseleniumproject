from pages.webapp.login import Login

def test_login(browser):
    login = Login(browser)
    login.username_for_login()
    login.password_for_login()
    login.login()