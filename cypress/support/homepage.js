class HomePage {
  visit() {
    cy.visit("https://cars.com")
  }

  placeSearch(stockType, makeType, modelType, priceMax, radius, zipCode) {
    cy.get('select[name="stockType"]').select(stockType)
    cy.get('select[name="makeId"]').select(makeType)
    cy.get('select[name="modelId"]').select(modelType)
    cy.get('select[name="priceMax"]').select(priceMax)
    cy.get('select[name="radius"]').select(radius)
    cy.get('input[name="zip"]').type(zipCode)
    cy.get('input[type="submit"]').click()
  }
}

export default HomePage
