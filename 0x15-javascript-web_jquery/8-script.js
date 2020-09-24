$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const films = data.results;
  for (const i in films) {
    $('UL#list_movies').append('<li>' + films[i].title + '</li>');
  }
});
