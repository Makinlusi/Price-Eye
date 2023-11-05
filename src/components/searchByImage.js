const searchByImage = require('searchbyimage');

function searchImageByURL(imageURL) {
  // Using callback
  searchByImage(imageURL, (err, res) => {
    if (err) {ole.error(err);
      return;
    }
      cons
    console.log(res); // {guess: 'night'}
  });
}

module.exports = searchImageByURL;