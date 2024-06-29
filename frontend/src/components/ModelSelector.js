import React from 'react';

export const ModelSelector = ({ selectedModel, setSelectedModel, handleSearch, isLoading, query, conversationId }) => (
  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
    {['google', 'chatgpt', 'mistral'].map((model) => (
      <div key={model} className="border border-gray-200 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow">
        <h2 className="text-xl font-bold mb-3 capitalize">{model}</h2>
        <button
          onClick={() => {
            setSelectedModel(model);
            handleSearch(model); // This should trigger the function passed from App.js
          }}
          disabled={isLoading}
          className={`...`}
        >
            Use {model}
        </button>
      </div>
    ))}
  </div>
);

export default ModelSelector;


