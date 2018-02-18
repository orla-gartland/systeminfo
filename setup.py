from setuptools import setup



 
setup(name= "systeminfo",
      version="0.1",
      description= "Basic system information for comp30670", 
      url="",
      author="Orla Gartland", 
      author_email="orla.gartland@ucdconnect.ie",
      licence="GPL3", 
      packages= ['systeminfo'],
      entry_points ={
          'console_scripts':['comp30670_workspace_systeminfo=systeminfo.main:main']
          }
    )