import React from 'react';

const ModelSelector = ({ selectedModel, setSelectedModel, handleSearch, isLoading }) => {
  const models = ['google', 'chatgpt', 'mistral'];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
      {models.map((model) => (
        <div key={model} className="border border-gray-200 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow">
          <h2 className="text-xl font-bold mb-3 capitalize">{model}</h2>
          <button
            onClick={() => {
              setSelectedModel(model);
              handleSearch(model);
            }}
            disabled={isLoading}
            className={`w-full py-2 px-4 rounded-md transition-colors ${
              selectedModel === model
                ? 'bg-indigo-600 text-white hover:bg-indigo-700'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            Use {model}
          </button>
        </div>
      ))}
    </div>
  );
};

export default ModelSelector;