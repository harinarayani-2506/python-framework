*** Settings ***
Library    SeleniumLibrary
Library    ../Page_Definitions/Feature_Definitions.py

*** Variables ***
${current_webdriver}    Chrome
${featured_List}    
${popularTopics_List}
${tools_List}
${allProducts_dict}
${support_List}

*** Keywords ***
Initialize webdriver
    ${current_webdriver}=    Get Library Instance     name=SeleniumLibrary    
    Set Suite Variable    ${current_webdriver}    ${current_webdriver}
    
Open BrowserStack Application and scroll to Test your websites and mobile Apps
    Open Browser    url=https://www.browserstack.com    browser=Chrome
    Initialize webdriver
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://button[@id='developers-dd-toggle']     
    Mouse Over    xpath://button[@id='developers-dd-toggle']
    Click Element    xpath://*[@id='developers-dd-menu']/div/div[1]/a
    Wait Until Element Is Visible    locator=//h1[@class='hero-section__heading']

Get Featured Application names
    ${featured_List}    Get Documentation application names    ${current_webdriver}    rootLocator=//div[@class='hero-section__featured-products-subsection']    headingName_Locator=//h3[@class='hero-section__subsection-heading']    appName_List_Locator=//ul[@class='hero-section__featured-products-list']//div[@class='hero-section__featured-product-header']//p
    Set Suite Variable    ${featured_List}    ${featured_List}
#    Log    ${featured_List}

Get AllProducts Application Names
    Scroll Element Into View    locator=//div[@class="all-products__content"]//h2
    Wait Until Element Is Visible    locator=//div[@class="all-products__content"]//h2
    ${current_webdriver}=    Get Library Instance    name=SeleniumLibrary
    ${allProducts_dict}=    Get sub headings of all products    ${current_webdriver}
    Set Suite Variable    ${allProducts_dict}    ${allProducts_dict}
#    Log    ${allProducts_dict}

Get Popular Topics Application names
    Scroll Element Into View    locator=//section[@class='popular-topics']
    Wait Until Element Is Visible    locator=//section[@class='popular-topics']
    ${popularTopics_List}    Get Documentation application names    ${current_webdriver}    rootLocator=//section[@class='popular-topics']    headingName_Locator=//h2[@class='popular-topics__heading']    appName_List_Locator=//ul[@class='popular-topics__list']//a//div[@class='condensed-card__text-container']//p[@class='condensed-card__text-name']
    Set Suite Variable    ${popularTopics_List}    ${popularTopics_List}
#    Log    ${popularTopics_List}

Get Tools Application names
    Scroll Element Into View    locator=//section[@class='tools']
    Wait Until Element Is Visible    locator=//section[@class='tools']
    ${tools_List}    Get Documentation application names    ${current_webdriver}    rootLocator=//section[@class='tools']    headingName_Locator=//h2[@class='tools__heading']    appName_List_Locator=//ul[@class='tools__list']//div[@class='minimal-card__text-container']//p[@class='minimal-card__text-name']
    Set Suite Variable    ${tools_List}    ${tools_List}
#    Log    ${tools_List}

Get Support Application names
    Scroll Element Into View    locator=//section[@class='support']
    Wait Until Element Is Visible    locator=//section[@class='support']
    ${support_List}    Get Documentation application names    ${current_webdriver}    rootLocator=//section[@class='support']    headingName_Locator=//h2[@class='support__heading']    appName_List_Locator=//ul[@class='support__list']//div[@class='condensed-card__text-container']//p[@class='condensed-card__text-name']
    Set Suite Variable    ${support_List}    ${support_List}
#    Log    ${support_List}

Display All Details of Documentation Page
    Log    ${featured_List}
    Log    ${allProducts_dict}
    Log    ${popularTopics_List}
    Log    ${tools_List}
    Log    ${support_List}

    
