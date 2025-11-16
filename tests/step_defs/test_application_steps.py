"""
Step definitions for application feature tests.
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path

# Load scenarios from the feature file
scenarios("../features/application.feature")


@given("the application is initialized")
def application_initialized(project_root):
    """Verify the application structure exists."""
    assert (project_root / "main.py").exists()
    assert (project_root / "pages").exists()
    assert (project_root / "README.md").exists()


@given("the README.md file exists")
def readme_exists(readme_path):
    """Verify README.md file exists."""
    assert readme_path.exists()
    assert readme_path.is_file()


@given("the application is running")
def application_running(project_root):
    """Simulate application running state."""
    # For BDD testing, we verify the application can be started
    assert (project_root / "main.py").exists()


@when("I start the application")
def start_application(project_root):
    """Simulate starting the application."""
    main_py = project_root / "main.py"
    assert main_py.exists()
    # In actual E2E tests, this would start the Streamlit app


@when("I navigate to the Motherboard page")
def navigate_to_motherboard(project_root):
    """Simulate navigation to motherboard page."""
    motherboard_page = project_root / "pages" / "1_Motherboard.py"
    assert motherboard_page.exists()


@when("I navigate to the CPU page")
def navigate_to_cpu(project_root):
    """Simulate navigation to CPU page."""
    cpu_page = project_root / "pages" / "2_Cpu.py"
    assert cpu_page.exists()


@when("I navigate to the Cost page")
def navigate_to_cost(project_root):
    """Simulate navigation to cost page."""
    cost_page = project_root / "pages" / "7_Cost.py"
    assert cost_page.exists()


@then("the main dashboard should be visible")
def verify_dashboard(project_root):
    """Verify main dashboard components."""
    main_py = project_root / "main.py"
    content = main_py.read_text()
    assert "streamlit" in content
    assert "README.md" in content


@then("the README content should be displayed")
def verify_readme_displayed(readme_path):
    """Verify README content is available."""
    content = readme_path.read_text()
    assert "Revit System" in content
    assert len(content) > 100


@then("I should see motherboard comparison data")
def verify_motherboard_data(project_root):
    """Verify motherboard comparison data exists."""
    motherboard_page = project_root / "pages" / "1_Motherboard.py"
    content = motherboard_page.read_text()
    assert "Z590" in content and "Z690" in content


@then("I should see Z590 vs Z690 comparison charts")
def verify_motherboard_charts(project_root):
    """Verify motherboard comparison charts."""
    motherboard_page = project_root / "pages" / "1_Motherboard.py"
    content = motherboard_page.read_text()
    assert "plotly" in content
    assert "px.bar" in content


@then("I should see CPU benchmark data")
def verify_cpu_data(project_root):
    """Verify CPU benchmark data exists."""
    cpu_page = project_root / "pages" / "2_Cpu.py"
    content = cpu_page.read_text()
    assert "i9-9900K" in content and "i9-12900K" in content


@then("I should see i9-9900K vs i9-12900K comparison")
def verify_cpu_comparison(project_root):
    """Verify CPU comparison exists."""
    cpu_page = project_root / "pages" / "2_Cpu.py"
    content = cpu_page.read_text()
    assert "Cinebench" in content or "Geekbench" in content


@then("the performance improvement should be displayed")
def verify_performance_improvement(project_root):
    """Verify performance improvement is shown."""
    cpu_page = project_root / "pages" / "2_Cpu.py"
    content = cpu_page.read_text()
    assert "Winner" in content or "30%" in content


@then("I should see the system cost breakdown")
def verify_cost_breakdown(project_root):
    """Verify cost breakdown exists."""
    cost_page = project_root / "pages" / "7_Cost.py"
    content = cost_page.read_text()
    assert "Cost" in content or "Invoice" in content


@then("I should see the BudgetWorks invoice")
def verify_budgetworks_invoice(project_root):
    """Verify BudgetWorks invoice is referenced."""
    cost_page = project_root / "pages" / "7_Cost.py"
    content = cost_page.read_text()
    assert "budgetwork" in content.lower()
