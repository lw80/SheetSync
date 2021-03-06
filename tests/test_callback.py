# -*- coding: utf-8 -*-
"""
Test the support for a row_change callback function.
"""
import sheetsync
import time, os

# TODO: Use this: http://stackoverflow.com/questions/22574109/running-tests-with-api-authentication-in-travis-ci-without-exposing-api-password

GOOGLE_U = os.environ.get("SHEETSYNC_GOOGLE_ACCOUNT")
GOOGLE_P = os.environ.get("SHEETSYNC_GOOGLE_PASSWORD")

TESTS_FOLDER = os.environ.get("SHEETSYNC_FOLDER_KEY")
# Template hosted by a dedicated "sheetsync" account that Mark set up.
TEMPLATE_DOC = ""

target = None

"""
TODO: write this test!
def setup_function(function):
    global target
    print ('setup_function: Create test spreadsheet.')
    # Copy the template spreadsheet into the prescribed folder.
    new_doc_name = '%s %s' % (__name__, int(time.time()))
    target = sheetsync.Sheet(GOOGLE_U,
                             GOOGLE_P,
                             document_name = new_doc_name,
                             folder_key = TESTS_FOLDER,
                             template_key = TEMPLATE_DOC,
                             sheet_name = "Arsenal",
                             header_row_ix=2,
                             key_column_headers = ["No."],
                             formula_ref_row_ix=1)


def teardown_function(function):
    print ('teardown_function Delete test spreadsheet')
    gdc = target._doc_client_pool[GOOGLE_U]
    target_rsrc = gdc.get_resource_by_id(target.document_key)
    gdc.Delete(target_rsrc)

def test_row_change_callback():
    print ('Update/Insert into a sheet and check row_change behavior')
    assert False
"""
