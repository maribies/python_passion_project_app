(function(){
  const products = document.getElementsByClassName('productContainer');

  [].forEach.call(products, element => {
    // TODO: mouseenter has better UX, and maybe combined with mouseleave or something else
    // for mouseover to achieve the truely desired effect...
    element.addEventListener("mouseenter", e => { toggleProductInfo(element, e) });
  });

  function toggleProductInfo(element, e) {
    // TODO: Not producing desired results.
    e.stopPropagation();

    const images = element.getElementsByClassName('productImage');
    const stock = element.getElementsByClassName('stockContainer');
    const description = element.getElementsByClassName('productDescription');

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

