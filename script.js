document.addEventListener('DOMContentLoaded', () => {
    const searchBtn = document.getElementById('search-btn');
    const resultsDiv = document.getElementById('results');

    searchBtn.addEventListener('click', () => {
        const category = document.getElementById('category').value;
        const playerCount = document.getElementById('player-count').value;
        const age = document.getElementById('age').value;
        const rating = document.getElementById('rating').value;

        // Send a GET request to your Flask server with the parameters
        fetch(`http://boardgames.pythonanywhere.com/search?category=${category}&playerCount=${playerCount}&age=${age}&rating=${rating}`)
            .then(response => response.json())
            .then(data => {
                // Clear previous results
                resultsDiv.innerHTML = '';

                // Loop through the received data and display it
                data.forEach(game => {
                    const gameDiv = document.createElement('div');
                    gameDiv.classList.add('game');

                    const name = document.createElement('h2');
                    name.textContent = game.name;

                    const minAge = document.createElement('p');
                    minAge.textContent = `Minimum Age: ${game['min-age']}`;

                    const year = document.createElement('p');
                    year.textContent = `Year Published: ${game.year}`;

                    const players = document.createElement('p');
                    players.textContent = `Players: ${game.players}`;

                    const rating = document.createElement('p');
                    rating.textContent = `Rating: ${game.rating}`;

                    gameDiv.appendChild(name);
                    gameDiv.appendChild(minAge);
                    gameDiv.appendChild(year);
                    gameDiv.appendChild(players);
                    gameDiv.appendChild(rating);

                    resultsDiv.appendChild(gameDiv);
                });
            });
    });
});
