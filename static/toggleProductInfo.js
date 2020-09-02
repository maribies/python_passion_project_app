(function(){
  const products = document.getElementsByClassName('productContainer');

  [].forEach.call(products, element => {
    element.addEventListener("mouseover", toggleProductInfo);
  });

  function toggleProductInfo() {
    const images = this.getElementsByClassName('productImage');
    const stock = this.getElementsByClassName('stockContainer');
    const description = this.getElementsByClassName('productDescription');

    [].forEach.call(images, imageElement => {
      if (imageElement.classList.contains('show')) {
        imageElement.classList.remove('show');
        imageElement.classList.add('hide');
      } else {
        imageElement.classList.remove('hide');
        imageElement.classList.add('show');
      }
    });

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
})();

