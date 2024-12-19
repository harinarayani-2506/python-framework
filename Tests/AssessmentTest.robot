*** Settings ***
Resource    ../resources/Page_Keywords/Updated_Feature_Keywords.resource

*** Test Cases ***

Compare BrowserStack Application names
    Open BrowserStack Application and scroll to Test your websites and mobile Apps
    Get Featured Application names
    Get AllProducts Application Names
    Get Popular Topics Application names
    Get Tools Application names
    Get Support Application names
    Display All Details of Documentation Page
    Close Browser