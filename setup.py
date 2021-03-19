from distutils.core import setup
setup(
  name = 'libmp',
  packages = ['LIBMP'],
  version = '0.1',
  license='MIT',
  description = 'LIBRARY FOR SUPPORT FUNCTIONS AND METHODS AT WORK FOR GROUP MULTIPECAS FROM BRAZIL',
  author = 'LUCAS GARCIA RIBEIRO',
  author_email = 'lucasgr7@gmail.com',
  url = 'https://onlinemotopecas.com.br/',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['LIBRARY', 'MULTIPECAS', 'API', 'MERCADOLIVRE'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)