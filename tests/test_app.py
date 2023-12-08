from playwright.sync_api import Page, expect
from datetime import datetime
date1 = datetime(2023,12,1,12,0)
date2 = datetime(2023,12,2,12,0)
date3 = datetime(2023,12,3,12,0)
date4 = datetime(2023,12,4,12,0)
date5 = datetime(2023,12,5,12,0)
date6 = datetime(2023,12,6,12,0)


def test_show_peeps(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    list_items = page.locator('ul')
    expect(list_items).to_have_text([
        f"post5\nuser1 {date5.strftime('%d/%m/%Y, %H:%M')}",
        f"post4\nuser2 {date4.strftime('%d/%m/%Y, %H:%M')}",
        f"post3\nuser2 {date3.strftime('%d/%m/%Y, %H:%M')}",
        f"post2\nuser1 {date2.strftime('%d/%m/%Y, %H:%M')}",
        f"post1\nuser1 {date1.strftime('%d/%m/%Y, %H:%M')}",
    ])

def test_send_peeps(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    page.fill("input[name='content']","post6")
    page.click("text=Send Peep")
    list_items = page.locator('ul')
    expect(list_items).to_have_text([
        f"post6\nuser1 {date6.strftime('%d/%m/%Y, %H:%M')}",
        f"post5\nuser1 {date5.strftime('%d/%m/%Y, %H:%M')}",
        f"post4\nuser2 {date4.strftime('%d/%m/%Y, %H:%M')}",
        f"post3\nuser2 {date3.strftime('%d/%m/%Y, %H:%M')}",
        f"post2\nuser1 {date2.strftime('%d/%m/%Y, %H:%M')}",
        f"post1\nuser1 {date1.strftime('%d/%m/%Y, %H:%M')}",
    ])

def test_send_blank_peep(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    page.click("text=Send Peep")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: You can't send a blank Peep")

def test_send_long_peep(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    long = '1'*165
    page.fill("input[name='content']",long)
    page.click("text=Send Peep")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Maximum length of a Peep is 160 characters")

def test_create_new_user_error_blank(db_connection,page,test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    page.click("text=Sign up here")
    page.click("text=Create Account")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Username cannot be blank, First name cannot be blank, Last name cannot be blank, E-mail cannot be blank, Password cannot be blank")

def test_create_new_user_error_blank(db_connection,page,test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    page.click("text=Sign up here")
    page.fill("input[name='first_name']",'user')
    page.fill("input[name='last_name']",'user')
    page.fill("input[name='username']",'user1')
    page.fill("input[name='email']",'user')
    page.fill("input[name='password']",'user')
    page.click("text=Create Account")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: This username already exists. Please choose an alternative.")

def test_create_new_user(db_connection,page,test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f'http://{test_web_address}/chitter/homepage')
    page.click("text=Sign up here")
    page.fill("input[name='first_name']",'fname3')
    page.fill("input[name='last_name']",'lname3')
    page.fill("input[name='username']",'user3')
    page.fill("input[name='email']",'email3@email.com')
    page.fill("input[name='password']",'password3')
    page.click("text=Create Account")
    header_element = page.locator('h1')
    expect(header_element).to_have_text('Welcome fname3')
    name_element = page.locator('.t-name')
    expect(name_element).to_have_text(f'Name: fname3 lname3')
    username_element = page.locator(".t-username")
    expect(username_element).to_have_text('Username: user3')
    expect(page.locator(".t-email")).to_have_text('Email: email3@email.com')