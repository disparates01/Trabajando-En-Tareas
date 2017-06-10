SplashScreen
============
A SplashScreen is commonly used by large applications which can take some time to startup. The SplashScreen usually provides the name and logo of the application, and occasionally a :doc:`progressbar` to indicate the progress made in starting the program.

It is recommended to only use a SplashScreen where required.

===========
Constructor
===========
Construction of the SplashScreen is made using the call::

  splashscreen = QSplashScreen(pixmap)

The *pixmap* parameter should be set to an appropriate :doc:`pixmap` image which will be displayed on the SplashScreen.

=======
Methods
=======
The SplashScreen can be displayed when required with::

  splashscreen.show()

A SplashScreen is able to be closed automatically when the main window is shown with::

  splashscreen.finish(window)

The *window* argument should be set to the main window which the SplashScreen will wait for.

Displaying of a message on the SplashScreen is able to be done via the method::

  splashscreen.showMessage(message)

A message can also be cleared from display via::

  splashscreen.clearMessage()

=======
Example
=======
Below is an example of a SplashScreen:

.. literalinclude:: _examples/splashscreen.py

Download: :download:`SplashScreen <_examples/splashscreen.py>`
