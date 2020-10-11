// TODO: Get top 10 NY times bestsellers
const isbns = [9780244951344, 9789291209910, 9788293516163, 9781560657699 , 9780198527565, 9780521421881 ,9780520221581, 9780719057298 , 9780307485779, 9788256019878];

let img_nr = 0;

// For every element in isbns list
isbns.forEach(isbn => {
  
  // Get JSON response from Google Books API
  fetch('https://www.googleapis.com/books/v1/volumes?q=isbn=' + isbn)
  .then(response => response.json())
  .then(data => {
    
    // Get thumbnail image
    const image = data['items'][0]['volumeInfo']['imageLinks']['thumbnail'];

    // Get ID of slider element
    const carousel = document.querySelector("#slider" + img_nr);

    // Set source to image link
    carousel.src = image;  
    img_nr++;
    });
  });



