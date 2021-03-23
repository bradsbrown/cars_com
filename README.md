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
