from distutils.core import setup
setup(
  name = 'Saranya-Sum-Two',         # How you named your package folder (MyLib)
  packages = ['Saranya-Sum-Two'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Addition of two numbers',   # Give a short description about your library
  author = 'Saranya Sekar',                   # Type in your name
  author_email = 'saranyatagore@yahoo.com',      # Type in your E-Mail
  url = 'https://github.com/saranya-sekar/Saranya-Sum-Two',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/saranya-sekar/Saranya-Sum-Two/archive/refs/tags/v02.tar.gz',    # I explain this later on
  keywords = ['saranya_addition', 'saranya_sum'],   # Keywords that define your package best
  
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sum=sum.__main__:main",
        ]
    },
)