import React from 'react';

const modelNames = {
  mistral: 'Mistral',
  chatgpt: 'ChatGPT-4',
  google: 'Google Search',
};

const ModelCard = ({ model, data, selectedModel, setSelectedModel, handleSearch, isLoadingModel, setIsLoadingModel }) => {
  const modelName = modelNames[model] || model;
  
  return (
    <div className="bg-white border border-gray-200 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
      <h2 className="text-2xl font-bold mb-4">{modelName}</h2>
      <div className="mb-4">
        <span className="inline-block px-3 py-1 rounded-md bg-indigo-100 text-indigo-800 font-semibold">
          Score: {data.score?.toFixed(2) ?? 'N/A'}
        </span>
      </div>
      <ul className="space-y-2 mb-6">
        <li>⚡️ {data.cost?.toFixed(2) ?? 'N/A'} watt-hours used</li>
        <li>💧 {data.water?.toFixed(3) ?? 'N/A'} ounces used</li>
        {/* <li>🌳 {data.bag?.toFixed(4) ?? 'N/A'} bags used</li> */}
        <li>🚗 {data.feet?.toFixed() ?? 'N/A'} feet of driving used</li>
      </ul>
      <button
        onClick={() => {
          setSelectedModel(model);
          handleSearch(model);
        }}
        disabled={isLoadingModel}
        className={`w-full py-2 px-4 rounded-md transition-colors ${
          isLoadingModel
            ? 'bg-indigo-600 text-white hover:bg-indigo-700'
            : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
        }`}
      >
         {isLoadingModel ? 'Calculating...' : `Use ${modelName}`}
          {isLoadingModel ? 'true' : 'false'}
      </button>
    </div>
  );
};

const ModelSelector = ({ selectedModel, setSelectedModel, handleSearch, isLoadingModel,setIsLoadingModel, modelData }) => {
  if (!modelData || typeof modelData !== 'object' || Object.keys(modelData).length === 0) {
    return <div className="text-center text-gray-600">No model data available. Please enter a query.</div>;
  }

const {complexity, ...models} = modelData;
console.log('modelData:', modelData);


  return (
    <div>
      <div className="mb-6 p-4 bg-gray-100 rounded-lg">
        <h2 className="text-xl font-semibold mb-2">Query Information</h2>
        <p className="text-gray-700">
          Estimated query complexity: <span className="font-medium">{complexity ?? 'N/A'}</span>
        </p>
    </div>
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {Object.entries(models).map(([model, data]) => (
          <ModelCard
            key={model}
            model={model}
            data={data}
            selectedModel={selectedModel}
            setSelectedModel={setSelectedModel}
            handleSearch={handleSearch}
            isLoadingModel={isLoadingModel}
            setIsLoadingModel={setIsLoadingModel}
          />
      ))}
    </div>
    </div>
  );
};

export default ModelSelector;