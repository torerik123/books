// Wait for page to load
window.addEventListener('DOMContentLoaded', (event) => {  
    
    // Only load scripts on specific pages
    if (window.location.pathname=="/") {
        
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

            console.log("NO ISBN FOUND");
            }

            else {
            const isbn13 = bestsellers[i]['isbns'][0]['isbn13'];
            bestseller_isbns.push(parseInt(isbn13));      
            }      
        }

        let img_nr = 0;

        // Book covers, title and description front page
        bestseller_isbns.forEach(isbn => {
            
            // Get JSON response from Google Books API
            fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn)
            .then(response => response.json())
            .then(data => {
            
                console.log(data['items'][0]['volumeInfo']['title'])
                
                // Thumbnail image and authors
                const image = data['items'][0]['volumeInfo']['imageLinks']['thumbnail'];
                const authors = data['items'][0]['volumeInfo']['authors'];
                const book_title = data['items'][0]['volumeInfo']['title']
                
                // Get ID of img, title and author
                const carousel = document.querySelector("#coverimg" + img_nr);
                const title = document.querySelector("#title" + img_nr);
                const author = document.querySelector("#author" + img_nr);
                
                // Set source to image link
                carousel.src = image;

                // Insert title
                title.innerHTML = book_title;

                // Update authors      
                if (authors.length == 1) {
                    authors.forEach(element => {
                    author.innerHTML = element;
                    });
                }

                // If more than 1 author
                else {
                    let fulltext = "";
                    const last = authors[authors.length -1];
                    
                    authors.forEach(element => {
                    
                    // If last author name, don't add comma
                    if (element === last) {
                        fulltext += element;
                    }

                    // Author name + comma  
                    else {
                        fulltext += element + (', ');
                    }
                    });

                    // Insert authors
                    author.innerHTML = fulltext;

                }  
                img_nr++;
                });
            });
        });
    };


    // Search results
    if (window.location.pathname.match(/results/)) {
        
        // Get covers for search results
        let counter = 0;
  
        const isbn_list = document.querySelectorAll("#isbn");

        const covers = document.querySelectorAll(".bookcover");

        // Get JSON response from Google Books API
        covers.forEach(img => {
            fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn_list[counter].innerHTML)
            .then(response => response.json())
            .then(data => {
        
                if (data['items'] !== undefined) {
            
                    if (data['items'][0]['volumeInfo']['imageLinks'] !== undefined) {
            
                        // Get thumbnail image
                        const image = data['items'][0]['volumeInfo']['imageLinks']['thumbnail'];
            
                        // Set cover to image link
                        img.src = image;
                    } 
            
                    else {
                        console.log("Book cover not found")
                    }
                }
            });
            counter++;
        });
    };


    // Book info
    if (window.location.pathname.match(/book/)) {
            
        // Get cover on book info page
        const isbn = document.querySelector("#isbn").innerHTML;

        const cover = document.querySelector("#cover-img");

        // Get JSON response from Google Books API
        fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn)
        .then(response => response.json())
        .then(data => {
            
            // Get thumbnail image
            const image = data['items'][0]['volumeInfo']['imageLinks']['thumbnail'];
        
            // Set cover to image link
            cover.src = image;
            
            // Insert description
            const description = document.querySelector("#description");
            description.innerHTML = data['items'][0]['volumeInfo']['description']; 
            

            // Rating
            const rating = document.querySelector("#rating");
            rating.innerHTML = data['items'][0]['volumeInfo']['averageRating'] + "/5";
        
        });
    };
});






