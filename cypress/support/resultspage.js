class ResultsPage {
  filters = new Array();

  clickNew() {
    cy.get('#stkTypId > .refinements > :nth-child(2) > .radio__label').click()
  }

  clickTouring() {
    cy.get("#trId-36434822").click()
  }

  checkFilters (key, value) {
    cy.get('.breadcrumbs').first().within(() => {
      cy.get(`li[data-dimension-id="${key}"]`).should('have.attr', 'data-value', value)
    })
  }

  selectResult(index) {
    cy.get(".listings>.shop-srp-listings__listing-container").eq(index).click()
  }
}

export default ResultsPage
