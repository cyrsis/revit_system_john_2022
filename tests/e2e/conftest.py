"""
Playwright E2E test configuration for Streamlit application.
"""
import pytest
import subprocess
import time
from pathlib import Path


@pytest.fixture(scope="session")
def streamlit_app():
    """
    Start the Streamlit application for E2E testing.

    This fixture starts the Streamlit app in a subprocess and waits for it to be ready.
    After tests complete, it terminates the process.
    """
    # Start Streamlit app
    project_root = Path(__file__).parent.parent.parent
    main_py = project_root / "main.py"

    process = subprocess.Popen(
        ["streamlit", "run", str(main_py), "--server.headless=true", "--server.port=8501"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Wait for app to start (adjust time as needed)
    time.sleep(5)

    yield "http://localhost:8501"

    # Cleanup: terminate the process
    process.terminate()
    process.wait(timeout=5)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configure browser context arguments for Playwright.
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "ignore_https_errors": True,
    }
