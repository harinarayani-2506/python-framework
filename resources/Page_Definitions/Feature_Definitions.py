import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class   Feature_Definitions:

    @keyword('Get Documentation application names')
    def Documentation_Application_Names(self, webdriver : SeleniumLibrary.SeleniumLibrary, rootLocator, headingName_Locator, appName_List_Locator):
        self.Browser_instance = webdriver
        headingLocator = rootLocator+headingName_Locator
        documentation_ItemName_WebElement : WebElement = self.Browser_instance.find_element(locator=headingLocator)
        documentation_Item_Dict = {}
        productNames_List=[]
        documentation_ItemName = documentation_ItemName_WebElement.text
        listOfItems_Locator = rootLocator+appName_List_Locator
        listOfItems = self.Browser_instance.find_elements(locator=listOfItems_Locator)
        
        for i in range(1,len(listOfItems)+1):
            locatorValue = "("+listOfItems_Locator+")["+str(i)+"]"
            productName : WebElement = documentation_ItemName_WebElement.find_element(By.XPATH,locatorValue)
            productNames_List.append(productName.text)
        documentation_Item_Dict[documentation_ItemName]=productNames_List
        return documentation_Item_Dict
    
    @keyword('Get sub headings of all products')
    def getSubHeadingsWebTesting(self, webdriver: SeleniumLibrary.SeleniumLibrary):
        self.Browser_instance = webdriver
        sub_headings: list[WebElement] = self.Browser_instance.find_elements("//ul[@class='all-products__testing-categories']//h3")
        heading_title = [title.text for title in sub_headings]
        result_dictionary = {}
        for i, heading in enumerate(heading_title, start=0):
            products: list[WebElement] = self.Browser_instance.find_elements(f"(//ul[@class='testing-category__products'])[1 + {i}]/li/a")
            product_title = [product.text for product in products]
            result_dictionary[heading] = product_title
        return result_dictionary
    

    '''def Get_AllProducts_ApplicationNames(self, webdriver : SeleniumLibrary.SeleniumLibrary, rootLocator, headingName_Locator, appName_List_Locator):
        self.Browser_instance = webdriver
        headingLocator = rootLocator+headingName_Locator
        allProducts_Heading_WebElements = self.Browser_instance.find_elements(locator=headingLocator)
        allProducts_Item_Dict = {}
        productNames_List=[]
        for i in range(1,len(allProducts_Heading_WebElements)+1):
            locator = "("+allProducts_Heading_WebElements+")["+str(i)+"]"
            heading = self.Browser_instance.find_element(locator)
            productNames_List[heading.text] = {}
        



        listOfItems_Locator = rootLocator+appName_List_Locator
        listOfItems = self.Browser_instance.find_elements(locator=listOfItems_Locator)
        allProducts_rootLocator = self.Browser_instance.find_element(locator=rootLocator)

        for i in range(1,len(listOfItems)+1):
            locatorValue = "("+listOfItems_Locator+")["+str(i)+"]"
            productName : WebElement = allProducts_rootLocator.find_element(By.XPATH,locatorValue)
            productNames_List.append(productName.text)
        documentation_Item_Dict[documentation_ItemName]=productNames_List
        return documentation_Item_Dict'''

    













    
    @keyword('Compare Web and Mobile Apps and Get the Common List')
    def compareWebAndMobileAppsAndGetTheCommonList(self,featured_List, web_List, app_List):
        common_elements_webTesting = list(set(featured_List) & set(web_List))
        common_elements_AppTesting = list(set(featured_List) & set(app_List))
        dictionaryValue={}
        dictionaryValue["Featured_WebTesting"] = common_elements_webTesting
        dictionaryValue["Featured_AppTesting"] = common_elements_AppTesting

        return dictionaryValue

