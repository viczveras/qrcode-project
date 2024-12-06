# if u reading this, u should know that this is my first ever project in phyton :)

import qrcode

def generate_qrcode(link):
    qr = qrcode.QRCode(
        version=1, # controls the size, 1 is minimum
        error_correction=qrcode.constants.ERROR_CORRECT_L, # defines level of error correction, L is minimum
        box_size=10, # pretty self explainable
        border=4, # border height 
        )
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white") # generates the qr code with the colors, black and white
    img.save("qrcode.png")

  


    
    
link = input("Please type the link you wish to turn into QRCode: ")
generate_qrcode(link)
print("QRCode generate and save as qrcode.png")




# again, if u seeing this, i hardly recommend you to look up the qrcode i generated as a test :)