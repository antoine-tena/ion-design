"""`python -m glaze`: the same entry point as the installed command."""

import sys

from glaze.cli import main

sys.exit(main())
