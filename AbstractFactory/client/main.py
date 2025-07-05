from AbstractFactory.client.Deploy import Deploy



if __name__ == '__main__':

    Platform = input("Enter the platform (Android/Ios): ").strip().lower()
    Deploy(Platform)

