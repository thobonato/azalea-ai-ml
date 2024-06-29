import React, { useState } from 'react';
import axios from 'axios';
import QueryInput from './components/QueryInput';
import ModelSelector from './components/ModelSelector';
import SearchResults from './components/SearchResults';
import ErrorMessage from './components/ErrorMessage';
import config from './config';

const App = () => {
  const [query, setQuery] = useState('');
  const [selectedModel, setSelectedModel] = useState('');
  const [result, setResult] = useState(null);
  const [conversationId, setConversationId] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async () => {
    setError(null);
    setIsLoading(true);
    try {
      if (selectedModel === 'chatgpt') {
        window.open(`https://chat.openai.com/`, '_blank');
        setResult({
          result: "Please use your ChatGPT account to process this query: " + query,
          ecoMetrics: {
            energyUsage: "N/A",
            treesSaved: "N/A",
            drivingAvoided: "N/A"
          }
        });
      } else {
        const response = await axios.post(`${config.API_URL}/query`, {
          query,
          model: selectedModel,
          conversationId
        });
        setResult(response.data);
        setConversationId(response.data.conversationId);
      }
    } catch (error) {
      setError('An error occurred while processing your request. Please try again.');
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Eco-Friendly AI Model Selector</h1>
      <QueryInput query={query} setQuery={setQuery} />
      <ModelSelector 
        selectedModel={selectedModel} 
        setSelectedModel={setSelectedModel}
        handleSearch={handleSearch}
        isLoading={isLoading}
      />
      {error && <ErrorMessage message={error} />}
      {result && <SearchResults result={result} />}
    </div>
  );
};

export default App;
