Feature: Go to 9-day forecast page
 Background:
    Given I launch Myobservatory
    When I go to 9-day forecast page

  Scenario: User check 9-day forecast
    Then I should see the "9-Day Forecast"

  Scenario: User switch to other tab
    Then I switch to "Local Forecast" tab and "Extended Outlook" tab

  Scenario: User open remarks
    Then I go to remarks page