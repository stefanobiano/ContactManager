import pickle
import os.path

"""
 * @brief  class Contact
 *
 * This class represents the user with all his attributes
 *
 *
 * @param  name   
 * @param  surname
 * @param  phone
 * @param  mail
 * @param  des
 *
 """
class Contact:
    def __init__(self, name, surname, phone, mail, des):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail
        self.des = des

"""
 * @brief  class ContactManager
 *
 * This class manages contacts
 *
 """
class ContactManager:

    """
     * @brief  function loadContacts
     *
     * This function load all contacts from a pickle file and save them in a list
     *
     * @return mylist list with all contacts
     *
     """
    def loadContacts(self):
        # define mylist
        self.mylist = []
        # if file exsist, open it and save in mylist
        if os.path.isfile('contactList.pkl'):
            with open('contactList.pkl', 'rb') as f:
                self.mylist = pickle.load(f)
        # return mylist
        return self.mylist

    """
     * @brief  function findContact
     *
     * This function find a contact by name or surname from the list loaded with loadContacts
     *
     * @param  nameorsurname  contact name or contact surname 
     *
     * @return foundedmylist list with all founded contacts
     *
     """
    def findContact(self, nameorsurname):
        # define foundedlist
        self.foundedlist = []

        self.loadContacts()

        # check name or surname and in positive case add to the foundedlist
        for i, o in enumerate(self.mylist):
            if (o.name.startswith(nameorsurname) or o.surname.startswith(nameorsurname)):
                self.foundedlist.append(o)

        # return foundedlist
        return self.foundedlist

    """
     * @brief  function findContactByPhone
     *
     * This function find a contact by phone from the list loaded with loadContacts
     *
     * @param  phone  contact phone
     *
     * @return o    founded contact
     *
     """
    def findContactByPhone(self, phone):
        # define foundedlist
        self.foundedlist = []

        self.loadContacts()
        # check phone number and in positive case return the contact
        for i, o in enumerate(self.mylist):
            if o.phone == phone:
                return o

    """
     * @brief  function saveContact
     *
     * This function save a contact in the pickle file
     *
     * @param  contact  a contact instance
     *
     """
    def saveContact(self, contact):

        mylist = self.loadContacts()
        # add new contact
        mylist.append(contact)
        # save new list
        with open('contactList.pkl', 'wb') as f:
            pickle.dump(mylist, f)

    """
     * @brief  function deleteContact
     *
     * This function delete a contact by phone from pickle file
     *
     * @param  phone  contact phone
     *
    """
    def deleteContact(self, phone):
        mylist = self.loadContacts()
        for i, o in enumerate(mylist):
            # check phone number and in positive case delete it and save the new list
            if o.phone == phone:
                del self.mylist[i]
                with open('contactList.pkl', 'wb') as f:
                    pickle.dump(mylist, f)

    """
     * @brief  function saveSortedList
     *
     * This function save all contacts in the pickle file
     *
     * @param  newlist  sorted list
     *
     """
    def saveSortedList(self, newlist):
        with open('contactList.pkl', 'wb') as f:
                    pickle.dump(newlist, f)

