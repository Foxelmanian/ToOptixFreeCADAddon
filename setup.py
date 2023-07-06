# tooptix setup.py
from distutils.core import setup
setup(
      name="tooptixworkbench",
      packages=[
                "freecad",
                "freecad/ToOptixWorkbench",
                ],
      include_package_data=True,
      install_requires=["numpy==1.16.3",  # To maintain Python 2.7 compatibility 
                        "scipy==1.10.0"  # To maintain Python 2.7 compatibility
                        ],
      version="0.0.1",
      description="Topology Optimization with FreeCAD",
      author="DMST1990",
      author_email="",
      url="https://github.com/DMST1990/ToOptixFreeCADAddon/",
      keywords=["topology optimization", "CAD"],
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Manufacturing",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Scientific/Engineering :: Physics",
                   ],
      long_description="""\
Topology Optimization for different load cases
"""
)
