"""Test the create_sdm tool."""
import glob
import os
import shutil

from lmtools.tools.create_sdm import cli


# .....................................................................................
def test_create_sdm(monkeypatch, work_dir, environment_dir, ecoregions, species_filename):
    """Test the create_sdm tool."""
    # Move occurrence data
    points_filename = os.path.join(work_dir, 'species.csv')
    shutil.copy(species_filename, points_filename)

    # Env dir
    env_dir = os.path.join(work_dir, 'model_env')
    os.mkdir(env_dir)
    for fn in glob.glob(os.path.join(environment_dir, '*')):
        shutil.copy(fn, os.path.join(env_dir, os.path.basename(fn)))

    ecoregions_filename = os.path.join(work_dir, 'ecoregions.tif')
    shutil.copy(ecoregions, ecoregions_filename)

    model_raster_filename = os.path.join(work_dir, 'model_raster.asc')

    params = [
        'create_sdm.py',
        '-n',
        '12',
        points_filename,
        env_dir,
        ecoregions_filename,
        work_dir,
        model_raster_filename
    ]

    monkeypatch.setattr('sys.argv', params)
    cli()
