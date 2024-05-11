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
    c = CourseItem(name='Python',button_text='Buy for 100',desciption='Master python')
    self.content_panel.add_component(c)
    

  def load_courses(self):
    courses = anvil.server.call('get_course_details').search()
    
    for course in courses:
      print(course['Name'])
