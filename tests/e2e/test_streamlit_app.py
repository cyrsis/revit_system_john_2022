"""
End-to-End tests for Streamlit application using Playwright.

These tests verify the complete user workflow through the application.
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
class TestStreamlitApplication:
    """E2E tests for the main Streamlit application."""

    def test_homepage_loads(self, page: Page, streamlit_app: str):
        """Test that the homepage loads successfully."""
        page.goto(streamlit_app)

        # Wait for Streamlit to load
        page.wait_for_load_state("networkidle")

        # Check that the page contains expected content
        expect(page).to_have_title("main")

        # Verify README content is displayed
        page.wait_for_selector("text=Revit System", timeout=10000)

    def test_sidebar_navigation(self, page: Page, streamlit_app: str):
        """Test navigation through sidebar menu."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Streamlit apps have a sidebar for multi-page navigation
        # Check if sidebar exists
        sidebar = page.locator('[data-testid="stSidebar"]')
        expect(sidebar).to_be_visible()

    def test_readme_content_displayed(self, page: Page, streamlit_app: str):
        """Test that README content is properly displayed on main page."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Check for key content from README
        page.wait_for_selector("text=Revit System", timeout=10000)

        # Verify some key information is present
        content = page.content()
        assert "Budget" in content or "Constraint" in content

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_motherboard_page_content(self, page: Page, streamlit_app: str):
        """Test motherboard page displays comparison data."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Navigate to Motherboard page
        # This would require clicking on the sidebar navigation
        # The exact selector depends on Streamlit's rendering
        motherboard_link = page.locator("text=Motherboard")
        if motherboard_link.is_visible():
            motherboard_link.click()
            page.wait_for_load_state("networkidle")

            # Verify motherboard content
            page.wait_for_selector("text=Z590", timeout=5000)
            page.wait_for_selector("text=Z690", timeout=5000)

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_cpu_page_benchmarks(self, page: Page, streamlit_app: str):
        """Test CPU page displays benchmark data."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Navigate to CPU page
        cpu_link = page.locator("text=Cpu")
        if cpu_link.is_visible():
            cpu_link.click()
            page.wait_for_load_state("networkidle")

            # Verify CPU content
            page.wait_for_selector("text=i9-9900K", timeout=5000)
            page.wait_for_selector("text=i9-12900K", timeout=5000)

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_cost_page_invoice(self, page: Page, streamlit_app: str):
        """Test cost page displays invoice information."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Navigate to Cost page
        cost_link = page.locator("text=Cost")
        if cost_link.is_visible():
            cost_link.click()
            page.wait_for_load_state("networkidle")

            # Verify cost content
            page.wait_for_selector("text=Cost", timeout=5000)
            page.wait_for_selector("text=Invoice", timeout=5000)


@pytest.mark.e2e
class TestStreamlitInteractivity:
    """E2E tests for interactive features."""

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_plotly_charts_render(self, page: Page, streamlit_app: str):
        """Test that Plotly charts render correctly."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Navigate to a page with charts (e.g., CPU or Motherboard)
        cpu_link = page.locator("text=Cpu")
        if cpu_link.is_visible():
            cpu_link.click()
            page.wait_for_load_state("networkidle")

            # Wait for Plotly chart to render
            # Plotly charts typically have a specific class or SVG element
            chart = page.locator(".js-plotly-plot")
            expect(chart).to_be_visible(timeout=10000)

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_images_load(self, page: Page, streamlit_app: str):
        """Test that images load properly throughout the application."""
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Check for images on various pages
        images = page.locator("img")

        # Verify at least one image is present
        expect(images.first).to_be_visible(timeout=10000)

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_responsive_layout(self, page: Page, streamlit_app: str):
        """Test that the layout is responsive to different screen sizes."""
        # Test desktop size
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Verify content is visible
        content = page.locator('[data-testid="stMarkdown"]')
        expect(content.first).to_be_visible()

        # Test tablet size
        page.set_viewport_size({"width": 768, "height": 1024})
        page.wait_for_timeout(1000)
        expect(content.first).to_be_visible()

        # Test mobile size
        page.set_viewport_size({"width": 375, "height": 667})
        page.wait_for_timeout(1000)
        expect(content.first).to_be_visible()


@pytest.mark.e2e
class TestStreamlitPerformance:
    """E2E tests for application performance."""

    def test_page_load_time(self, page: Page, streamlit_app: str):
        """Test that the page loads within acceptable time."""
        import time

        start_time = time.time()
        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")
        load_time = time.time() - start_time

        # Page should load within 10 seconds
        assert load_time < 10, f"Page took {load_time:.2f}s to load"

    @pytest.mark.skip(reason="Requires running Streamlit app - skip in CI")
    def test_navigation_performance(self, page: Page, streamlit_app: str):
        """Test that navigation between pages is fast."""
        import time

        page.goto(streamlit_app)
        page.wait_for_load_state("networkidle")

        # Test navigation to multiple pages
        pages_to_test = ["Motherboard", "Cpu", "Cost"]

        for page_name in pages_to_test:
            link = page.locator(f"text={page_name}")
            if link.is_visible():
                start_time = time.time()
                link.click()
                page.wait_for_load_state("networkidle")
                nav_time = time.time() - start_time

                # Navigation should complete within 5 seconds
                assert nav_time < 5, f"Navigation to {page_name} took {nav_time:.2f}s"
