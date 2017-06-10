Wizard
======
A Wizard is a helper widget which allows for paginated display of information which the user can progress through. They are commonly used for setup of new programs or building up information prior to an action.

===========
Constructor
===========
The Wizard is constructed with the statement::

  wizard = QWizard()

=======
Methods
=======
A page can be added to the Wizard via the two methods::

  wizard.addPage(page)
  wizard.setPage(number, page)

The *page* parameter should be the :doc:`wizardpage` object which is to be added. The *number* indicates the position at which the page should be added.

Pages can also be removed by specifying the page number::

  wizard.removePage(number)

Any page can be set to be the starting page via the method::

  wizard.setStartId(start)

The *start* value defines the page number of the required WizardPage.

The title used on the page can be set with::

  wizard.setTitle(title)

The page object for a given page number can be retrieved using::

  wizard.page(number)

The current page object and number can be retrieved with the calls::

  wizard.currentPage()
  wizard.currentId()

A list of page ID numbers available can be fetched by calling::

  wizard.pageIds()

A check can be made on whether a user has visited a particular page via::

  wizard.hasVisitedPage(number)

Alternatively, a list of visited pages can be obtained in list form with::

  wizard.visitedPages()

The operation of the page movement can be done programmatically by::

  wizard.back()
  wizard.next()
  wizard.restart()

The ``.back()`` and ``.next()`` methods will take the user back to the previous page on forward to the next page. The ``.restart()`` call takes the user back to the first page.

The Wizard supports fetching of values from any widget on any page held by the Wizard with::

  wizard.field(name)

The *name* parameter specifies the name of the field whose value should be fetched.

A number of options to customise the look and feel of the Assistant can be defined for the Wizard, using the single or multiple methods::

  wizard.setOption(option, enabled)
  wizard.setOptions(option, ...)

The *option* parameter defines the option to be defined. The ``setOptions()`` method takes multiple options and enables them. The ``setOption()`` function also supports an *enabled* field which when set to ``True``, enables the defined option.

The available options are:

* ``QWizard.IndependentPages`` - pages are independent of each other and don't derive set values from each other.
* ``QWizard.IgnoreSubTitles`` - don't show any subtitles.
* ``QWizard.ExtendedWatermarkPixmap`` - extend watermark pixmaps to the bottom of the window edge.
* ``QWizard.NoDefaultButton`` - don't make a Next or Finish button the default.
* ``QWizard.NoBackButtonOnStartPage`` - hide Back button from first page.
* ``QWizard.NoBackButtonOnLastPage`` - hide Back button from last page.
* ``QWizard.DisabledBackButtonOnLastPage`` - prevent user from going back when on last page.
* ``QWizard.HaveNextButtonOnLastPage`` - show Next button on final page.
* ``QWizard.HaveFinishButtonOnEarlyPages`` - allow user to finish at any point in Wizard.
* ``QWizard.NoCancelButton`` - prevent user from cancelling the Wizard.
* ``QWizard.CancelButtonOnLeft`` - place Cancel button on left away from other buttons.
* ``QWizard.HaveHelpButton`` - show a Help button.
* ``QWizard.HelpButtonOnRight`` - place Help button on right with other buttons.
* ``QWizard.NoCancelButtonOnLastPage`` - remove Cancel button from final page.
* ``QWizard.HaveCustomButton1`` - show first user-defined button.
* ``QWizard.HaveCustomButton2`` - show second user-defined button.
* ``QWizard.HaveCustomButton3`` - show third user-defined button.

=======
Example
=======
Below is an example of a Wizard:

.. literalinclude:: _examples/wizard.py

Download: :download:`Wizard <_examples/wizard.py>`
