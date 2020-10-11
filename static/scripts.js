// Only load on index page

// Get JSON response from Google Books API
fetch('https://www.googleapis.com/books/v1/volumes/RJxWIQOvoZUC')
  .then(response => response.json())
  .then(data => {
    
    // Imagelink from volumeinfo
    const image = data['volumeInfo']['imageLinks']['thumbnail'];

    
    const carousel = document.querySelectorAll("#slider");

    carousel.forEach(element => {
      element.src = image;  
    });
    
  });

