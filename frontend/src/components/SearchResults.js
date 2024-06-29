import React from 'react';

export const SearchResults = ({ result }) => (
  <div className="border border-gray-200 p-6 rounded-md shadow-md">
    <h2 className="text-2xl font-bold mb-4">Search Results</h2>
    <p className="mb-6 text-gray-700">{result.result}</p>
    {result.ecoMetrics.energyUsage !== "N/A" && (
      <div className="bg-green-50 p-4 rounded-md">
        <h3 className="font-bold text-green-800 mb-2">Eco Metrics:</h3>
        <ul className="space-y-2">
          <li className="flex items-center">
            <span className="w-40">Energy Usage:</span>
            <span className="font-medium">{result.ecoMetrics.energyUsage} kWh</span>
          </li>
          <li className="flex items-center">
            <span className="w-40">Trees Saved:</span>
            <span className="font-medium">{result.ecoMetrics.treesSaved}</span>
          </li>
          <li className="flex items-center">
            <span className="w-40">Driving Avoided:</span>
            <span className="font-medium">{result.ecoMetrics.drivingAvoided} miles</span>
          </li>
        </ul>
      </div>
    )}
  </div>
);