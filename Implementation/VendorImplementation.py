from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel

class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        if self.vendor_model.is_correct_vendor(username, password):
            self.vendor_session.login(username)
            print("user {} logged in successfully!".format(username))
            return True
        else:
            print("Invalid username or password.")

    # Add you code here after verifying the vendor data exists in the dictionary

    def logout(self, username):
        self.vendor_session.logout(username)
        print("User {} logged out successfully!".format(username))


        # Add your code here to log out the current vendor
