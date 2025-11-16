Feature: Revit System Configuration Application
  As a user
  I want to analyze Revit workstation specifications
  So that I can make informed hardware purchasing decisions

  Background:
    Given the application is initialized
    And the README.md file exists

  Scenario: Application loads successfully
    When I start the application
    Then the main dashboard should be visible
    And the README content should be displayed

  Scenario: Navigate to component analysis pages
    Given the application is running
    When I navigate to the Motherboard page
    Then I should see motherboard comparison data
    And I should see Z590 vs Z690 comparison charts

  Scenario: View CPU performance benchmarks
    Given the application is running
    When I navigate to the CPU page
    Then I should see CPU benchmark data
    And I should see i9-9900K vs i9-12900K comparison
    And the performance improvement should be displayed

  Scenario: Cost analysis is accurate
    Given the application is running
    When I navigate to the Cost page
    Then I should see the system cost breakdown
    And I should see the BudgetWorks invoice
