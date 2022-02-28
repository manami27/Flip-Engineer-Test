from importlib.resources import contents
from multiprocessing import context
from time import sleep
from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()    

@when('open flip landing page')
def openHomepage(context):
    context.driver.get('https://flip.id/')

@when('verify success open landing page')
def verifyHomepage(context):
    assert "Transfer Antar Bank Tanpa Biaya - Flip" in context.driver.title
    print("Success open Flip landing page")

@when('navigate to masuk menu')
def masukMenu(context):
    try:
        context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/button').click()
        sleep(10)      
    except:
        context.driver.close()
        assert False, "Test is failed in click Masuk button"

@then('verify success open login page')
def verifyLoginPage(context):
    try:
        assert "Login dan Mulai Kirim Uang Tanpa Biaya Admin - Flip" in context.driver.title
        print("Success open Flip landing page")
        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test is failed in verify open login page"

@when('navigate to produk menu')
def produkMenu(context):
    try:
        context.driver.find_element_by_css_selector('.dropdown').click()
        layananflip = context.driver.find_element_by_class_name('sc-cHSUfg').is_displayed()
        assert layananflip is True, "Success open product menu list"
    except:
        context.driver.close()
        assert False, "Test is failed in open product list"

@then('verify success open layanan flip page')
def openLayananFlip(context):
    try:
        context.driver.find_element_by_css_selector("a[href='https://business.flip.id/']").click()
        assert "Flip for Business | Solusi Manajemen Transaksi Bisnis Terbaik" in context.driver.title
        print("Success in open layanan flip")
        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test is failed in open layanan flip"

@when('navigate to karir menu')
def karirMenu(context):
    try:
        context.driver.find_element_by_link_text('Karir').click()
    except:
        context.driver.close()
        assert False, "Test is failed in click Karir menu"

@then('verify success open karir page')
def openKarirPage(context):
    try:
        browserTabs = context.driver.window_handles
        context.driver.switch_to.window(browserTabs[1])
        assert "Flip Careers" in context.driver.title
        print("Success open Flip Careers page")
        context.driver.quit()
    except:
        context.driver.close()
        assert False, "Test is failed in open Flip Careers page"

print('Test Completed')


