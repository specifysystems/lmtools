"""Create an SDM using a method determined by the data."""
import argparse


# .....................................................................................
def cli():
    """Provide a command-line interface for the tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--min_points',
        type=int,
        default=12,
        help='Minimum number of points to use Maxent.',
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
    args = parser.parse_args()


# .....................................................................................
if __name__ == '__main__':
    cli()

