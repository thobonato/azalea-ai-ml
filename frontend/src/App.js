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

  const handleSearch = async (model) => {
    console.log(`Searching with model: ${model}`);
    console.log(`Searching at: ${config.API_URL}/query/`);
    setIsLoading(true);
    setError(null);
    
    console.log('Trying to get response...');
    try {
      const response = await axios({
        method: 'post',
        url: `${config.API_URL}/query/`,
        data: {
          query: query,
          model: model,
          conversationId: conversationId
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        withCredentials: true
      });
      console.log('Received response...');
      console.log('Response:', response.data);
      
      setResult(response.data);
      setConversationId(response.data.conversationId);
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error.message);
      setError('An error occurred while processing your request. Please try again.');
    } finally {
      setIsLoading(false);
    }
    console.log('Search process completed.');
  };

  const handleCalculate = async () => {
    if (!query.trim()) {
      setError('Query cannot be empty');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await axios({
        method: 'post',
        url: `${config.API_URL}/calculate/`,
        data: {
          query: query,
          conversationId: conversationId
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        withCredentials: true
      });

      setResult(response.data);
      setConversationId(response.data.conversationId);
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error.message);
      setError('An error occurred while processing your request. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Eco-Friendly AI Model Selector</h1>
      <QueryInput 
        query={query} 
        setQuery={setQuery} 
        error={error}
        setError={setError}
        sendQuery={handleCalculate}
        isLoading={isLoading}
      />
      <ModelSelector 
        selectedModel={selectedModel} 
        setSelectedModel={setSelectedModel}
        handleSearch={handleSearch}
        isLoading={isLoading}
        query={query}
        conversationId={conversationId}
      />
      {error && <ErrorMessage message={error} />}
      {result && <SearchResults result={result} />}
    </div>
  );
};

export default App;