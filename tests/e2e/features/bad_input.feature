Feature: bad input handling
    Scenario: No arguments
        Given no arguments
        When poker script is run
        Then it should fail

    Scenario: One argument
        Given 'AAAQQ' argument
        When poker script is run
        Then it should fail

    Scenario: Three arguments
        Given below list of arguments
        """
        AAAQQ AAAQQ AAAQQ
        """
        When poker script is run
        Then it should fail

    Scenario: Invalid arguments
        Given 123 and ABCD hands
        When poker script is run
        Then it should fail
