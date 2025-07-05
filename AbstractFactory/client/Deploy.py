from factory.AbstractAndroidFactory import AbstractAndroidFactory
from factory.AbstractIosFactory import AbstractIosFactory


class Deploy():
    def __init__(self, Platform):
        self.Platform = Platform

    def deploy(self):
        if self.Platform == "android":
            Elements =input("Enter the elements to deploy for Android Button/Checkbox: ")
            if Elements.lower() == "button":
                return AbstractAndroidFactory().create_button()
            elif Elements.lower() == "checkbox":
                return  AbstractAndroidFactory().create_checkbox()
            else:
                print("Invalid element for Android. Please choose either 'Button' or 'Checkbox'.")
            
        elif self.Platform == "ios":
            Elements = input("Enter the elements to deploy for Ios Button/Checkbox: ")
            if Elements.lower() == "button":
                return AbstractIosFactory().create_button()
            elif Elements.lower() == "checkbox":
                return AbstractIosFactory().create_checkbox()
            else:
                print("Invalid element for Ios. Please choose either 'Button' or 'Checkbox'.")
            
        else:
            print("Invalid platform. Please choose either 'Android' or 'Ios'.")