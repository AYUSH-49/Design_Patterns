from BuilderDirectory import BuilderDirectory

if __name__ == "__main__":
    # Create a Builder instance
    TypeOfComputer = input("Enter the type of computer you want to build (Gaming/Normal): ").strip().lower()
    builder = BuilderDirectory(TypeOfComputer.capitalize()).get_builder().built()
    print(builder)