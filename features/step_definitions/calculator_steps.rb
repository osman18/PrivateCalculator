require 'watir-webdriver'

browser = nil


def input_click(browser, formula)
    input = Array.new
    formula = formula.gsub(' ','')
    input = formula.split('')

    for i in input
        if i === '+'
            browser.div(:id, 'btn-add').click
        elsif i === '-'
            browser.div(:id, 'btn-minus').click
        elsif i === 'x' 
            browser.div(:id, 'btn-times').click
        elsif i === '/'
            browser.div(:id, 'btn-divided').click
        elsif i === '('
            browser.div(:id, 'btn-LParenthesis').click
        elsif i === ')'
            browser.div(:id, 'btn-RParenthesis').click
        else
            browser.div(:id, 'btn-' + i).click
        end
        sleep(1.0)
    end

    browser.div(:id, 'btn-equal').click
end

Given(/^A web calculator$/) do
    browser = Watir::Browser.new
    browser.goto 'http://127.0.0.1:5000'
    browser.send_keys :f11
end

When(/^enter "(.*?)"$/) do |arg1|
    input_click(browser, arg1)
end

Then(/^get the result is (\d+)$/) do |arg1|
    result_int = browser.span(:id => 'result-int').text
    expect(result_int).to eq arg1
    browser.close
end
