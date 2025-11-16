"""
Pytest configuration and fixtures for the Revit System Configuration project.
"""
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def readme_path(project_root):
    """Return the README.md file path."""
    return project_root / "README.md"


@pytest.fixture(scope="session")
def image_dir(project_root):
    """Return the image directory path."""
    return project_root / "image"


@pytest.fixture
def sample_cpu_data():
    """Sample CPU comparison data for testing."""
    return {
        "i9-9900K": {
            "cinebench_r23": 1284,
            "cinebench_r23_multi": 12450,
            "geekbench_5_multi": 8779,
            "revit_2019": 5651,
        },
        "i9-12900K": {
            "cinebench_r23": 1997,
            "cinebench_r23_multi": 27472,
            "geekbench_5_multi": 17595,
            "revit_2019": 6946,
        },
    }


@pytest.fixture
def sample_motherboard_data():
    """Sample motherboard comparison data for testing."""
    return {
        "Z590": {"bandwidth": 16, "ram_speed": 320, "network_speed": 10},
        "Z690": {"bandwidth": 32, "ram_speed": 480, "network_speed": 100},
    }
