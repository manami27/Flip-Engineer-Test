Feature: Open flip menu feature
  Background: common steps
    Given launch chrome browser
    When open flip landing page
    When verify success open landing page

  Scenario: Open login page
    When navigate to masuk menu
    Then verify success open login page

  Scenario: Open produk page
    When navigate to produk menu
    Then verify success open layanan flip page

  Scenario: Open karir page
    When navigate to karir menu
    Then verify success open karir page