cart = document.getElementById('cart')
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


