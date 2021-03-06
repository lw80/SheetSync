# -*- coding: utf-8 -*-
"""
Test document creation:
    - Create new blank spreadsheets.
    - Creating from a template copy.
    - Creating in an existing folder (and removing it from the root container!)
"""

import sheetsync
import time, os

GOOGLE_U = os.environ.get("SHEETSYNC_GOOGLE_ACCOUNT")
GOOGLE_P = os.environ.get("SHEETSYNC_GOOGLE_PASSWORD")

TEMPLATE_DOC_KEY = "TODO"
TEMPLATE_DOC_NAME = "Interesting edge case?"
TESTS_FOLDER_KEY = os.environ.get("SHEETSYNC_FOLDER_KEY")
TESTS_FOLDER_NAME = "sheetsync testruns"

"""
def test_create_from_copy_template_key():
    print ('TODO: Create by copying template sheet.')
    assert False


def test_create_from_copy_template_name():
    print ('TODO: Create by copying template sheet.')
    assert False

"""

def test_move_to_folder_by_key():
    new_doc_name = '%s %s' % (__name__, int(time.time()))
    target = sheetsync.Sheet(GOOGLE_U,
                             GOOGLE_P,
                             document_name = new_doc_name,
                             sheet_name = 'Sheet1',
                             folder_key = TESTS_FOLDER_KEY)
    # Delete the doc
    gdc = target._doc_client_pool[GOOGLE_U]
    target_rsrc = gdc.get_resource_by_id(target.document_key)
    gdc.Delete(target_rsrc)


def test_move_to_folder_by_name():
    new_doc_name = '%s %s' % (__name__, int(time.time()))
    target = sheetsync.Sheet(GOOGLE_U,
                             GOOGLE_P,
                             document_name = new_doc_name,
                             sheet_name = 'Sheet1',
                             folder_name = TESTS_FOLDER_NAME)
    # Delete the doc
    target_rsrc = target.docs_client.get_resource_by_id(target.document_key)
    target.docs_client.Delete(target_rsrc)


def test_move_to_new_folder_by_name():
    new_doc_name = '%s %s' % (__name__, int(time.time()))
    new_folder_name = 'sheetsync testrun %s' % int(time.time())
    target = sheetsync.Sheet(GOOGLE_U,
                             GOOGLE_P,
                             document_name = new_doc_name,
                             sheet_name = 'Sheet1',
                             folder_name = new_folder_name)
    # Delete the doc
    gdc = target._doc_client_pool[GOOGLE_U]
    target_rsrc = gdc.get_resource_by_id(target.document_key)
    gdc.Delete(target_rsrc)
    # Delete the new folder too..
    folder_key = target.folder.GetId().rsplit('%3A',1)[1]
    folder_rsrc = gdc.get_resource_by_id(folder_key)
    gdc.Delete(folder_rsrc)


def test_the_kartik_test():
    # The most basic usage of creating a new sheet and adding data to it.
    # From April, Google defaults to using new-style sheets which requires
    # workarounds right now.

    new_doc_name = '%s %s' % (__name__, int(time.time()))
    target = sheetsync.Sheet(GOOGLE_U,
                             GOOGLE_P,
                             document_name = new_doc_name)
    # Check we can sync data to the newly created sheet.
    data = {"1" : {"name" : "Gordon", "color" : "Green"},
            "2" : {"name" : "Thomas", "color" : "Blue" } }
    target.sync(data)
    
    retrieved_data = target.data()
    assert "1" in retrieved_data
    assert retrieved_data["1"]["name"] == "Gordon"
    assert "2" in retrieved_data
    assert retrieved_data["2"]["color"] == "Blue"
    assert retrieved_data["2"]["Key"] == "2"

    # Try opening the doc with a new instance (thereby guessing key columns)
    test_read = sheetsync.Sheet(GOOGLE_U, GOOGLE_P,
                                document_name = new_doc_name)
    retrieved_data_2 = test_read.data()
    assert "1" in retrieved_data_2
    assert "2" in retrieved_data_2
    assert retrieved_data["2"]["color"] == "Blue"

    # Delete the doc
    gdc = target._doc_client_pool[GOOGLE_U]
    target_rsrc = gdc.get_resource_by_id(target.document_key)
    gdc.Delete(target_rsrc)

