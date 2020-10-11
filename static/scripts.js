
const isbns = [9780244951344, 9789291209910, 9788293516163, 9781560657699 , 9780198527565, 9780521421881 ,9780520221581, 9780719057298 , 9780307485779, 9788256019878];
let book_titles = []

API_KEY = 'GmNm9aeq6FeIaUjHXriO80RCzGrWEHuS';

// Get bestsellers list from NYT API
fetch('https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=' + API_KEY)
.then(response => response.json())
.then(data => {

  const bestsellers = data['results'];
  
  // Get title of top 10 best selling books
  for (i = 0; i < 10; i++) {

      book_titles.push(bestsellers[i]['title']);
  }

  console.log(book_titles);
});


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



