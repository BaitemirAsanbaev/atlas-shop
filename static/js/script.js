cart = document.getElementById('cart')


select = document.querySelector('#price ')
select.addEventListener('change', (e) => {
  e.preventDefault()
  window.location.href = `/catalog/${e.target.value}`
  window.scrollTo(self)

})

cartLink = document.getElementById('cartLink')

cartLink.addEventListener('click', (e) => {
  e.preventDefault()
  cart.className = 'anim'
  setTimeout(() => {
    cart.className = ''
    cart.style.opacity = '0'
    window.location.href = '/cart'
  }, 1000)
})

category = document.querySelector('#category ')
category.addEventListener('change', (e) => {
  e.preventDefault()
  window.location.href = `/catalog/${e.target.value}`
  window.scrollTo(self)

})
