Feature: Hardware Component Analysis
  As a hardware analyst
  I want to compare different component specifications
  So that I can recommend the best configuration

  Scenario: Compare CPU performance
    Given I have CPU benchmark data
    When I compare i9-9900K and i9-12900K
    Then i9-12900K should show better performance
    And the improvement should be at least 20% for Revit workloads

  Scenario: Compare motherboard specifications
    Given I have motherboard specification data
    When I compare Z590 and Z690 chipsets
    Then Z690 should have higher bandwidth
    And Z690 should support faster RAM
    And Z690 should have faster network speeds

  Scenario: Validate budget constraints
    Given the budget is 40000 HKD
    When I calculate the total system cost
    Then the cost should be within budget
    And all components should meet minimum requirements

  Scenario: Check memory requirements
    Given the Revit memory requirement is 64GB
    When I validate the memory configuration
    Then the system should have at least 64GB RAM
    And the RAM should be high-speed DDR4 or DDR5
