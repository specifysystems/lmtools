"""Create an SDM using a method determined by the data."""
import argparse

from lmtools.sdm.maxent import DEFAULT_MAXENT_OPTIONS
from lmtools.sdm.model import create_sdm


# .....................................................................................
def cli():
    """Provide a command-line interface for the tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--min_points',
        type=int,
        default=12,
        help='Minimum number of points to use Maxent.',
    )
    parser.add_argument(
        '-m',
        '--maxent_params',
        type=str,
        help=f'Extra options to send to Maxent (added to {DEFAULT_MAXENT_OPTIONS}.',
    )
    parser.add_argument(
        '--species_key',
        type=str,
        default='species_name',
        help='Header of CSV column containing species information.'
    )
    parser.add_argument(
        '--x_key',
        type=str,
        default='x',
        help='Header of CSV column containing X value for record.'
    )
    parser.add_argument(
        '--y_key',
        type=str,
        default='y',
        help='Header of CSV column containing Y value for record.'
    )

    parser.add_argument(
        'points_filename',
        type=str,
        help='File containing occurrences in species, x, y format.'
    )
    parser.add_argument(
        'env_dir',
        type=str,
        help='Directory containing environment layers for modeling.'
    )
    parser.add_argument(
        'ecoregions_filename', type=str, help='Ecoregions raster filename.'
    )
    parser.add_argument('work_dir', type=str, help='Directory where work can be done.')
    args = parser.parse_args()
    model_params = {
        'sp_key': args.species_key,
        'x_key': args.x_key,
        'y_key': args.y_key
    }
    if args.maxent_params is not None:
        model_params['maxent_arguments'] = args.maxent_params

    model_raster_filename, report = create_sdm(
        args.min_points,
        args.points_filename,
        args.env_dir,
        args.ecoregions_filename,
        args.work_dir,
        **model_params
    )


# .....................................................................................
if __name__ == '__main__':
    cli()
