Dev
==================================

::

    (hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/client$ python client.py
    /hangman/hangman_client/venvs/hangman_client/local/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
    SNIMissingWarning
    /hangman/hangman_client/venvs/hangman_client/local/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
    InsecurePlatformWarning
    {"message":"Problems parsing JSON"}

solution

::

    $ sudo apt-get install build-essential python-dev
    $ sudo apt-get install libffi-dev libssl-dev
    $ pip install pyopenssl ndg-httpsclient pyasn1

or 

:: 

    $ pip install requests==2.5.3
