# Alvaro Francisco-Esteban This program is going to be a citation generator
# that I would like to use for my essays in other classes. This will include
# MLA, APA, and Chicago type citations.

# Here is a variable list:
# style: represents which style the citation; MLA, APA, or Chicago
# source: represents the name of the source that the user inputs
# firstName: represents the first name of the author
# lastName: represents the last name of the author
# title: represents the title of the book or website
# publisher: represents the name of the publisher
# year: represents the year published
# month: represents the month published
# day: represents the day published
# pageNumbers: represents the page number(s) used either as # or #-#
# url: represents the url of the website used
# location: this represents the location of publication

print("Hello user, welcome to Al's citation generator.", end=' ')  # I used
# an end= argument
print("Lets begin!")
# Here I used W3 Schools to help me with making sure that the input I needed
# to be remained as a lowercase no matter how the input was typed and
# learned about lower()
# URL: https://www.w3schools.com/python/ref_string_lower.asp
style = input("Which citation style are you looking to use today?\nMLA, APA,"
              "or Chicago?: ").lower()
# Here I used a while loop
while True:
    # here I used the "==" operator
    if style == "mla" or style == "apa" or style == "chicago":
        print("You chose:" + style)

    if style == "mla":
        print("Okay!")
        print("Is your source a book or a website?")
        source = input("Enter book or website: ")

        if (source == "Book") or (source == "book"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your book's title?")
            title = input("Enter title name: ")
            print("Next, what is the book's publisher?")
            publisher = input("Enter publisher name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            print("What pages did you use?")
            pageNumbers = input("Enter page number as # or #-#: ")
            print("Hear is your citation:")
            print(
                lastName + ", " + firstName + '. "' + title + '", ' +
                publisher +
                ", " + year + ", pp.",
                pageNumbers, sep='')  # I used a sep= argument
            # I also used the + string operator in the code above to combine
            # the string in order.
            print("\nEnjoy!" * 4)
            # I used the * string operator in the code above to print enjoy! 4
            # times
        # I used stack overflow to help me understand why my elif statement was
        # not working in the following code It was because I did not put == in
        # between each variable and string in the elif statement. Here is the
        # URL: https://stackoverflow.com/questions/15602421/if-within-if-python
        elif source == "Website" or (source == "website"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your the website's title?")
            title = input("Enter title name: ")
            print("Next, who is the publisher?")
            publisher = input("Enter publisher name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            month = str(input("Enter the first 3 letters of the month: "))
            day = input("Enter the day: ")
            print("What is the websites URL?")
            url = input("Enter the URL: ")
            print("Here is your citation: \n")
            print(
                lastName + ", " + firstName + '. "' + title + '", ' +
                publisher +
                ", " + day + " " + month + " " + year + ", " + url)
            print("\nEnjoy!" * 4)

    elif style == "apa":
        print("Okay!")
        print("Is your source a book or a website?")
        source = input("Enter book or website: ")
        if (source == "Book") or (source == "book"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your book's title?")
            title = input("Enter title name: ")
            print("Next, what is the book's publisher?")
            publisher = input("Enter publisher name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            print("What pages did you use?")
            pageNumbers = input("Enter page number as # or #-#: ")
            print("Hear is your citation:")
            print(
                lastName + ', ' + firstName + '. (' + year + '). "' + title +
                '" (pp. ' + pageNumbers + '). :' + publisher, sep='')

            print("\nEnjoy!" * 4)

        elif source == "Website" or (source == "website"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your the website's title?")
            title = input("Enter title name: ")
            print("Next, who is the publisher?")
            publisher = input("Enter publisher name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            month = str(input("Enter the month: "))
            day = input("Enter the day: ")
            print("What is the websites URL?")
            url = input("Enter the URL: ")
            print("Here is your citation: \n")
            print(
                lastName + ", " + firstName + '. (' + year + ',' + month +
                day +
                '). "' + title + '". ' + publisher + ', ' + url)
            print("\nEnjoy!" * 4)

    elif style == "chicago":
        print("Okay!")
        print("Is your source a book or a website?")
        source = input("Enter book or website: ")

        if (source == "Book") or (source == "book"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your book's title?")
            title = input("Enter title name: ")
            print("Next, what is the book's publisher?")
            publisher = input("Enter publisher name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            print("What pages did you use?")
            location = input("Enter the place of publication: ")
            print("Here is your citation:")
            print(
                lastName + ', ' + firstName + '. "' + title + '". ' +
                location +
                ': ' + publisher + ', ' + year, sep='')

            print("\nEnjoy!" * 4)

        elif source == "Website" or (source == "website"):
            print("Now, what is the name of the author of the source?")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            print("Next, what is your the website's title?")
            title = input("Enter title name: ")
            print("Next, who is the publisher?")
            publisher = input("Enter publisher/website name: ")
            print("What year was this source published?")
            year = input("Enter year: ")
            month = str(input("Enter the month: "))
            day = input("Enter the day: ")
            print("What is the websites URL?")
            url = input("Enter the URL: ")
            print("Here is your citation: \n")
            print(
                lastName + ", " + firstName + '. ' + publisher + '. ' +
                month + ' ' +
                day + ', ' + year + '. ' + url)
            print("\nEnjoy!" * 4)
        break

    else:
        print("Invalid source. Try again.")
        style = input(
            "Which citation style are you looking to use today?\nMLA, APA,"
            "or Chicago?: ").lower()

# I was not able to find a way to incorporate any numeric operators in my
# program, so I will instead explain what they do.

# The "**" operator finds the power of a number. ex.
# print("\n2 ** 3 =", 2 ** 3)
# this calculates 2 to the power of 3 and
# prints the answer of 8

# The "*" operator multiplies 2 numbers. ex.
# print("2 * 4 =", 2 * 4)

# The "/" operator divides a number by another
# print("16 / 2 =", 16 / 2)

# The "//" operator divides 2 numbers then round to its integer value. ex.
# print("17 // 2=", 17 // 2)

# The "%" operator divided 2 numbers then displays the remainder of theanswer.
# ex. print("98 % 10 =", 98 % 10)

# The "+" operator adds numbers together. ex.
# print("2 + 2 + 4 =", 2 + 2 + 4)

# The "-" operator subtracts numbers. ex.
# print("10 - 2 =", 10 - 2)

# These numerical operators can be combined. ex.
# print("(((2 ** 3 / 1) // 1) * 12.25 + (1-1)) % 10 =",
#       (((2 ** 3 / 1) // 1) * 12.25 + (1 - 1)) % 10)

# Due to time constraints I was not able to implement any shortcut operators or
# function definitions. But what I would do to include one is by defining a
# function for the type of source such as def bookAPA() or def websiteMLA()

# I was not able to find a way to use the relation operators: != or at least
# one of the following: > >= < <= so I will explain what they do.

# The "!=" basically means not equal to. For example: While x != 1

# The > means greater than, the >= means greater than or equal to, the < means
# less than, the <= means greater than or equal to

# I was not also able to find a way to use the "and" as well as the "not"
# operator.
# The "and" operator combines two expressions.
# The "not" operator excludes an expression

# I did not use "for", "range()", or "in" because I could not find a way to use
# them without drastically changing my code.
# "for" is to create a loop that can involve lists
# "range()" gives a sequence of numbers that can be used for identifying parts
#       of lists. They are used with "for"
# "in" is used retrieve things from a specific range or list
