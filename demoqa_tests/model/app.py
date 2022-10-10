from selene import have
from selene.support.shared import browser


def given_opened_text_box():
    browser.open('/text-box')
    ads = browser.all('[id^=google_ads_][id$=container_]')
    # .should(have.size_greater_than_or_equal(3)) #явное ожиданиие появления трех блоков реклам
    # if ads.wait_until(have.size_greater_than_or_equal(3)): #ожидание появления реклам
    if ads.matching(have.size_greater_than_or_equal(3)):  # оптимизация ожидания, если я знаю. что все что надо - появилось сразу
        ads.perform(command.js.remove)
    # browser.execute_script('document.querySelectorALl("[id^=google_ads_][id$=container_]").forEach(element=>element.remove())') #костыль на отключение рекламы
