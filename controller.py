#!/usr/bin/env python
# -*- coding: utf-8 -*- controller
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.clock import mainthread
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.image import Image
from kivy.lang import Builder
from model import Contact, ContactManager

"""
 * @brief  class MapScreen
 *
 * This class represents the view of the application
 *
 """
class MapScreen(Screen):

    @mainthread
    def on_enter(self):
        cm = ContactManager()
        listContact = cm.loadContacts()
        # show all contact in the grid view
        for contact in listContact:
            self.ids.grid.add_widget(Label(text=(contact.name + " " + contact.surname)))


"""
 * @brief  class SearchInput
 *
 * This class shows all contacts matching the introduced string in real time
 *
 """
class SearchInput(TextInput):

    """
     * @brief  function searchContact
     *
     * This function searches all contacts matching the introduced string in real time
     * and in the same moment updates all info about contact in the contact info view
     *
     * @param  grid         component list all contacts founded
     * @param  ti           component with input text
     * @param  deltiname    name view
     * @param  deltisurname surname view
     * @param  deltiphone   phone view
     * @param  deltimail    mail view
     * @param  deltides     des view
     * 
     """
    def searchContact(self, grid, ti, deltiname, deltisurname, deltiphone, deltimail, deltides):
        cm = ContactManager()
        # every time clear list
        grid.clear_widgets()
        foundedList = cm.findContact(ti.text)
        # if there is ore or more result i print only the first in the contact info view
        # i print all founded contact in the grid view
        if foundedList != []:
            time = 1
            for contact in foundedList:
                if time == 1:
                    deltiname.text = contact.name
                    deltisurname.text = contact.surname
                    deltiphone.text = contact.phone
                    deltimail.text = contact.mail
                    deltides.text = contact.des
                    time = 2
                grid.add_widget(Label(text=(contact.name + " " + contact.surname)))
        else:
            grid.add_widget(Label(text="Nessun contatto trovato"))

"""
@brief  class SortButton

This class sorts all contacts in the grid list

"""
class SortButton(Button):

    """
     * @brief  function sortByName
     *
     * This function sorts all contact in the gril list by name
     *
     * 
    """
    def sortByName(self):
        cm = ContactManager()
        mylist = cm.loadContacts()
        newlist = sorted(mylist, key=lambda contact: contact.name)
        cm.saveSortedList(newlist)

    """
     * @brief  function sortBySurname
     *
     * This function sorts all contact in the gril list by surname
     *
     * 
    """
    def sortBySurname(self):
        cm = ContactManager()
        mylist = cm.loadContacts()
        newlist = sorted(mylist, key=lambda contact: contact.surname)
        cm.saveSortedList(newlist)

"""
@brief  class AddButton

This class addes a new contact

"""
class AddButton(Button):

    """
     * @brief  function addContact
     *
     * This function addes a new contact
     *
     * 
    """
    def addContact(self, name, surname, phone, mail, des):
        cm = ContactManager()
        c = Contact(name, surname, phone, mail, des)
        cm.saveContact(c)

"""
@brief  class DeleteButton

This class deletes a  contact

"""
class DeleteButton(Button):

    """
     * @brief  function deleteContact
     *
     * This function deletes a contact
     *
     * 
    """
    def deleteContact(self, phone):
        cm = ContactManager()
        cm.deleteContact(phone)

"""
@brief  class ModifyButton

This class modifies an element of a contact

"""
class ModifyButton(Button):

    """
     * @brief  function changeName
     *
     * This function changes the name of a contact
     *
     * 
    """
    def changeName(self, ti, cb, phone):
        if cb.active:
            cm = ContactManager()
            c = cm.findContactByPhone(phone)
            cm.deleteContact(phone)
            c.name = ti.text
            cm.saveContact(c)

    """
     * @brief  function changeSurname
     *
     * This function changes the surname of a contact
     *
     * 
    """
    def changeSurname(self, ti, cb, phone):
        if cb.active:
            cm = ContactManager()
            c = cm.findContactByPhone(phone)
            cm.deleteContact(phone)
            c.surname = ti.text
            cm.saveContact(c)

    """
     * @brief  function changeMail
     *
     * This function changes the mail of a contact
     *
     * 
    """
    def changeMail(self, ti, cb, phone):
        if cb.active:
            cm = ContactManager()
            c = cm.findContactByPhone(phone)
            cm.deleteContact(phone)
            c.mail = ti.text
            cm.saveContact(c)

    """
     * @brief  function changeDes
     *
     * This function changes the description of a contact
     *
     * 
    """
    def changeDes(self, ti, cb, phone):
        if cb.active:
            cm = ContactManager()
            c = cm.findContactByPhone(phone)
            cm.deleteContact(phone)
            c.des = ti.text
            cm.saveContact(c)


presentation = Builder.load_file("view.kv")

"""
@brief  class Controller

This class is the main class

"""
class Controller(App):
    def build(self):
        return presentation


Controller().run()