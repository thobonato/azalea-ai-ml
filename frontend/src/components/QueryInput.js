import React from 'react';

const QueryInput = ({ query, setQuery, error, setError, sendQuery, isLoading }) => {
  const handleChange = (e) => {
    setQuery(e.target.value);
    if (e.target.value.trim() === '') {
      setError('Query cannot be empty');
    } else {
      setError('');
    }
  };

  return (
    <div className="mb-6">
      <label htmlFor="query" className="block text-sm font-medium text-gray-700 mb-2">
        Enter your query
      </label>
      <input
        id="query"
        type="text"
        value={query}
        onChange={handleChange}
        placeholder="What would you like to know?"
        className={`w-full p-3 border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 ${
          error ? 'border-red-500' : 'border-gray-300'
        }`}
      />
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
      <div className="flex justify-center">
      <button
        onClick={sendQuery}
        disabled={isLoading}
        className={`mt-4 w-full py-2 px-4 rounded-md transition-colors ${
          isLoading
            ? 'bg-gray-400 cursor-not-allowed'
            : 'bg-indigo-600 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2'
        }`}
      >
        {isLoading ? 'Calculating...' : 'Calculate'}
      </button>
      </div>
    </div>
  );
};

export default QueryInput;