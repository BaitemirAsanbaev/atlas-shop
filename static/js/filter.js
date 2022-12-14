
select = document.querySelector('#price ')
select.addEventListener('change', (e) => {
  e.preventDefault()
  window.location.href = `/catalog/${e.target.value}`
  window.scrollTo(self)

})


category = document.querySelector('#category ')
category.addEventListener('change', (e) => {
  e.preventDefault()
  window.location.href = `/catalog/${e.target.value}`
  window.scrollTo(self)

})
