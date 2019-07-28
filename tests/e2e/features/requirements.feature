Feature: poker winner checker
    Scenario Outline: All possible cases
        Given <first_hand> and <second_hand> hands
        When poker script is run
        Then it should succeed
        Then expected output is equal to <expected_output>

        Examples: Tie
            | first_hand | second_hand | expected_output |
            | AAAQQ      | QQAAA       | It's a tie!     |
            | 53QQ2      | Q53Q2       | It's a tie!     |
            | 53888      | 88385       | It's a tie!     |
            | QQAAA      | AAAQQ       | It's a tie!     |
            | Q53Q2      | 53QQ2       | It's a tie!     |
            | 88385      | 53888       | It's a tie!     |

        Examples: First hand wins
            | first_hand | second_hand | expected_output  |
            | AAAQQ      | QQQAA       | First hand wins! |
            | Q53Q4      | 53QQ2       | First hand wins! |
            | 53888      | 88375       | First hand wins! |
            | 33337      | QQAAA       | First hand wins! |
            | 22333      | AAA58       | First hand wins! |
            | 33389      | AAKK4       | First hand wins! |
            | 44223      | AA892       | First hand wins! |
            | 22456      | AKQJT       | First hand wins! |
            | 99977      | 77799       | First hand wins! |
            | 99922      | 88866       | First hand wins! |
            | 9922A      | 9922K       | First hand wins! |
            | 99975      | 99965       | First hand wins! |
            | 99975      | 99974       | First hand wins! |
            | 99752      | 99652       | First hand wins! |
            | 99752      | 99742       | First hand wins! |
            | 99753      | 99752       | First hand wins! |

        Examples: Second hand wins
            | first_hand | second_hand | expected_output   |
            | QQQAA      | AAAQQ       | Second hand wins! |
            | 53QQ2      | Q53Q4       | Second hand wins! |
            | 88375      | 53888       | Second hand wins! |
            | QQAAA      | 33337       | Second hand wins! |
            | AAA58      | 22333       | Second hand wins! |
            | AAKK4      | 33389       | Second hand wins! |
            | AA892      | 44223       | Second hand wins! |
            | AKQJT      | 22456       | Second hand wins! |
            | 77799      | 99977       | Second hand wins! |
            | 88866      | 99922       | Second hand wins! |
            | 9922K      | 9922A       | Second hand wins! |
            | 99965      | 99975       | Second hand wins! |
            | 99974      | 99975       | Second hand wins! |
            | 99652      | 99752       | Second hand wins! |
            | 99742      | 99752       | Second hand wins! |
            | 99752      | 99753       | Second hand wins! |
