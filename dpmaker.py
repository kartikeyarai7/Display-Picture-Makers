from PIL import Image, ImageFilter

user = input('Where do you want to use this picture \n 1. Whatsapp 2.Instagram 3.Facebook \n Enter the option number: ')

def img_converter(user):
    if user == "1":
        img = Image.open("./meee.jpg")  #INSERT YOUR IMAGE IN THE SAME DIRECTORY AND SAVE IT AS meee.jpg
        img.thumbnail((192,192))  #Thumbnail keeps the aspect ratio
        bws_dp = img.convert("L")
        # beautified_dp = bws_dp.filter(ImageFilter.SMOOTH) IF YOU WANT TO SMOOTHEN IT, UNCOMMENT THIS
        # bws_dp.save("Wsdpbw.png","png") IF YOU WANT TO SAVE UNCOMMENT THIS
        # print(beautified_dp)
        bws_dp.show()


    if user == "2":
        img = Image.open("./meee.jpg")
        img.thumbnail((110,110))
        bws_dp = img.convert("L")
        # beautified_dp = bws_dp.filter(ImageFilter.SMOOTH) IF YOU WANT TO SMOOTHEN IT, UNCOMMENT THIS
        # bws_dp.save("Wsdpbw.png","png") IF YOU WANT TO SAVE UNCOMMENT THIS
        # print(beautified_dp)
        bws_dp.show()


    if user == "3":
        img = Image.open("./meee.jpg")
        img.thumbnail((170,170))
        bws_dp = img.convert("L")
        # beautified_dp = bws_dp.filter(ImageFilter.SMOOTH) IF YOU WANT TO SMOOTHEN IT, UNCOMMENT THIS
        # bws_dp.save("Wsdpbw.png","png") IF YOU WANT TO SAVE UNCOMMENT THIS
        # print(beautified_dp)
        bws_dp.show()

img_converter(user)




