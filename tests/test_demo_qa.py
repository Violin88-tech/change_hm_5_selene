from selene import browser, have, command
import os
from os.path import dirname, abspath

PATH_RES = os.path.join(dirname(dirname(abspath(__file__))), "resources")

def test_demo_qa():
    browser.open('/automation-practice-form')

    # Fill in personal data

    browser.element('#firstName').type('Vika')
    browser.element('#lastName').type('Islenteva')
    browser.element('#userEmail').type('email@email.email')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('7777777777')

    # Fill in date birth 1990-01-01

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="1991"]').click()
    browser.element('.react-datepicker__month-select').element('[value="2"]').click()
    browser.element('.react-datepicker__day--003').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('.form-file-label').perform(command.js.scroll_into_view)
    browser.all('[for^=hobbies-checkbox-3]').element_by(have.exact_text('Music')).click()

    # Add picture
    browser.element('[for="uploadPicture"]').should(have.exact_text('Select picture'))
    browser.element('.form-file-label').perform(command.js.scroll_into_view)
    browser.element('[type=file]').send_keys(os.path.abspath('resourses/_2224643_orig.jpg'))



    browser.element('#currentAddress').type('45 Current Address')
    #
    # # Select state and city
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('#currentAddress').press_tab()
    browser.element('#state').click()
    browser.element('#state').element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#stateCity-wrapper').element('#react-select-4-option-0').click()
    #
    # # Submit form
    browser.element('#submit').press_enter()
    #
    # # Check data
    browser.element('.table-responsive').all('td:nth-child(2)')[0].should(have.text('Vika Islenteva'))
    browser.element('.table-responsive').all('td:nth-child(2)')[1].should(have.text('email@email.email'))
    browser.element('.table-responsive').all('td:nth-child(2)')[2].should(have.text('Female'))
    browser.element('.table-responsive').all('td:nth-child(2)')[3].should(have.text('7777777777'))
    browser.element('.table-responsive').all('td:nth-child(2)')[4].should(have.text('03 March,1991'))
    browser.element('.table-responsive').all('td:nth-child(2)')[5].should(have.text('Computer Science'))
    browser.element('.table-responsive').all('td:nth-child(2)')[6].should(have.text('Music'))
    browser.element('.table-responsive').all('td:nth-child(2)')[7].should(have.text('_2224643_orig.jpg'))
    browser.element('.table-responsive').all('td:nth-child(2)')[8].should(have.text('45 Current Address'))
    browser.element('.table-responsive').all('td:nth-child(2)')[9].should(have.text('NCR Delhi'))

