import qrcode 

upi_id = input("Enter your upi id")


phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

                                        
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#save image of the qr_code(OPTIONAL)

#You can add image of the phonepay qrcode here.......
#You can add image of the paytm qrcode here.......
#You can add image of the googlepay qrcode here.......

#--------------------------------------------------------------------------------------------------------------------#

#Display qr codes ( You may need to install PIL/Pillow library)

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

