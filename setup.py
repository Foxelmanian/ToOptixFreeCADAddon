# pyrateoptics setup.py
from distutils.core import setup
setup(
      name="tooptixworkbench",
      packages=["ToOptix",
                "freecad",
                "freecad/ToOptixWorkbench"],
      include_package_data=True,
      install_requires=["numpy",
                        "scipy",
                        "matplotlib",
                        "sympy",
                        "pyyaml"],
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
