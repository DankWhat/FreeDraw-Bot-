import settings
import drawing

def main():
    print("Welcome to Free Draw Bot!")

    # Load settings
    settings.load_settings()

    while True:
        print("--------------------")
        print("Please choose an option:")
        print("(1) Draw from data file")
        print("(2) Draw from image")
        print("(3) Make your own data file")
        print("(4) See preview")
        print("(5) Change settings")
        print("(6) Exit")

        option = input("Enter option: ")

        if option == "1":
            drawing.draw_from_data_file()
        elif option == "2":
            drawing.draw_from_image()
        elif option == "3":
            drawing.make_data_file()
        elif option == "4":
            drawing.preview()
        elif option == "5":
            settings.change_settings()
        elif option == "6":
            print("Exiting Free Draw Bot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
