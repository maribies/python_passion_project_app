const products = document.getElementsByClassName('productContainer');

(function() {
  for (var i=0, len=products.length|0; i<len; i=i+1|0) {
    products[i].addEventListener("mouseover", toggleProductInfo);
  }
})();

function toggleProductInfo() {
  const images = this.getElementsByClassName('productImage');
  const stock = this.getElementsByClassName('stockContainer');
  const description = this.getElementsByClassName('productDescription');

  for (var i=0, len=images.length|0; i<len; i=i+1|0) {
    if (images[i].classList.contains('show')) {
      images[i].classList.remove('show');
      images[i].classList.add('hide');
    } else {
      images[i].classList.remove('hide');
      images[i].classList.add('show');
    }
  }

  if (description[0].classList.contains('hide')) {
    stock[0].classList.add('hide');
    description[0].classList.remove('hide');
    description[0].classList.add('show');
  } else {
    stock[0].classList.remove('hide');
    description[0].classList.remove('show');
    description[0].classList.add('hide');
  }
};
