def login(ctx, username='admin', email='admin@gmail.com',password='Admin123'):
    ctx.browser.get(ctx.server_address + "/login")
    uname = ctx.browser.find_element_by_name('username')
    email1 = ctx.browser.find_element_by_name('email')
    passwd = ctx.browser.find_element_by_name('password')
    login_button = ctx.browser.find_element_by_name('login')
    uname.clear();
    email1.clear();
    passwd.clear();
    uname.send_keys(username)
    email1.send_keys(email)
    passwd.send_keys(password)
    login_button.click()

def logout(ctx):
    pass