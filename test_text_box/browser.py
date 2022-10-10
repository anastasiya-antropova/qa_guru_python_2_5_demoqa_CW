from selene import be, have
from selene.support.shared import browser

from demoqa_tests.model import app


def test_submit_user_details():
    app.given_opened_text_box() #убираем лишнее из теста, только вызов метода
    #browser.switch_to.window() #переход на другую вкладку
    #browser.driver.     #можно выбрать команду, которой не хватает через стандартный селениум
    browser.should(have.title('ToolsQA'))
    # хорошая практика - это
    browser.element('.main-header').should(be.visible)  # без привязки к тексту

    #плохо привязываться к тексту!!!
#    browser.element('.main-header').should(have.text('Text Box'))
#    browser.element('//*[.="Text Box"]') #альтернативный поиск текста через xpath или
#    browser.element('//*[text() = "Text Box"]').should(be.visible) #более точный, тоже альтернативный поиск текста через xpath
#    browser.element(by.text('Text Box')).should(be.visible)#сокр запись предыдущего

    #плохая практика - перечислять все категории сразу
    #browser.with_(timeout=5).all('#userForm input, #userForm textarea').should(have.size(4))  # таймаут для строки, место в строке не важно

    #хорошая практика - перечислять по вложенности
    browser.element('#userForm').all('input, textarea').should(have.size(4))  # таймаут для строки, место в строке не важно
    #browser.all('.form-label').filtered_by(have.text('Address'))[1] #элемент из списка
    browser.all('.form-label').filtered_by(have.text('Address'))[1].should(have.text('Permanent Address'))#для 1го элемента вместо [1] - .first
    browser.all('.form-label').element_by(have.text('Address')).should(have.text('Current Address'))#альтернатива для 1го элемента

    browser.element('#userName').set_value('bingo')
    #browser.element('#submit').click() #предпочтительный, консистентный селектор
#    browser.element(by.id('submit')).click() #альтернативный путь через by, но он не предпочтителен

