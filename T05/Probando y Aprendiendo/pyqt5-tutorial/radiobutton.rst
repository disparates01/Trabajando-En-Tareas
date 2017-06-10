RadioButton
===========
The RadioButton is a toggable button, which is typically used in conjunction with other RadioButton's with only one of the buttons able to be selected at any one time.

If multiple items should be set at one time, a :doc:`checkbox` or :doc:`pushbutton` operating in toggle-mode can be used.

===========
Constructor
===========
The constructor used for building the RadioButton is::

  radiobutton = QRadioButton(label)

=======
Methods
=======
Text can be changed within the RadioButton via::

  radiobutton.setText(label)

The text can also be retrieved from the RadioButton by using the method::

  radiobutton.text()

To set a RadioButton to be checked, use::

  radiobutton.setChecked(checked)

When *checked* is set to ``True``, the defined RadioButton will be active.

Determining whether the RadioButton is active or not is done by::

  radiobutton.isChecked()

By default, all RadioButton widgets within the window will be assigned to the same group. This will cause problems if there are multiple batches of buttons which have different intents. To resolve this issue, read about the :doc:`buttongroup` object.

An icon can also be applied to the RadioButton if required::

  radiobutton.setIcon(icon)

=======
Example
=======
Below is an example of a RadioButton:

.. literalinclude:: _examples/radiobutton.py

Download: :download:`RadioButton <_examples/radiobutton.py>`
