document.getElementById('recipeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const ingredients = document.getElementById('ingredients').value;
    
    // Format the input to space-separated string
    const formattedIngredients = ingredients.split(',').map(ingredient => ingredient.trim()).join(' ');

    fetch(`/recipe?ingredients=${encodeURIComponent(formattedIngredients)}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results

            for (let key in data) {
                const recipe = data[key];
                const recipeElement = document.createElement('div');
                recipeElement.innerHTML = `<h3>${recipe.recipe}</h3>
                                           <p>Score: ${recipe.score}</p>
                                           <p>Ingredients: ${recipe.ingredients}</p>
                                           <a href="${recipe.url}" target="_blank">View Recipe</a>`;
                resultsDiv.appendChild(recipeElement);
            }
        })
        .catch(error => console.error('Error:', error));
});
