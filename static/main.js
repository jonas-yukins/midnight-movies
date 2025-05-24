document.addEventListener("DOMContentLoaded", async function () {
    const moviesContainer = document.getElementById("popular-movies");
    if (moviesContainer) {
        try {
            const response = await fetch("/api/movies");
            let movies = await response.json();

            // Shuffle and select 3 random movies
            movies = movies.sort(() => 0.5 - Math.random()).slice(0, 3);

            moviesContainer.innerHTML = movies.map(createMovieCard).join("");
        } catch (error) {
            console.error("Error fetching movies:", error);
        }
    }
});

function createMovieCard(movie) {
    return `
        <div class="col-lg-3 col-md-4 col-sm-6">
            <a href="/view/${movie.id}" class="movie-card-link">
                <div class="card mb-4 shadow-sm movie-card" style="max-width: 300px;">
                    <img src="${movie.image}" class="card-img-top" alt="${movie.title} movie poster" style="height: 300px; object-fit: cover;">
                    <div class="card-body" style="padding: 12px;">
                        <h5 class="card-title" style="font-size: 1.1rem;">${movie.title} (${movie.year})</h5>
                        <p class="card-text" style="font-size: 0.9rem; height: 70px; overflow: hidden; text-overflow: ellipsis;">${movie.short_description}</p>
                        <a href="/view/${movie.id}" class="btn btn-primary movie-details-btn" style="width: 100%;">View Details</a>
                    </div>
                </div>
            </a>
        </div>
    `;
}

function validateSearch(event) {
    let form = event.target; // Get the form that triggered the event
    let searchBar = form.querySelector("input[type='search']"); // Get the search input within this form

    // Get the search query
    var query = searchBar.value.trim();

    // If the search query is empty, prevent form submission
    if (query === '') {
        searchBar.value = '';  // Clear the input
        searchBar.focus();  // Focus the correct search input
        return false;  // Prevent the form from submitting
    }
    return true;  // Proceed with the search if the query is valid
}
