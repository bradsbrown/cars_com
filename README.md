# Project Description and Steps

This is a project to automate the following actions using the Page Object Model:

- Go to Cars.com and:
  - Select `Used Cars`
  - Select Make `Honda`
  - Select Model `Pilot`
  - Select Price `50000`
  - Select Distance `100 miles`
  - Enter Zip Code 60008
  - Click `Search`
- Validate using assertions that 4 filters are displayed next to `Clear All`
  - Max Price is 50000
  - Selected Make is Honda
  - Selected Model is Pilot
  - Selected `Used`
- Select `New` radio button from New/Used
- Validate using assertion that the `New` filter is displayed and `Used` is NOT displayed
- Select Touring 8-Passemger from Trim
- Validate using assertion that the `Touring 8-Passenger` filter is displayed
- Select the second available car
- Validate using assertions:
  - Selected car title contains `Honda Pilot 8-Passenger For Sale`
  - `Check Availability` button is displayed
- In the Contact Seller section enter:
  - First Name: Car
  - Last Name: Owner
  - Email: carowner@yahoo.com
- Scroll down to `Payment Calculator` and take a screenshot


# My Notes - Python Tests

I built this using the POM as logically as I could see to assemble it.
I did run into some odd issues with Cars.com returning 503s across browsers,
almost as if they're using automation detection of some sort.
I couldn't find a way to bypass it entirely, so I tested this logic piecemeal
to ensure it made sense, then re-assembled it into a single test case for review.

You'll find the POMs in `/pages`, and the single test case in `tests/`.

## To run the tests

### Initial Setup
1. Set up a virtualenv (`python3 -m pip venv .venv`)
2. Activate the venv (`source .venv/bin/activate`)
3. Install the Python requirements (`pip install -r requirements`)
4. In addition, you'll need selenium (`brew install selenium-server-standalone`) and chromedriver (`brew install chromedriver`), as well as Google Chrome.

### On-Demand Runs
With the above setup in place, you can call `./run_tests.sh` to trigger a test run.


# My Notes - Cypress Tests

Given the issues I was having getting selenium to drive the automation in this case,
I decided to make another attempt in Cypress,
and ran into similar issues eventually.
I did not complete this code flow due to those failures,
but left it as a partial example of how I'd implement a POM test in Cypress.

## To run the tests

### Initial Setup
To set up requirements: `npm install`

### On-Demand Runs
With the setup in place, run: `$(npm bin)/cypress run -s cypress/integrations/cars.js`
