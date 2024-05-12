from ._anvil_designer import CoursesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..CourseItem import CourseItem



class Courses(CoursesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_courses()
    

  def load_courses(self):
    courses = anvil.server.call('get_course_details').search()
    
    for course in courses:
      c = CourseItem(name=course['name'], button_text=f"Purchase for Rs{course['price']}", description=course['description'], image=course["image"], button_callback=None)
      self.content_panel.add_component(c)
