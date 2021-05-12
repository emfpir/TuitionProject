Feature: Tuition Portal Has Many Credentials

  Scenario Outline: Users Credentials Works
    Given The User is on the Authorization Page
    When The User types <name> in the Name Field
    When The User types <title> in the Title Field
    When The User clicks the Submit Button
    Then The banner should be <banner>

    Examples:
      | name        | title                      | banner                             |
      | Adam        | Benefits Coordinator       | Adam - Benefits Coordinator        |
      | Betty       | Accounting Head            | Betty - Accounting Head            |
      | Chris       | Human Resources Head       | Chris - Human Resources Head       |
      | Doug        | Operations Head            | Doug - Operations Head             |
      | Edward      | Operations Supervisor       | Edward - Operations Supervisor      |
      | Fred        | Accounting Supervisor      | Fred - Accounting Supervisor       |
      | Georgia     | Operations Employee        | Georgia - Operations Employee      |
      | Henry       | Accounting Employee        | Henry - Accounting Employee        |
      | Issac       | Human Resources Supervisor | Issac - Human Resources Supervisor |
      | Jesse        | Human Resources Employee   | Jesse - Human Resources Employee    |
      | Kyle        | Human Resources Employee   | Kyle - Human Resources Employee    |
      | Lee         | Accounting Employee        | Lee - Accounting Employee          |
      | Matthew     | Operations Employee        | Matthew - Operations Employee      |
