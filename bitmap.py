import sys
#there is 68 periods from left to right and 20 lines going horizontal 



bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

response = input("Enter a message to be displayed on the map: ")
if response = "":
    sys.exit()

# if blank dont print the letter if a star then print the letter
stringofrows = bitmap.splitlines()
for line in stringofrows:
    
    for number, col in enumerate(bitmap):
            if col = " ":
                print(" ")
            else:
                print(response[number-1], end = '')
    print()
