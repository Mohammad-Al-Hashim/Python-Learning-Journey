#NOTE: This file tracks my code evolution. The active version is at the bottom.

#V1:
if False:
    user_library = []
    user_book1=input("Enter the name of a book you own: \n")
    user_library.append(user_book1)
    user_book2=input("Enter the name of another book you own. OR: press enter to skip \n")
    if user_book2:
        user_library.append(user_book2)
        print(f"Your library: {user_library}")
        wishlist = []
        book_wish1 = input("Enter the name of a book you wish to have in the future: \n")
        wishlist.append(book_wish1)
        book_wish2 = input("Enter the name of another book you wish to have in the future. OR: press enter to skip \n")
        if book_wish2:
            wishlist.append(book_wish2)
            print(f"Your wishlist: {wishlist}")
            acquired = input("Enter the name of a book from your wishlist that you've actually acquired. OR: press enter to skip \n")
            if acquired:
                wishlist.remove(acquired)
                user_library.append(acquired)
                print(f"Your updated library: {user_library}. Your updated wishlist: {wishlist}")
                donate = input("Enter the name of a book from your library you wish to donate. OR: press enter to skip \n")
                if donate:
                    user_library.remove(donate)
                    print(f"Final library after donation: {user_library}")
                else:
                    print(f"Final library: {user_library}")
            else:
                print(f"Your updated library: {user_library}. Your updated wishlist: {wishlist}")
        else:
            print(f"Your wishlist: {wishlist}")
    else:
        print(f"Your library: {user_library}")

#V2:
user_library = []
wishlist = []
user_book = input("Enter the name of a book you own: \n")
user_library.append(user_book)
user_book = input("Enter the name of another book you own. OR: press enter to skip \n")
if user_book:
    user_library.append(user_book)
    print(f"Your library: {user_library}")
else:
    print(f"Your library: {user_library}")
user_book = input("Enter the name of a book you wish to have in the future: \n")
wishlist.append(user_book)
user_book = input("Enter the name of another book you wish to have in the future. OR: press enter to skip \n")
if user_book:
    wishlist.append(user_book)
    print(f"Your wishlist: {wishlist}")
else:
    print(f"Your wishlist: {wishlist}")
user_book = input("Enter the name of a book from your wishlist that you've actually acquired. OR: press enter to skip \n")
if user_book in wishlist:
    wishlist.remove(user_book)
    user_library.append(user_book)
    print(f"Your updated library: {user_library}. Your updated wishlist: {wishlist}")
else:
    print("You didn't acquire any book from your wishlist yet.")
    print(f"Your updated library: {user_library}. Your updated wishlist: {wishlist}")
donate = input("Enter the name of a book from your library you wish to donate. OR: press enter to skip \n")
if donate in user_library:
    user_library.remove(donate)
    print(f"Final library after donation: {user_library}")
else:
    print("You didn't donate a book from your library.")
    print(f"Final library: {user_library}")


