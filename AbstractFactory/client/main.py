from AbstractAndroidFactory import AbstractAndroidFactory
from AbstractIosFactory import AbstractIosFactory


def Deploy_Android():
    Abc= AbstractAndroidFactory()
    Button = Abc.create_Button().create()
    Button.click()

    #Abc2=AbstractAndroidFactory
    #checkbox_Button = Abc2.create_checkbox().create()
    #checkbox_Button.click()
    


if __name__ == '__main__':
    Deploy_Android()