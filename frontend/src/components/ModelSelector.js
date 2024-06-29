import React from 'react';

export const ModelSelector = ({ selectedModel, setSelectedModel, handleSearch, isLoading }) => (
  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
    {['google', 'chatgpt', 'mistral'].map((model) => (
      <div key={model} className="border border-gray-200 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow">
        <h2 className="text-xl font-bold mb-3 capitalize">{model}</h2>
        <button
          onClick={() => {
            setSelectedModel(model);
            handleSearch();
          }}
          disabled={isLoading}
          className={`w-full py-2 px-4 rounded-md transition-colors ${
            selectedModel === model
              ? 'bg-indigo-600 text-white hover:bg-indigo-700'
              : 'bg-white text-indigo-600 border border-indigo-600 hover:bg-indigo-50'
          } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
        >
          {isLoading ? 'Loading...' : `Use ${model}`}
        </button>
      </div>
    ))}
  </div>
);