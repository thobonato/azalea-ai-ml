import React from 'react';

export const QueryInput = ({ query, setQuery, error, setError }) => {
  const handleChange = (e) => {
    setQuery(e.target.value);
    if (e.target.value.trim() === '') {
      setError('Query cannot be empty');
    }
  };

  return (
    <div className="mb-6">
      <label htmlFor="query" className="block text-sm font-medium text-gray-700 mb-2">Enter your query</label>
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
    </div>
  );
};

export default QueryInput;