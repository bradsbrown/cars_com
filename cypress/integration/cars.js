import HomePage from "../support/homepage"
import ResultsPage from "../support/resultspage"

Cypress.on("uncaught:exception", (err, runnable) => {
  return false
});


describe('Page Load Test', () => {
  it('Visits the Cars.com Home Page', () => {
    // Load home page and fill out search
    const homePage=new HomePage()
    homePage.visit()
    homePage.placeSearch("Used Cars", "Honda", "Pilot", "$50,000", "100 Miles from", "60008")

    const resultsPage=new ResultsPage()
    // Check Filters to ensure epected count and values
    resultsPage.checkFilters("stkTypId", "28881")
    resultsPage.checkFilters("prMx", "$50,000")
    resultsPage.checkFilters("mkId", "20017")
    resultsPage.checkFilters("mdId", "21729")

    // Select New radio button and verify New is displayed
    resultsPage.clickNew()
    resultsPage.checkFilters("stkTypId", "28880")

    // Select Touring 8-Passenger from Trim and validate filter
    resultsPage.clickTouring()
    resultsPage.checkFilters("trId", "36434822")

    // Select the 2nd Entry
    resultsPage.selectResult(1)

    // TODO: run the result page
  })


});
