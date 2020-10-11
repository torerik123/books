const bestseller_isbns = [];

API_KEY = 'GmNm9aeq6FeIaUjHXriO80RCzGrWEHuS';

// Get bestsellers list from NYT API
fetch('https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=' + API_KEY)
.then(response => response.json())
.then(data => {

  const bestsellers = data['results'];
  
  // Get title of top 10 best selling books
  for (i = 0; i < 10; i++) {
    
    // If no ISBN exists
    if (!bestsellers[i]['isbns'][0]) {
      
      // TODO: GET ISBN BY TITLE - CALL FUNCTION

      console.log("NO ISBN FOUND");
    }

    else {
      const isbn13 = bestsellers[i]['isbns'][0]['isbn13'];
      bestseller_isbns.push(parseInt(isbn13));      
    }      
  }

  let img_nr = 0;

  // Book covers
  bestseller_isbns.forEach(isbn => {
    
    // Get JSON response from Google Books API
    fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn)
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
});







