
import React, { useState, useEffect} from 'react';
import axios from 'axios';

function PriceEye() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [searchResults, setSearchResults] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');
  const [itemName, setItemName] = useState('');



  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];

    if (file && allowedTypes.includes(file.type)) {
      setSelectedImage(file);
      setErrorMessage('');
    } else {
      // Handle invalid file type error
      setErrorMessage('Invalid file type. Please select an image file.');
    }
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append('image', selectedImage);

      const response = await axios.post('http://localhost:5000/search', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setSearchResults(response.data.itemSummaries);
      setItemName(response.data.itemSummaries[0].title);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

    // Calculate additional information about the search results
    const top10Items = searchResults && searchResults.length > 0 ? searchResults.slice(0, 10) : [];
    const avgPrice = top10Items.length > 0 ? (top10Items.reduce((total, item) => total + parseFloat(item.price.value), 0) / top10Items.length).toFixed(2) : 0;
    const lowestPrice = top10Items.length > 0 ? Math.min(...top10Items.map(item => parseFloat(item.price.value))) : 0;
    const highestPrice = top10Items.length > 0 ? Math.max(...top10Items.map(item => parseFloat(item.price.value))) : 0;

    return (
      <div className="p-6 bg-white dark:bg-gray-800 min-h-screen">
        <h1 className="text-3xl font-semibold text-gray-700 dark:text-white mb-4">
          Price-Eye 👀
        </h1>
        {errorMessage && (
          <div className="bg-red-500 text-white p-4">
            {errorMessage}
          </div>
        )}
        <div className="flex">
          <div className="w-3/4 pr-4 overflow-y-auto">
            <div className="mb-6 items-center mx-auto">
              {/* <label className="block text-sm text-gray-600 dark:text-gray-400 mb-2 text-left" htmlFor="upload">
                Upload an image:
              </label> */}
              <div className="flex items-center justify-between p-2 border-2 border-gray-300 rounded-md">
                <input
                  className="w-full text-gray-700 dark:text-gray-200"
                  id="upload"
                  type="file"
                  onChange={handleFileChange}
                />
                <button
                  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                  onClick={handleUpload}
                  disabled={!selectedImage} // Disable the button if no image is selected
                >
                  Upload
                </button>
              </div>
            </div>
            {searchResults.length > 0 && (
              <div>
                <h2 className="text-2xl font-semibold text-gray-700 dark:text-white mb-4">
                  Matching Listings
                </h2>
                <div className="grid gap-4">
                  {searchResults.slice(0, 10).map((item) => (
                    <div key={item.itemId}>
                      <img
                        alt={item.title}
                        className="object-cover w-full mb-2"
                        height="200"
                        src={item.thumbnailImages[0].imageUrl}
                        style={{
                          aspectRatio: "200/200",
                          objectFit: "cover",
                        }}
                        width="200"
                      />
                      <h3 className="font-semibold text-lg dark:text-gray-200">
                        {item.title}
                      </h3>
                      <p className="text-gray-600 dark:text-gray-400">
                        {"$"}{parseFloat(item.price.value)} 
                        <br />
                        {item.shippingOptions.length > 0 && item.shippingOptions[0].shippingCost && item.shippingOptions[0].shippingCost.value ? (
                          <>
                            Shipping: ${parseFloat(item.shippingOptions[0].shippingCost.value)}
                            <br />
                          </>
                        ) : (
                          "Shipping: Free"
                        )}
                      </p>
                      <a href={item.itemWebUrl} target="_blank" rel="noopener noreferrer">
                        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                          View Item
                        </button>
                      </a>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
          <div className="w-1/4">
            <div className="sticky top-0">
              {searchResults.length > 0 && (
                <div>
                  <h2 className="text-2xl font-semibold text-gray-700 dark:text-white mb-4">
                    Analytics of: {itemName}
                  </h2>
                  <div className="p-4 border-2 border-gray-300 rounded-md grid md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                      <p className="text-gray-600 dark:text-gray-400">Avg Price:</p>
                      <h3 className="font-semibold text-xl bg-green-200 dark:text-gray-200 rounded-md p-2">${avgPrice}</h3>
                    </div>
                    <div className="space-y-2">
                      <p className="text-gray-600 dark:text-gray-400">Matches:</p>
                      <h3 className="font-semibold text-xl bg-blue-200 dark:text-gray-200 rounded-md p-2">{top10Items.length}</h3>
                    </div>
                    <div className="space-y-2">
                      <p className="text-gray-600 dark:text-gray-400">Highest Price:</p>
                      <h3 className="font-semibold text-xl bg-red-200 dark:text-gray-200 rounded-md p-2">${highestPrice}</h3>
                    </div>
                    <div className="space-y-2">
                      <p className="text-gray-600 dark:text-gray-400">Lowest Price:</p>
                      <h3 className="font-semibold text-xl bg-purple-200 dark:text-gray-200 rounded-md p-2">${lowestPrice}</h3>
                    </div>
                    <div className="space-y-2">
                      <p className="text-gray-600 dark:text-gray-400">Avg Age:</p>
                      <h3 className="font-semibold text-xl bg-yellow-200 dark:text-gray-200 rounded-md p-2"> 3 days</h3>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    );
  }

  export default PriceEye;