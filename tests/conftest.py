"""Pytest configuration."""
import glob
import os
import shutil
import tempfile

import pytest


TEST_DATA_DIR = os.path.abspath(os.path.join('data_dir'))


# .....................................................................................
@pytest.fixture(scope='session', params=glob.glob(os.path.join(TEST_DATA_DIR, 'occurrence', '*.csv')))
def species_filename(request):
    """Get species occurrence filenames."""
    yield request.param


# .....................................................................................
@pytest.fixture(scope='session')
def environment_dir():
    """Get a directory of environment layers."""
    return os.path.join(TEST_DATA_DIR, 'env_layers')


# .....................................................................................
@pytest.fixture(scope='session')
def ecoregions():
    """Get an ecoregions file location."""
    return os.path.join(TEST_DATA_DIR, 'ecoregions.tif')


# .....................................................................................
@pytest.fixture(scope='session')
def generate_temp_filename(request):
    """Get a function to generate (and clean up) temporary files.
    Args:
        request (pytest.fixture): A pytest request fixture.
    Returns:
        Method: A function to generate a temporary filename.
    """
    delete_globs = []

    # ..................
    def get_filename(suffix='', wildcard_delete=True):
        """Get a temporary filename.
        Args:
            suffix (str): A suffix to add to the filename.
            wildcard_delete (bool): Delete all files with returned basename.
        Returns:
            str: A temporary filename.
        """
        base_name = tempfile.NamedTemporaryFile().name
        fn = f'{base_name}{suffix}'
        if wildcard_delete:
            delete_globs.append(f'{base_name}*')
        else:
            delete_globs.append(fn)
        return fn

    # ..................
    def finalizer():
        """Clean up temporary files."""
        for del_glob in delete_globs:
            for fn in glob.glob(del_glob):
                try:
                    os.remove(fn)
                except PermissionError:
                    try:
                        time.sleep(10)
                        os.remove(fn)
                    except PermissionError:
                        pass

    request.addfinalizer(finalizer)
    return get_filename


# .....................................................................................
@pytest.fixture(scope='function')
def work_dir():
    """Get a work directory.

    Yields:
        str: A directory to use for testing.
    """
    dir_name = tempfile.TemporaryDirectory().name
    os.makedirs(dir_name)
    yield dir_name

    shutil.rmtree(dir_name)