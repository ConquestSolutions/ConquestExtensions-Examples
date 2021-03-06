##########
#
# THIS SCRIPT VALIDATES THE LOCATION FIELD IN THE ACTION FORM BEFORE IT FIRES
# Copy this code into ActionSavingValidation - it uses the location field from that particular interface.
# This script fires when someone goes to 'save' an action. We want to check to make sure they have entered a location.
# If they haven't, we'll raise a MessageBox as shown in 3.1.
#
### NOTE: THIS SCRIPT NEEDS TO BE COPIED TO THE REQUEST SCRIPT WITH THE KEY 'ActionSavingValidation' FOR IT TO WORK
#
##########

from System import *
from System.Windows import *

#create reusable MessageBox
def displayMessage(message):
	MessageBox.Show(str(message))

#Validate a field - check that a location has been entered, if it hasn't, display a messagebox.
if String.IsNullOrWhiteSpace(source.Location):
	isWaitCallBack = True #isWaitCallback is a Conquest function that will prevent the 'Save' from firing until it gets a response from the callback.
	displayMessage('Please enter a location.')