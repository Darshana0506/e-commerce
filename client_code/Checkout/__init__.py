from ._anvil_designer import CheckoutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Checkout(CheckoutTemplate):
  def __init__(self,id_name,back_button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.back_button.callback = back_button_callback
    self.update_form(id_name)

    # Any code you write here will run before the form opens.
  def update_form(self, id_name):
    course = anvil.server.call('get_course_details', id_name)
    self.name_label.text = course["name"]
    self.description_label.text = course['description']
    self.price_label.text = f"Rs{course['price']}"
    self.image_content.source = course['image']

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()
  